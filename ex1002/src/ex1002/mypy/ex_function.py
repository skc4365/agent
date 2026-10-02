# ##########
# 값을 실행한 결과를 전달: return
def my_function(num1):
    result = num1 + 100
    return result

sum = my_function(77)
print(sum)

# ##########
# 매개변수의 파라메터 갯수를  똑같이 맞춰주자~!
def my_function2(fname, lname):
    print(fname + " " + lname)

my_function2("길동", "홍")

# my_function2("세종대왕")
# 오류메세지
# TypeError: my_function2() missing 1 required positional argument: 'lname'

# ##########
# 기본 파라메터를 사용
def my_function3(country = "천안"):
    # 공통 출력 기능
    print("나의 고향은 ", country)

my_function3("서울")
my_function3("익산")
my_function3()


# ##########
# 파라메터를 지정해서 값을 넘겨움.
def my_function4(animal, name):
    print("나의 애완동물 ", animal)
    print("나의 이름은 ", name)

my_function4(animal="dog", name="버디")
# 순서 상관없음
my_function4(name="깻잎이", animal="고양이" )