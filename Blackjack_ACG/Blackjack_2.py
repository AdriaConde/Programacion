#Blackjack fase 2
import random
o_carta="s"
n_p="s"
apuestas=0
apuestas_ac=0
apuestas_rest=1000

print("Partes con 1000€\n")
while n_p=="s":
    apuestas_ac=0
    blackjack=0
    apuestas_rest = apuestas_rest + apuestas
    carta=random.randint(1,13)
    if carta==1:
        print("\nAs")
        op=int(input("¿Cuánto quieres que valga el As, 1 o 11? "))
        if op==1:
            blackjack +=1
        if op==11:
            blackjack +=11
    if carta in [2,3,4,5,6,7,8,9,10]:
        print("\n{carta}")
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
    apuestas=float(input("¿Cuánto quieres apostar? "))
    apuestas_ac=apuestas_ac+apuestas
    apuestas_rest=apuestas_rest-apuestas
    print(apuestas_rest,"€ restantes")
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
        apuestas=float(input("¿Cuánto quieres apostar? "))
        apuestas_ac=apuestas_ac+apuestas
        apuestas_rest=apuestas_rest-apuestas
        print(apuestas_rest,"€ restantes")
        if blackjack==21 or blackjack >21:
            o_carta="n"
        else:
            o_carta=input(f"Total: {blackjack} \nDinero restante: {apuestas_rest} \n¿Quieres otra carta? (s/n): ")
        
    if blackjack==21:
        print(f"\nEnhorabuena, ¡has ganado la partida! Dinero obtenido: {apuestas_rest+apuestas_ac*2}")
    if blackjack in [16,17,18,19,20]:
        print(f"\nHas sido un poco conservador. Dinero obtenido: {apuestas_rest+apuestas_ac*0.5}")
    if blackjack<15:
        print(f"\nQuizás tendrías que arriesgar un poco, ¿no? Dinero obtenido: {apuestas_rest}")
    if blackjack >21:
        print(f"\n¡Has perdido la partida! Dinero obtenido: {apuestas_rest-apuestas_ac}")
    n_p=input("¿Quieres hacer otra partida? (s/n): )
    if apuestas_rest==0:
        n_p="n"

print("No más partidas.")
if apuestas_rest==0:
    print("No más partidas. No tienes dinero")