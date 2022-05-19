
duration = int(input('введите число '))

if duration <= 60:
    print(duration, 'сек')

# минуты
if duration > 60 and duration < 3600:
    if duration / 60 != 0:
        min = duration // 60
        sek = duration - (min * 60)
        print(min, 'мин', sek, 'сек')
# часы
if duration >= 3600 and duration < 86400:
    if duration / 3600 != 0:
        hour = duration // 3600
        min = ((duration - (hour * 3600)) // 60)
        if min != 0:
            sek = (duration - (hour * 3600) - (min * 60))

        #    sek = min * 60
        # print(hour, 'час', min, 'мин')
        print(hour, 'час', min, 'мин', sek, 'сек')

# DAYS
if duration >= 86400:
    if duration / 86400 != 0:
        day = duration // 86400
        hour = (duration - (day * 86400)) // 3600  # duration// 3600
        min = (duration - (day * 86400) - (hour * 3600)) // 60
        sek = duration - (day * 86400) - (hour * 3600) - min * 60
        print(day, 'дн', hour, 'час', min, 'мин', sek, 'сек')