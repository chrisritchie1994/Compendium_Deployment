import boto3
import json
import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
import datetime


def data_extraction(db_cred, extraction_tables):
    connection = psycopg2.connect(user=db_cred['user'],
                                   password=db_cred['password'],
                                   host=db_cred['host'],
                                   port=db_cred['port'],
                                   database=db_cred['database'])
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    for t in extraction_tables:
        cursor.execute("""SELECT * FROM """ + t + """;""")
        data = cursor.fetchall()
        d = pd.DataFrame(data)
        d.to_csv(r"{}.csv".format(t))

    if connection:
        cursor.close()
        connection.close()


def send_to_compendium_backup(aws_cred, extraction_tables):
    s3 = boto3.resource("s3",
                        aws_access_key_id=aws_cred["aws_access_key_id"],
                        aws_secret_access_key=aws_cred['aws_secret_access_key'])
    bucket = s3.Bucket('compendium-backup')
    now = datetime.datetime.today().strftime('%Y-%m-%d')
    for t in extraction_tables:
        bucket.upload_file(t + '.csv', now + '-Compendium_Prod/' + t + '.csv')


if __name__ == '__main__':
    with open('aws_credentials.json') as f:
        aws_cred = json.load(f)
    with open('database_credentials.json') as f:
        db_cred = json.load(f)
    extraction_tables = ["compendium_app_journal", "auth_user"]
    data_extraction(db_cred, extraction_tables)
    send_to_compendium_backup(aws_cred, extraction_tables)

