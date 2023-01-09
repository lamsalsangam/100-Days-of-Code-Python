def DecimaltoBinary(num):
    if num > 1:
        DecimaltoBinary(num//2)
    print(num % 2, end="")


DecimaltoBinary(46)
