##2번째 게임 100에서부터 내려오기
#2-0. 주사위 선택
dice_n = int(input("굴릴 주사위의 면수를 입력하세요 : "))

#2-1.랜덤숫자(goal) 출력
import random
goal = random.randint(1,100)
print("goal : ",goal)

#2-2.라운드 진행
# 총 lound는 5, 한라운드에 25번 주사위 굴리기
import time
time_start = 0; time_end=0; time_dice = 0; temp = 0; dice = 0; dice_sum = 0;
dice = []; result = 0; updown = "";
win = 0

#주사위 굴리기
def dice_roll():
    time_start = time.time()
    temp = input("주사위를 멈출려면 enter키를 누르세요!")
    time_end = time.time()
    time_dice = int((time_end - time_start)*1000)
    #print(time_end - time_start)
    #print(time_dice % dice_n)
    dice = time_dice % dice_n + 1
    return dice

#업다운 결과 출력
def dice_updown(result,goal):
    updown = '';
    if result > goal :
        print("down!!")
    elif result < goal:
        print("up!")
    else:
        print("맞췄습니다!!!")
        updown = "out"
    return updown
            
#def dice_continue():
    

for lound in range(5):
    lound += 1
    print("\t", lound, "번째 라운드입니다. \n")
    for i in range(25):
        print("   %d번째 주사위를 굴립니당" %(i+1))
        dice = dice_roll()
        print("나온 숫자 :  %d " %dice)

        #주사위를 굴리고 합과 100에서의 차
        YN = input("\n나온 숫자를 0으로 바꿀까요? 네(Y) 아니요(N)  : ")
        if YN == 'Y' or YN == 'y':
            dice = 0
        dice_sum += dice
        result = 100 - dice_sum
        print("%dlound 지금의 결과 : %d" %(lound, result) )

        #업다운 결과 출력
        updown = dice_updown(result,goal)
        
        #주사위 계속 굴릴지 말지
        if updown != 'out':
            if i < 19:
                YN = input("\n주사위 굴리기를 계속 진행할까요? 네(Y) 아니요(N)  : ")
                print( )
            else:
                print("\n주사위를 전부 돌렸습니다..")
                YN = 'N'
        else:
            YN = 'N'
        
        #2-3.라운드 종료
        if YN =='N' or YN == 'n':
            dice_sum = 0
            result = 100
            break
        elif YN == 'Y' or YN == 'y':
            continue
    if updown =='out':
        break
