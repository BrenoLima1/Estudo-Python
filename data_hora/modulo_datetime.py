# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

data_str = '2022-04-20 07:49:30'
data_str_formato = '%Y-%m-%d %H:%M:%S'

data = datetime.strptime(data_str, data_str_formato)

print(data)
print(datetime.now(timezone('America/Sao_Paulo')))

print('\n###\n')

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)
diferenca = data_fim - data_inicio

print(diferenca)

print('\n###\n')
print('\n###\n')

# Formatando data

fmt = '%d%m%Y'
# data = datetime(2025, 12, 13, 7, 59, 23)
data = datetime.strptime('2025 12 13 07 59 23', '%Y %m %d %H %M %S')
