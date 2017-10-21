from modules.ponto import Point

def main(args=[]):
    P1 = Point(2,5)
    P2 = Point(3,4)
    PS = P1 + P2

    print("Ponto Soma definido:")

    print(P1)
    
    print('        +')
    
    print(P2)
    
    print('        =')

    print(PS)

if __name__ == "__main__":
    main()
    
