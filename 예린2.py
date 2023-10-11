import random
import time

# 입력 범위 내에서 목표 수치를 설정하는 함수
def goalChoice(min, max):
    global goal
    goal = random.randint(min, max)
    #print(goal)
    return goal
    
# 2개의 주사위를 굴리고 눈의 합을 계산하는 함수
def roll_two_dice():
    dice1 = random.randint(1, 6)  # 첫 번째 주사위 굴리기
    dice2 = random.randint(1, 6)  # 두 번째 주사위 굴리기
    total = dice1 + dice2  # 두 주사위 눈의 합 계산
    return total

# 사칙연산을 하는 함수
def calculation(sign):
    global resultAll
    
    if(calc == '+') :
        resultAll = resultAll + result
    if(calc == '-') :
        resultAll = resultAll - result
    if(calc == '*') :
        resultAll = resultAll * result
    if(calc == '/') :
        resultAll = resultAll / result
        
    return resultAll

# 결과를 출력하는 함수
def gameEnd():
    if(flag == 0) :
        overTF = "패배"
    if(flag != 0) :
        overTF = "승리"
        
    print("\t\t<최종 결산>")
    print("총 라운드 수 : {}, 목표 수치 : {}, 주사위 눈의 합 : {}\n".format(i+1, goal, resultAll))
    print("\t\t게임 결과 : {}".format(overTF))
    
# -------------------------------------------------------------------
#                              게임 시작
# -------------------------------------------------------------------

# 범위 한도 지정 및 목표 수치 설정
limit1, limit2, limit3 = map(int, input("목표 수치의 범위를 설정하세요.(최소값, 최대값, 라운드 횟수) : ").split())
goalChoice(limit1, limit2) 

# 목표 수치가 들통나지 않도록 화면을 지워야 하는데 방법을 찾지 못하다 . . .

print("\t[ 목표 수치의 최소값 : {}, 최대값 : {}, 최대 라운드 횟수 : {} ]\n".format(limit1, limit2, limit3))

# 눈속임♥

print("잠시만 기다려주세요. 목표 수치를 정하고 있습니다 ", end="")
for i in range(5):
    print(". ", end="")
    time.sleep(1.5)

print("\n\n")
print("목표 수치의 선정이 완료되었습니다. 게임을 시작합니다.\n")    

# 누적용 변수 선언 및 초기화
resultAll = 0
reCount = 0

# 정답 여부 파악용 변수 선언 및 초기화
flag = 0 

    # 본 프로그램 (지정된 라운드만큼 반복)
for i in range(limit3) :

    reCount=reCount+1
    
    print("\n\t==========================================\n\n")
    print("\t\t[ {}번째 라운드입니다. ]\n".format(i+1))
    user = input("주사위를 굴리시겠습니까? (Y/N) : ")
    
    # 사용자 선택으로 게임이 종료되거나, 혹은 모든 횟수가 소모되었을 때 종료
    if (user == 'N' or user == 'n' or reCount == limit3) :
        print("")
        print("게임이 종료되었습니다. 결과를 출력합니다.")
        gameEnd()
        break
    
    if (user == 'Y' or user == 'y') :
        # 주사위를 굴려서 눈의 합을 출력
        result = roll_two_dice()
        print(f"현재 주사위 눈의 합: {result}\n")
    
    # 사칙연산으로 재미를 추구해봤습니다
    # 그러나 이거 은근 어렵더라고요 . . .
    # 누적합 및 사칙연산 계산
    calc = input("어떤 계산을 하시겠습니까? (+, -, *, /) : ")
    print("현재 주사위 눈의 누적값 : {}\n".format(calculation(calc)))
    
    # Up / Down 결과 출력    
    if (goal < resultAll) :
        print("[Down!] 주사위 눈의 합이 목표 수치보다 높습니다.")
    if (goal > resultAll) :
        print("[Up!] 주사위 눈의 합이 목표 수치보다 낮습니다.")
    if (goal == resultAll) :
        print("[Wow!] 축하합니다. 정답을 맞췄습니다!")
        print("결과를 출력한 뒤 게임을 종료합니다.")
        flag = flag + 1
        gameEnd()
        break

