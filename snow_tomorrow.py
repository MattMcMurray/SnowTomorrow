import time
import json
import os
import requests

def get_forecast(event, context):
  API_KEY=os.getenv('OPEN_WEATHER_MAP_API_KEY', None)
  IFTTT_URL=os.getenv('IFTTT_URL', None)

  if API_KEY is None:
      raise ValueError('OPEN_WEATHER_MAP_API_KEY env var is not present')
      
  if IFTTT_URL is None:
      raise ValueError('IFTTT_URL env var is not present')

  LOCATION='Winnipeg,CA'
  REQUEST_URL='http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}'.format(LOCATION, API_KEY)

  r = requests.get(REQUEST_URL)

  now = time.time()
  sec_in_day = 24 * 60 * 60
  sec_in_hour = 60 * 60
  tmrw = now + sec_in_day + (2 * sec_in_hour)

  relevant_forecasts = []
  for entry in r.json()['list']:
      if entry['dt'] > tmrw:
          break

      if entry['weather'][0]['id'] >= 600 and entry['weather'][0]['id'] < 700:
          relevant_forecasts.append(entry['weather'][0]['description'])

  # use a set to remove duplicate entries
  relevant_forecasts = list(set(relevant_forecasts))

  if len(relevant_forecasts) > 0:
    requests.post(IFTTT_URL, {'value1': json.dumps(relevant_forecasts)})

if __name__ == '__main__':
  get_forecast(None, None)
