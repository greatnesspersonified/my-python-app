from datetime import datetime
from datetime import date

now = datetime.now()
print(now)

print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d/%B/%Y %H:%M:%S"))
print(now.strftime("%d/%b/%Y %H:%M:%S"))
print(date.today().strftime("%d-%m-%Y"))
print(date.today().strftime("%d-%B-%Y"))