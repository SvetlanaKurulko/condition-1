# Користувач вводить з клавіатури кількість метрів.
# Залежно від вибору користувача програма переводить метри милі, дюйми або ярди.

meters = float(input("Введіть кількість метрів: "))

print("Оберіть одиницю виміру для переведення:")
print("1. Метри в милі")
print("2. Метри в дюйми")
print("3. Метри в ярди")

choice = int(input("Ваш вибір (1/2/3): "))

if choice == 1:
    miles = meters * 0.000621371
    print(f"{meters} метрів дорівнює {miles} миль")
elif choice == 2:
    inches = meters * 39.3701
    print(f"{meters} метрів дорівнює {inches} дюймів")
elif choice == 3:
    yards = meters * 1.09361
    print(f"{meters} метрів дорівнює {yards} ярдів")
else:
    print("Невірний вибір")



