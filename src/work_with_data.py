import os

import httpx
from playhouse.db_url import connect

db = connect(os.environ.get('DB_CONNECTION_STRING'))
login = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')
url = os.environ.get('URL')

cursor = db.cursor()


@db.atomic()
def delete_data(date):
    cursor.execute(f"Delete FROM history_item where created <= '{date}'")
    cursor.execute(f"Delete FROM duration_trend where created <= '{date}'")
    cursor.execute(f"Delete FROM categories_trend where created <= '{date}'")
    cursor.execute(f"Delete FROM history_trend where created <= '{date}'")
    cursor.execute(f"Delete FROM retry_trend where created <= '{date}'")


def rebuild_report():
    httpx.put(f'{url}', data={'collect_history': 'false'}, auth=(f'{login}', f'{password}'))
