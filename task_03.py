def encoding(s):
    string = ""
    total = 0
    index = s[0]
    for i in s:
        if i == index:
            total += 1
        else:
            string += str(total) + index
            total = 1
            index = i
    string += str(total) + i
    return string


def decoding(s):
    decoder_string = ""
    for i in range(0,len(s) -1, 2):
        decoder_string += int(s[i]) * s[i + 1]
    return  decoder_string


cod = encoding(input("Введите стороку для кодировки "))
decod = decoding(cod)
print(f"Закодированная сторока  : {cod}")
print(f"Раскодированная строка  : {decod}")