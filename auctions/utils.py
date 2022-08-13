# 
# 
# https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date=20220801&json
# Примітка: Поточного дня буде відображатися офіційний курс гривні до іноземних валют, встановлений НА ЗАВТРА за схемою:

#     До 15:30* – відображається лише офіційний курс гривні до іноземних валют, що встановлюється 1 раз на місяць.
#     Після 15:30* - офіційний курс, зазначений у п.1, та офіційний курс гривні до іноземних валют, що встановлюється щодня.

# * пункт 4 Порядку встановлення офіційного курсу гривні до іноземних валют та розрахунку довідкового значення курсу гривні до 
# долара США й облікової ціни банківських металів та їх оприлюднення від 01.03.2021 № 79-рш (зі змінами, внесеними рішенням Правління НБУ від 31.12.2021 № 659-рш).
# Дані у форматі
#  [
# { 
# "r030":840,"txt":"Долар США","rate":36.5686,"cc":"USD","exchangedate":"01.08.2022"
#  }
# ]

import json
from datetime import date
from urllib.request import urlopen

def current_exchange_rate(currency):
    
    data_str = date.today().strftime("%Y%m%d")
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&date={data_str}&json"
    page_json = urlopen(url).read()
   
    if len(page_json)>6:
        dict_from_json = dict(json.loads(page_json)[0])
        return dict_from_json
    else:
        return False