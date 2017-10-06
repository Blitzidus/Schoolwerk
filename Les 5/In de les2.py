def test_a_word(word):
    if len(word) > 3:
        for char in word:
            if char == 'a':
                return True
    else:
        return False

print(test_a_word('rere'))

