year = int(input("Введіть рік: "))

if year % 400 == 0:
    print(year, "є високосним роком")
elif year % 100 == 0:
    print(year, "не є високосним роком")
elif year % 4 == 0:
    print(year, "є високосним роком")
else:
    print(year, "не є високосним роком")