from datetime import datetime

tiempo_str = "1995-12-26T14:50:17.170000Z"

tiempo_datetime = datetime.strptime(tiempo_str, "%Y-%m-%dT%H:%M:%S.%fZ")

tiempo_date = tiempo_datetime.date()

print(tiempo_date)  
