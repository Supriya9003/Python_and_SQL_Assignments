s = "a10b2c2"
res=""
i = 0

while i< len(s):
    char = s[i]
    i += 1

    num_str = ""
    while i<len(s) and s[i].isdigit():
        num_str += s[i]
        i += 1

    res += char*int(num_str)

print("input:", s)
print("out put:", res)