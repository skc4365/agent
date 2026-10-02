# 설계도, 틀, 개념.
class MyClass:
    # 이름, 나이
    name = "홍길동"
    age = 5

print(MyClass)
print(MyClass.age)

# 오브젝트
p1 = MyClass()
print(p1.name)

p2 = MyClass()
p2.name = "test"
print(p2.name)

p3 = MyClass()
print(p3.name)

p4 = MyClass()
print(p4.name)

# ##########
# 오브젝트를 생성할때, 클래스 초기화 사용.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("에밀리", 36)
print(p1.name)
print(p1.age)

# ##########
#  클래스의 메서드(액션)
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 메서드method :클래스 안에서 정의된 함수
    def greet(self):
        print("반가워요~ 내 이름은 " + self.name)

pp1 = Person2("에밀", 33)
# 오브젝트를 통해서 호출함.
pp1.greet()


# ##########
#  클래스
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ---({self.age})"

ppp1 = Person3("장영실", 36)
print(ppp1)


# ##########
# class Student(Person):
#     pass

# st1 = Student("마이크", 22)
# print(st1.name)

# ##########
class MyPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(MyPerson):
    def __init__(self, name, age, school, grade):
        super().__init__(name, age)
        self.school = school
        self.grade = grade

st01 = Student("한석봉", 20, "호서대학교", 4)

# Super 부모의 값을 사용
print(st01.name)
print(st01.age)
# Student 자기의 멤버필드값을
print(st01.school)
print(st01.grade)

# ##########
# 상속 - 문제1
class Shape:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Shape 색상은 {self.color}"

class Squre(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
        
    def __str__(self):
        return f"{super().__str__()}, 가로는 {self.width}, 세로는 {self.height}"

squre1 = Squre("red", 20, 5)
squre2 = Squre("yellow", 30, 10)
print("[Shape을 상속받는 Squre와 Triangle]")
print(squre1, "\n", squre2)

class Triangle(Shape):
    def __init__(self, color, angle: float):
        super().__init__(color)
        self.angle = float(angle)

    def __str__(self):
        return f"{super().__str__()}, Triangle 각도는 {self.angle}"
    
triangle1 = Triangle("purple", 20.5)
triangle2 = Triangle("orange", 5.5)
print(triangle1, "\n", triangle2)


        
# ##########
# 상속 - 문제2
class Food:
    def __init__(self, orign):
        self.orign = orign

    def __str__(self):
        return f"<오늘의 메뉴> 원산지: {self.orign}"

class Rice(Food):
    def __init__(self, orign, grain):
        super().__init__(orign)
        self.grain = grain

    def __str__(self):
        return super().__str__() + " - " + self.grain

rice1 = Rice("천안산", "흰밥")
rice2 = Rice("천안산", "잡곡밥")
print(rice1)
print(rice2)

class Soup(Food):
    def __init__(self, orign, flag):
        super().__init__(orign)
        self.flag = flag

    def __str__(self):
        return super().__str__()  + " - " + self.flag

soup1 = Soup("익산산", "버섯스프")
soup2 = Soup("부산산", "어니언스프")


