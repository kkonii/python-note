#타입 에러1
#len( )에 정수 입력 불가
len(448)

#타입 에러2
#String 타입과 int 타입의 + 결합 불가
num_char = len(input("What is your name?"))
print("Your name has" + num_char + "characters.")

#에러 발생 가능 경우 타입을 먼저 확인
#int
type(num_char)