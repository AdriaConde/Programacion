#Blackjack
import random
o_carta="s"
n_p="s"
diferencia=0
stop=0
lista_as=[1,11]
bo=0

nombre=input("Introduce un alias: ")

while n_p=="s":
    blackjack=0
    carta=random.randint(1,13)
    if carta==1:
        print("\nAs")
        op=int(input("¿Cuánto quieres que valga el As, 1 o 11? "))
        if op==1:
            blackjack +=1
        if op==11:
            blackjack +=11
    if carta in [2,3,4,5,6,7,8,9,10]:
        print(f"\n{carta}")
        blackjack +=carta
    if carta==11:
        print("\nJ")
        blackjack +=10
    if carta==12:
        print("\nQ")
        blackjack +=10
    if carta==13:
        print("\nK")
        blackjack +=10
    o_carta=input(f"{nombre} tu total es: {blackjack} \n¿Quieres otra carta? (s/n): ")
    
    while o_carta=="s":
        carta=random.randint(1,13)
        if carta==1:
            print("\nAs")
            op=int(input("¿Cuánto quieres que valga el As, 1 o 11? "))
            if op==1:
                blackjack +=1
            if op==11:
                blackjack +=11
        if carta in [2,3,4,5,6,7,8,9,10]:
            print(f"\n{carta}")
            blackjack +=carta
        if carta==11:
            print("\nJ")
            blackjack +=10
        if carta==12:
            print("\nQ")
            blackjack +=10
        if carta==13:
            print("\nK")
            blackjack +=10
        if blackjack==21 or blackjack >21:
            print(f"{nombre} tu total es: {blackjack}")
            o_carta="n"
        else:
            o_carta=input(f"{nombre} tu total es: {blackjack} \n¿Quieres otra carta? (s/n): ")
            
    while o_carta=="n":
        blackjack_ordenador=0
        carta=random.randint(1,13)
        if carta==1:
            print("\nAs")
            print("¿Cuánto quieres que valga el As, 1 o 11? ")
            valor_as=random.choice(lista_as)
            if valor_as==1:
                blackjack_ordenador +=1
            if valor_as==11:
                blackjack_ordenador +=11
        if carta in [2,3,4,5,6,7,8,9,10]:
            print(f"\n{carta}")
            blackjack_ordenador +=carta
        if carta==11:
            print("\nJ")
            blackjack_ordenador +=10
        if carta==12:
            print("\nQ")
            blackjack_ordenador +=10
        if carta==13:
            print("\nK")
            blackjack_ordenador +=10
        print(f"Total ordenador es: {blackjack_ordenador}")
        diferencia=blackjack-blackjack_ordenador
        input()
        
        while blackjack_ordenador<21 and blackjack<21:
            while blackjack_ordenador in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] and diferencia>0:
                carta=random.randint(1,13)
                if carta==1:
                    print("\nAs")
                    print("¿Cuánto quieres que valga el As, 1 o 11? ")
                    valor_as=random.choice(lista_as)
                    if valor_as==1:
                        blackjack_ordenador +=1
                    if valor_as==11:
                        blackjack_ordenador +=11
                if carta in [2,3,4,5,6,7,8,9,10]:
                    print(f"\n{carta}")
                    blackjack_ordenador +=carta
                if carta==11:
                    print("\nJ")
                    blackjack_ordenador +=10
                if carta==12:
                    print("\nQ")
                    blackjack_ordenador +=10
                if carta==13:
                    print("\nK")
                    blackjack_ordenador +=10
                print(f"Total ordenador es: {blackjack_ordenador}")
                diferencia=blackjack-blackjack_ordenador
                input()

        if blackjack>blackjack_ordenador:
            if blackjack<=21:
                print(f"\n{nombre} enhorabuena, ¡has ganado la partida!")
            else:
                print(f"\n{nombre}¡Has perdido la partida!")
        if blackjack==blackjack_ordenador:
            print(f"\n{nombre} has sido un poco conservador")
        if blackjack<blackjack_ordenador:
            print(f"\n{nombre}¡Has perdido la partida!")
        n_p=input(f"\n¿{nombre} quieres hacer otra partida? (s/n): ")
        if n_p=="n":
            print("No más partidas")
            break