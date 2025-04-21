def insert(s, char):
    result = ""
    for i in range(len(s)):
        result += s[i]
        result += char
    return result[:-1]


original_str, insert_char = input().split()
new_str = insert(original_str, insert_char)
print(new_str)
    