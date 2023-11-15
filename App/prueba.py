from datetime import datetime

fecha_str = '2012-12-12'

fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()

año = fecha_obj.year

print(año)
