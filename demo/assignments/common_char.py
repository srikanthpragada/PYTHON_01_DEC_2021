def common_char(*names):
    chars = set(names[0])
    for n in names[1:]:
        chars = chars & set(n)

    print(chars)


common_char('abc', 'bbc', 'xbqc')
common_char('abc', 'pqr', 'xyz')

