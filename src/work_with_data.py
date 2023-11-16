import os

import httpx
from playhouse.db_url import connect

db = connect(os.environ['DB_CONNECTION_STRING'])
login = os.environ['LOGIN']
password = os.environ['PASSWORD']
url = os.environ['URL']

cursor = db.cursor()


@db.atomic()
def delete_data(date):
    cursor.execute(f"Delete FROM history_item where created <= '{date}'")
    cursor.execute(f"Delete FROM duration_trend where created <= '{date}'")
    cursor.execute(f"Delete FROM categories_trend where created <= '{date}'")
    cursor.execute(f"Delete FROM history_trend where created <= '{date}'")
    cursor.execute(f"Delete FROM retry_trend where created <= '{date}'")


def rebuild_report():
    httpx.put(f'{url}/report/build', data={'collect_history': 'false'}, auth=(login, password))
