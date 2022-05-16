duration = int(input("Введите продолжительность времени в секундах: "))
day = duration // 86400
hour = duration % 86400 // 3600
minute = duration % 3600 // 60
second = duration % 60
if day == 0 and hour == 0 and minute == 0:
    print(second, "сек")
elif day == 0 and hour == 0:
    print(minute, "мин", second, "сек")
elif day == 0:
    print(hour, "час", minute, "мин", second, "сек")
else:
    print(day, "дн", hour, "час", minute, "мин", second, "сек")
