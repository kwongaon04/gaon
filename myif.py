def print_dog():
    dog = [
          " _",
         "<(o )",
         " (  >)"
    ]
    
    for line in dog:
        print(line)

print("그림 출력 프로그램")
print("=====================")
print("1. 개")
print("0. 종료")
print("=====================")

# 무한 반복
while True:
    n = int(input("선택: "))  # 사용자 입력 받기

    # 0을 입력하면 종료
    if n == 0:
        print("프로그램을 종료합니다.")
        break  # 루프 종료

    # 1을 입력하면 강아지 출력
    elif n == 1:
        print("강아지")
        print_duck()
  
    # 잘못된 입력 처리
    else:
        print("잘못입력")
    
    print()  # 각 출력 후 공백 한 줄 추가
