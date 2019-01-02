from django.db.models.signals import post_save
from django.dispatch import receiver
from compendium_app.models import Journal, Idea, Decision, Principle, Aphorism, Observation, Lesson
import re


@receiver(post_save, sender=Journal)
def data_dissemination(sender, instance, **kwargs):
    models = [{"record_type": "idea", "open_tag": "#i", "close_tag": "i#"},
              {"record_type": "principle", "open_tag": "#p", "close_tag": "p#"},
              {"record_type": "decision", "open_tag": "#d", "close_tag": "d#"},
              {"record_type": "aphorism", "open_tag": "#a", "close_tag": "a#"},
              {"record_type": "observation", "open_tag": "#o", "close_tag": "o#"},
              {"record_type": "lesson", "open_tag": "#l", "close_tag": "l#"}
              ]
    x_list = []
    for m in models:
        entry = re.findall(m["open_tag"] + "(.*?)" + m["close_tag"], instance.entry, re.DOTALL)
        for x in entry:
            x_record = {}
            x_record["record_type"] = m["record_type"]
            # create x logic
            x_value = re.sub('-- .*? --', '', x)
            x_value = x_value.strip()
            x_record[m['record_type']] = x_value
            # create details logic
            details = re.findall("-- (.*?) --", x)
            for d in details:
                # create details logic
                elements = re.findall("(?:^|(?<=,))[^,]*", d)
                for e in elements:
                    e = e.strip()
                    e_list = e.split(":")
                    e_list2 = []
                    for ie in e_list:
                        ier = ie.strip()
                        e_list2.append(ier)
                    x_record[e_list2[0]] = e_list2[1]
            x_list.append(x_record)
    for r in x_list:
        if r["record_type"] == 'idea':
            i = Idea(entry=r['idea'], idea=r['idea'], created_by=instance.created_by, journal=instance)
            i.save()
        elif r["record_type"] == 'decision':
            d = Decision(entry=r['decision'], decision=r['decision'], created_by=instance.created_by, journal=instance)
            d.save()
        elif r["record_type"] == 'principle':
            p = Principle(entry=r['principle'], principle=r['principle'], created_by=instance.created_by, journal=instance)
            p.save()
        elif r["record_type"] == 'aphorism':
            a = Aphorism(entry=r['aphorism'], aphorism=r['aphorism'], created_by=instance.created_by, journal=instance)
            a.save()
        elif r["record_type"] == 'observation':
            o = Observation(entry=r['observation'], observation=r['observation'], created_by=instance.created_by, journal=instance)
            o.save()
        elif r["record_type"] == 'lesson':
            l = Lesson(entry=r['lesson'], lesson=r['lesson'], created_by=instance.created_by, journal=instance)
            l.save()
