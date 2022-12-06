s =input().split()
new_s = ""
for i in range(len(s)):
    if "абв" not in s[i]:
        new_s += s[i] + ' '
print(new_s)