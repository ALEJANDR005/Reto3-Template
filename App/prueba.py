from tabulate import tabulate
from datetime import time
import datetime

element = {'code': 'p000e5bu', 'time': datetime.date(2005, 12, 2), 'lat': '25.025', 'long': '141.634', 'mag': 4.1, 'nst': 88.0, 'title': 'M 4.1 - Volcano Islands, Japan region', 'depth': 516.8, 'felt': 'Unknown', 'cdi': 'Unknown', 'mmi': 'Unknown', 'tsunami': False}

keys = element.keys()

table = tabulate([element.values()], headers=keys, tablefmt="grid")

print(table)