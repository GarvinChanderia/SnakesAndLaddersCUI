import random
p1=0
p2=0
ladders_i=[8,21,43,50,54,62,66,80]
ladders_f=[26,82,77,91,93,96,87,100]
snakes_i=[98,95,92,83,73,69,64,59,55,52,48,46,44]
snakes_f=[28,24,51,19,1,33,36,17,7,11,9,7,22]
while p1<=100 or p2<=100:
    if(p1>=100):
        print("P1 Wins")
        break
    elif(p2>=100):
        print("P2 Wins")
        break
    else:
        if input("\nPlayer 1 Roll?(Press Enter)")=="":                    
            rand=random.randint(1,6)
            p1=p1+rand
            print("\nYou Got A ",rand,"On The Die\n")
            for i in range (8):
                if(p1==ladders_i[i]):
                    p1old=p1
                    p1=ladders_f[i]
                    print("\nYou Found A Ladder At ",p1old)
                elif(p1==snakes_i[i]):
                    p1old=p1
                    p1=snakes_f[i]
                    print("\nA Snake Bit You At ",p1old)
            print("\nCurrent : ",p1,"\n")
            
        else:
            print("Player 1 Surrenders, Player 2 Wins")

        if input("\nPlayer 2 Roll?(Press Enter) :")=="":       
            rand=random.randint(1,6)
            p2=p2+rand
            print("\nYou Got A ",rand,"On The Die\n")
            for i in range (8):
                if(p2==ladders_i[i]):
                    p2old=p2
                    p2=ladders_f[i]
                    print("\nYou Found A Ladder At ",p2old)
                elif(p2==snakes_i[i]):
                    p2old=p2
                    p2=snakes_f[i]
                    print("\nA Snake Bit You At ",p2old)
            print("\nCurrent : ",p2,"\n")
        else:
            print("Player 2 Surrenders, Player 1 Wins")
        