# pip install requests pandas

import requests #requisiçoes http // get, post, put, delete
import pandas as pd #biblioteca de manipulação de dados

url = 'https://www.sofascore.com/api/v1/event/12117219/statistics'

headers = { #simulando navegador
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"
}

response = requests.get(url, headers=headers) #pegando requisições com url e com o headers

if response.status_code == 200: #se a requisição der certo
  data = response.json() #faz um arquivo json

  all_data = [] #todas as informaçoes requisitadas

  for match_stat in data['statistics']: #pegue as estatisticas
    period = match_stat['period'] #tempo de jogo

    for group in match_stat['groups']: #grupos de informações coletadas
      group_name = group['groupName']

      for item in group['statisticsItems']: #itens de estatísticas do jogo
        stat_name = item.get('name') #nomes dos itens
        home_value = item.get('home') #time da casa
        away_value = item.get('away') #time de fora

        all_data.append({
            'Tempo': period,
            'Análise': group_name,
            'Estatística': stat_name,
            'Corinthians': home_value,
            'Flamengo': away_value })

  df = pd.DataFrame(all_data) #DataFrame

df
