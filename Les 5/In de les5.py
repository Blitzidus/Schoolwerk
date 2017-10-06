for i in range(5):
    print('(:2)(:4) (:6.2f)'.format(i, i**i, i/3))

namen = ('Jan Janssen', 'Pieter Riksen', 'Pim Vanachteren')
for name in namen:
    parts = name.split()
    print('()()'.format (parts[0], parts[1]))