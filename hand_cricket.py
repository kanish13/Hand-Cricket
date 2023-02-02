def p1_batting():
    global p1_score
    while True:
        p1_run=int(input("Choose the number from 0 to 10 to hit the score:"))
        if p1_run>-1 and p1_run<11:
            cpu_bowl=random.choice([0,1,2,3,4,5,6,7,8,9,10])
            print(p1_run,"VS",cpu_bowl)
            if p1_run==cpu_bowl:
                print("OUT!!!")
                break
            else:
                p1_score=p1_score+p1_run+cpu_bowl
                print("CURRENT SCORE OF P1:",p1_score)
    print("TOTTAL SCORE OF P1:",p1_score)
def p1_second_batting(a):
    global p1_score
    while True:
        p1_run=int(input("Choose the number from 0 to 10 to hit the score:"))
        if p1_run>-1 and p1_run<11:
            cpu_bowl=random.choice([0,1,2,3,4,5,6,7,8,9,10])
            print(p1_run,"VS",cpu_bowl)
            if p1_run==cpu_bowl:
                print("OUT!!!")
                break
            else:
                p1_score=p1_score+p1_run+cpu_bowl
                print("CURRENT SCORE OF P1:",p1_score)
            if p1_score>cpu_score and a==2:
                print("P1 WON !!!!")
                break
    print("TOTTAL SCORE OF P1:",p1_score)
def cpu_batting():
    global cpu_score
    while True:
        cpu_run=random.choice([0,1,2,3,4,5,6,7,8,9,10])
        
        p1_bowl=int(input("Choose the number from 0 to 10 to wicket the opponent:"))
        if p1_bowl>-1 and p1_bowl<11:
            print(cpu_run,"VS",p1_bowl)
            if cpu_run==p1_bowl:
                print("OUT!!!")
                break
            else:
                cpu_score=cpu_score+cpu_run+p1_bowl
                print("CURRENT SCORE OF CPU",cpu_score)
    print("TOTAL SCORE OF CPU:",cpu_score)
def cpu_second_batting(x):
    global cpu_score
    while True:
        cpu_run=random.choice([0,1,2,3,4,5,6,7,8,9,10])
        
        p1_bowl=int(input("Choose the number from 0 to 10 to wicket the opponent:"))
        if p1_bowl>-1 and p1_bowl<11:
            print(cpu_run,"VS",p1_bowl)
            if cpu_run==p1_bowl:
                print("OUT!!!")
                break
            else:
                cpu_score=cpu_score+cpu_run+p1_bowl
                print("CURRENT SCORE OF CPU",cpu_score)
            if cpu_score>p1_score and x==2:
                print("CPU WON !!!!")
                break
    print("TOTAL SCORE OF CPU:",cpu_score)

import random
coin=["head","tail"]
play=["batting","bowling"]
call=int(input("Enter who wanna call the toss 1.p1 2.cpu:"))
if call==1:
    p1_toss=input("p1 choose: head or tail:")
    rand_toss=random.choice(coin)
    if p1_toss==rand_toss:
        print("YOU WON THE TOSS")
        p1_choice=int(input("1.BAT 2.BOWLING:"))
        if p1_choice==1:
            print("YOU CHOOSED BATTING")
            p1_score=0
            cpu_score=0
            p1_batting()
            a=2
            cpu_second_batting(a)
            print("PLAYER 1 SCORE:",p1_score)
            print("CPU SCORE:",cpu_score)
            if p1_score>cpu_score:
                print("PLAYER 1 WON !!!!")
            elif p1_score==cpu_score:
                print("DRAW")
        else:
            print("YOU CHOOSED BOWLING")
            p1_score=0
            cpu_score=0
            cpu_batting()
            a=2
            p1_second_batting(a)
            if p1_score<cpu_score:
                print("CPU WON !!!!")
            elif p1_score==cpu_score:
                print("DRAW")
    else:
        print("YOU LOST THE TOSS. SO CPU GOT TO CHOOSE")
        cpu_choice=random.choice(play)
        if cpu_choice=="batting":
            print("CPU CHOOSED BATTING")
            p1_score=0
            cpu_score=0
            cpu_batting()
            a=2
            p1_second_batting(a)
            if p1_score<cpu_score:
                print("CPU WON !!!!")
            elif p1_score==cpu_score:
                print("DRAW")
        else:
            print("CPU CHOOSED BOWLING")
            p1_score=0
            cpu_score=0
            p1_batting()
            a=2
            cpu_second_batting(a)
            print("PLAYER 1 SCORE",p1_score)
            print("CPU SCORE",cpu_score)
            if p1_score>cpu_score:
                print("PLAYER 1 WON !!!!")
            elif p1_score==cpu_score:
                print("DRAW")
else:
    print("CPU'S CALL")
    cpu_toss=random.choice(coin)
    rand_toss=random.choice(coin)
    if cpu_toss==rand_toss:
        print("CPU WON THE TOSS")
        cpu_choice=random.choice(play)
        if cpu_choice=="bating":
            print("CPU CHOOSED BATTING")
            p1_score=0
            cpu_score=0
            cpu_batting()
            a=2
            p1_second_batting(a)
            if p1_score<cpu_score:
                print("CPU WON !!!!")
            elif p1_score==cpu_score:
                print("DRAW")
        else:
            print("CPU CHOOSED BOWLING")
            p1_score=0
            cpu_score=0
            p1_batting()
            a=2
            cpu_second_batting(a)
            print("PLAYER 1 SCORE",p1_score)
            print("CPU SCORE",cpu_score)
            if p1_score>cpu_score:
                print("PLAYER 1 WON !!!!")
            elif p1_score==cpu_score:
                print("DRAW")
    else:
        print("CPU LOST THE TOSS")
        p1_choice=int(input("1.BAT 2.BOWLING:"))
        if p1_choice==1:
            print("P1 CHOOSED BATTING")
            p1_score=0
            cpu_score=0
            p1_batting()
            a=2
            cpu_second_batting(a)
            print("PLAYER 1 SCORE",p1_score)
            print("CPU SCORE",cpu_score)
            if p1_score>cpu_score:
                print("PLAYER 1 WON !!!!")
            elif p1_score==cpu_score:
                print("DRAW")
        else:
            print("P1 CHOOSED BOWLING")
            p1_score=0
            cpu_score=0
            cpu_batting()
            a=2
            p1_second_batting(a)
            if p1_score<cpu_score:
                print("CPU WON !!!!")
            elif p1_score==cpu_score:
                print("DRAW")
        






            