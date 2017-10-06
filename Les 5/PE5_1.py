def convert(celcius):
    fahrenheit = celcius * 1.8 + 32
    return(fahrenheit)

def table():
    print('F        C')
    for x in range(-30, 41, 10):
        print('{:>5}  {:>5}'.format(convert(x), float(x)))

table()