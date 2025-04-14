# 숫자 두개를 입력을 받아서
# +, -, *, / 를 출력 하는 프로그램을 만들어 보자
try:
    # 두 숫자 입력받기
    dam = float(input("첫 번째 숫자를 입력하세요: "))
    mi = float(input("두 번째 숫자를 입력하세요: "))
    
    # 계산 결과 출력
    print("\n===== 사칙연산 결과 =====")
    print(f"{dam} + {mi} = {dam + mi}")
    print(f"{dam} - {mi} = {dam - mi}")
    print(f"{dam} * {mi} = {dam * mi}")
    
    # 나눗셈 (0으로 나누는 경우 예외 처리)
    if mi != 0:
        print(f"{dam} / {mi} = {dam / mi}")
    else:
        print(f"{dam} / {mi} = 0으로 나눌 수 없습니다")
        
except ValueError:
    print("유효한 숫자를 입력해주세요.")
