def seizoen(maand):
    if maand < 0 or maand > 12:
        return 'Er zijn 12 maanden, vriendelijke vriend.'

    if maand > 3 and maand < 5:
        return 'lente'
    elif maand > 5 and maand < 9:
        return 'zomer'
    elif maand > 9 and maand < 11:
        return 'herfst'
    elif maand > 11 or maand < 3:
        return 'winter'

print(seizoen(-2))
print(seizoen(2))
print(seizoen(8))
print(seizoen(12))
print(seizoen(13))
