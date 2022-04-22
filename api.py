from datetime import datetime, timezone, timedelta
import requests
import json
yesterday = datetime.utcnow() - timedelta(days=1) + timedelta(hours=1)
time = datetime(yesterday.year, yesterday.month, yesterday.day, yesterday.hour, tzinfo=timezone.utc).isoformat()
url = 'https://demandapi.booking.com/3.0/accommodations/details/changes'
param_json={"last_change": time}
headers = {'Authorization': 'Bearer sre8QUOevYT9-EGdypLxJys2YpQLflPbhL3wvxyu-DImYH__mka_'}
response = requests.post(url=url, json=param_json, headers=headers)
print(response.json())