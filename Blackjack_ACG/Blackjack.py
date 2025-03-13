#Blackjack
import random
blackjack=0
o_carta="s"
n_p="s"

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
        print(f"\ncarta")
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
    o_carta=input(f"Total: {blackjack} \n¿Quieres otra carta? (s/n): ")
    
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
            o_carta="n"
        else:
            o_carta=input(f"Total: {blackjack} \n¿Quieres otra carta? (s/n): ")
        
    if blackjack==21:
        print("\nEnhorabuena, ¡has ganado la partida!")
    if blackjack in [16,17,18,19,20]:
        print("\nHas sido un poco conservador")
    if blackjack<15:
        print("\nQuizás tendrías que arriesgar un poco, ¿no?")
    if blackjack >21:
        print("\n¡Has perdido la partida!")
    n_p=input("\n¿Quieres hacer otra partida? (s/n): ")

print("No más partidas.")