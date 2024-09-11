pip install requests pandas

import requests
import pandas as pd

url = 'https://www.sofascore.com/api/v1/event/12268525/statistics'

headers = { #simulando navegador
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
  data = response.json()

  all_data = []

  for match_stat in data['statistics']:
    period = match_stat['period']

    for group in match_stat['groups']:
      group_name = group['groupName']

      for item in group['statisticsItems']:
        stat_name = item.get('name')
        home_value = item.get('home')
        away_value = item.get('away')

        all_data.append({
            'Tempo': period,
            'Análise': group_name,
            'Estatística': stat_name,
            'Manchester United': home_value,
            'Liverpool': away_value })

  df = pd.DataFrame(all_data) #DataFrame

df