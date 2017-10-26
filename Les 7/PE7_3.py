dictionary = {
    "Jan": 7,
    "Kees": 10,
    "Henk": 8,
    "Jaap": 5,
    "Peter": 6,
    "Dap": 9,
    "Hendrik": 2,
    "Cees": 4,
}

for name, mark in dictionary.items():
    if mark >= 9:
        print("{} heeft hoger dan een 9 ({})".format(name, mark))
