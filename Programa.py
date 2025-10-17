from operaçoes import *

while True:
    print('Digite 1 para somar.')
    print('Digite 2 para subtrair.')
    print('Digite 3 para multiplicar.')
    print('Digite 4 para dividir.')
    print('Digite 0 para cancelar.')
    op=int(input("Qual operação vós mercê deseja realizar: "))

    if op == 1:
        x=int(input("Qual o primeiro número da soma?: "))
        y=int(input("Qual o segundo número da soma?: "))
        print(soma(x, y))
    elif op == 2:
        x=int(input("Qual o primeiro número da subtração?: "))
        y=int(input("Qual o segundo número da subtração?: "))
        print(sub(x, y))
    elif op == 3:
        x=int(input("Qual o primeiro número da multiplicação?: "))
        y=int(input("Qual o segundo número da multiplicação?: "))
        print(mult(x, y))
    elif op == 4:
        x=int(input("Qual o primeiro número da divisão?: "))
        y=int(input("Qual o segundo número da divisão?: "))
        if y == 0:
            print("[error] Esta divisão não corresponde aos parâmetros da sociedade!")
        else:
            print(div(x, y))
    elif op == 0:
        break
    else:
        continue