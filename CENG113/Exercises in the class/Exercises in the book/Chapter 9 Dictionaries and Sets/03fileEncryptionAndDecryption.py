codes = {"A" : "%", "a" : "9", "B": "@" , "b" : "#" , "C" : "=", "c" : "/"}
keys = list(codes.keys())
values = list(codes.values())

with open("03text.txt", "r", encoding="utf8") as f:
    content = f.readlines()

with open("03textencrypt.txt", "w", encoding="utf8") as w:
    for line in content:
        encrypted = ""
        for char in line:
            if char in keys:
                char = codes[char]
            encrypted = encrypted + char
        w.writelines(encrypted)

with open("03textencrypt.txt", "r", encoding="utf8") as f:
    content = f.readlines()

with open("03textdecrypt.txt", "w", encoding="utf8") as w:
    for line in content:
        decrypted = ""
        for char in line:
            if char in values:
                index = values.index(char)
                char = keys[index]
            decrypted = decrypted + char
        w.writelines(decrypted)
