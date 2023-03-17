import calendar
import os
os.system('cls||clear')
print("Добро пожаловать в календарь! \n") 

year = int(input("Пожалуйста введите год: "))


os.system('cls||clear')
month = int(input("Пожалуйста введите номер месяца: "))
os.system('cls||clear')
print(calendar.month(year,month))

print("Всего хорошего \n") 