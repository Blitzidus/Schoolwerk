def convert(celsius):
    return celsius * 1.8 + 32

def table():
    print("   F      C")
    for temp in range(-30, 41, 10):
        print('{:>6} {:>6}'.format(convert(temp), float(temp)))

table()
