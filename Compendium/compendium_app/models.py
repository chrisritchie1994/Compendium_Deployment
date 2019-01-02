from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Journal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=200)
    entry = models.TextField()
    rating = models.IntegerField(default=5)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    data_types = (
        ("Real", "Real"),
        ("Test", "Test")
    )
    data_type = models.CharField(
        max_length=4,
        choices=data_types,
        default="Real"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']


class Idea(models.Model):
    idea_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    entry = models.TextField()
    idea = models.TextField()
    application = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.idea

    class Meta:
        ordering = ['-pk']


class Decision(models.Model):
    decision_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    entry = models.TextField()
    decision = models.TextField()
    application = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.decision

    class Meta:
        ordering = ['-pk']


class Principle(models.Model):
    principle_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    entry = models.TextField()
    principle = models.TextField()
    application = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.principle

    class Meta:
        ordering = ['-pk']


class Aphorism(models.Model):
    aphorism_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    entry = models.TextField()
    aphorism = models.TextField()
    application = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.aphorism

    class Meta:
        ordering = ['-pk']


class Observation(models.Model):
    observation_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    entry = models.TextField()
    observation = models.TextField()
    application = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.observation

    class Meta:
        ordering = ['-pk']


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    entry = models.TextField()
    lesson = models.TextField()
    application = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson

    class Meta:
        ordering = ['-pk']


class Subentry(models.Model):
    subentries_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    record_type = models.CharField(max_length=10)
    open_tag = models.CharField(max_length=10)
    close_tag = models.CharField(max_length=10)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk']


