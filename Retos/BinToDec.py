def bintodec(binario):
    if len(binario) == 1:
        return int(binario)
    else:
        return int(binario[-1]) + 2 * bintodec(binario[:-1])

binario = "111111"
dec = bintodec(binario)
print(dec)

#Hecho por Christian Lombardi
