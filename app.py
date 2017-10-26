from modules.ponto import Point

def main(args=[]):
    inputx = int(input("\nInsira o valor de X1 >> "))
    inputy = int(input("\nInsira o valor de Y1 >> "))

    P1 = Point(inputx, inputy)

    inputx = int(input("\nInsira o valor de X2 >> "))
    inputy = int(input("\nInsira o valor de Y2 >> "))

    P2 = Point(inputx, inputy)

    PS = P1 + P2

    print("\nPonto Soma definido:\n")

    print(P1)
    
    print('        +')
    
    print(P2)
    
    print('        =')

    print(PS)

    print("\nTeste de Igualdade entre P1 e P2: ")
    
    if(P1 == P2):
        print("Pontos iguais")
    else:
        print("Pontos Diferentes")
    
    print(' ')


if __name__ == "__main__":
    main()
    
