from operaçoes import *

while True:
    print ("Digite 1 para somar")
    print ("Digite 2 para subtrair")
    print ("Digite 3 para multiplica")
    print ("Digite 4 para dividir")
    print ("Se vossa senhoria quiser cancelar digite 0 ")

    Abacaxi= input("Qual operação a senhora(o) deseja ?")
    if Abacaxi == "1":
        x=int(input("Qual número a quirida(o)gostaria de escolher?"))
        y=int(input("Qual número a quirida(o)gostaria de escolher?"))
        print(soma(x,y))
        print(emoji.emojize(":red_heart:"))
    elif Abacaxi == "2":
        x=int(input("Qual número a quirida(o)gostaria de escolher?"))
        y=int(input("Qual número a quirida(o)gostaria de escolher?"))
        print(sub(x,y))
        print(emoji.emojize(":red_heart:"))
    elif Abacaxi == "3":
        x=int(input("Qual número a quirida(o)gostaria de escolher?"))
        y=int(input("Qual número a quirida(o)gostaria de escolher?"))
        print(mult(x,y))
        print(emoji.emojize(":red_heart:"))
    elif Abacaxi == "4":
        x=int(input("Qual número a quirida(o)gostaria de escolher?"))
        y=int(input("Qual número a quirida(o)gostaria de escolher?"))
        print(div(x,y))
        print(emoji.emojize(":red_heart:"))
    elif Abacaxi == "0":
        print(emoji.emojize(":red_heart:"))
        break
    else:
        continue