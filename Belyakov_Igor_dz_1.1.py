duration = int(input())
days = duration // 3600 // 24
hours = (duration % 86400) // 3600
minutes = (duration % 3600) // 60
seconds = (duration % 60)
if days == 0 and hours == 0 and minutes == 0:
    print(seconds, 'сек')
elif days == 0 and hours == 0:
    print(minutes, 'мин', seconds, 'сек')
elif days == 0:
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
else:
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
