def count_common_chars(s1, s2):
    return len(set(s1) & set(s2))


def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


print(count_common_chars('abcdeedaaa', 'deeafxyz'))
print(count_upper('AbcAXdeeD'))
