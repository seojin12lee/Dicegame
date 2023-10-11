##프로그램 강제 종료 : crtl + c

#1-1. 시작화면
#1-2. 게임설명

#2-0. 주사위 선택
dice_n = int(input("굴릴 주사위의 면수를 입력하세요 : "))

#2-1.랜덤숫자(goal) 출력
import random
goal = random.randint(2*dice_n +1, 4*dice_n+2)
print("goal : ",goal)

#2-2.라운드 진행
# 총 lound는 17, 한라운드에 7번 주사위 굴리기
import time
time_start = 0; time_end=0; time_dice = 0; temp=0; dice = 0; dice_sum = 0;
dice = []
win = 0

for lound in range(17):
    lound += 1
    print("\t", lound, "번째 라운드입니다. \n")
    for i in range(7):
        print("   %d번째 주사위를 굴립니당" %(i+1))
        time_start = time.time()
        temp = input("주사위를 멈출려면 enter키를 누르세요!")
        time_end = time.time()
        time_dice = int((time_end - time_start)*1000)
        #print(time_end - time_start)
        #print(time_dice % dice_n)
        
        dice = time_dice % dice_n + 1
        print("나온 숫자 :  %d " %dice)
        YN = input("\n나온 숫자를 0으로 바꿀까요? 네(Y) 아니요(N)  : ")
        if YN == 'Y' or YN == 'y':
            dice = 0
        dice_sum += dice
        print("%d 라운드의 주사위의 합 : %d \n" %(lound, dice_sum))

        if i < 6:
            YN = input("주사위 굴리기를 계속 진행할까요? 네(Y) 아니요(N)  : ")
            print( )
        else:
            print("주사위를 전부 돌렸습니다..")
            YN = 'N'
        
        #2-3.라운드 종료, 업다운 결과 출력
        if YN =='N' or YN == 'n':
            if dice_sum > goal :
                print("down!!")
            elif dice_sum < goal:
                print("up!")
            else:
                print("맞췄습니다!!!")
                temp = 'out'
                win += 1
            dice_sum = 0
            break
        elif YN == 'Y' or YN == 'y':
            continue
    if temp =='out':
        break

#3-1.승패 출력
#3-2.엔딩화면

##2번째 게임 1000에서부터 내려오기
#1-1. 게임설명
#1-2.
