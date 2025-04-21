def mystrcmp(str1, str2):
    i = 0
    while i < len(str1) and i < len(str2):
        if str1[i] != str2[i]:
            return ord(str1[i]) - ord(str2[i])
        i += 1
    if i < len(str1):
        return ord(str1[i])
    elif i < len(str2):
        return -ord(str2[i])
    return 0

str1, str2 = input().split()
result = mystrcmp(str1, str2)
print(result)
    