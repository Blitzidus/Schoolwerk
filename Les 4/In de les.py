def delete_klinkers(woord):
    result = ''
    for char in woord:
        if char not in 'aeiou':
            result = result + char
    return result

print('The result is:' + delete_klinkers('vis'))