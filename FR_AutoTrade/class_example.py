name = '장환승'
age = 24
major = 'cs'

def print_hakjuk(name, age, major):
    print("이름은 %s" % name)
    print("나이는 %i" % age)
    print("전공은",major)

print_hakjuk(name, age, major)

#무언가 귀찮다.

class hakjuk():
    def basic_info(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

hwanseung = hakjuk()
hwanseung.basic_info('환승',27,'cs')
#파이썬 클래스 생성과 클래스 인스턴스 생성

hwanseung.name
hwanseung.age
hwanseung.major

#메소드 내에서 self는 무슨 역할을 할까? 변수는 어떻게 생성될까?

#학적 내용을 프린트 하는 함수를 클래스 안에 넣어보자


class FR_BASIC():
    def __init__(self):
        print("FR")

hororo = FR_BASIC()
#생성자란 무엇인가


#self를 이해해보자

class foo:
    def fun1():
        print("function 1")

    def fun2(self):
        print("function 2")
f = foo()
f.fun2()
f.fun1()
#둘의 차이점은? 파이썬 클래스 내 함수는 첫번째 인자로 항상 인스턴스를 받는다.

f.fun1()
foo.fun1()
#둘의 차이점은?

foo.fun2(self)
foo.fun2()
#둘의 차이점은?

#(클래스 인스턴스).메서드 또는 클래스.메서드(클래스 인스턴스 변수 or 그걸 의미하는 self)


class account():
    account_num = 1000000
n1 = account()
n2 = account()
n1.account_num = 8000
n1.account_num
n2.account_num
#두 개가 무엇이 다른가, fuction 설명할 때와 마찬가지로 독립된 개체라는 느낌

class FR_num():
    FR_number = 0
    def __init__(self, name):
        self.name = name
        self.FR_num+=1

class FR_num():
    FR_number = 0
    def __init__(self, name):
        self.name = name
        FR_num.FR_number+=1

#두 코드의 차이점은?
class naming_problem():
    name = '피카츄'
    def __init__(self, name):
        self.name = name

abc = naming_problem("꼬부기")
abc.name
naming_problem.name
#두 코드의 차이점은? 이해하셨나요? 클래스 변수와 인스턴스 변수의 차이


class Parent:
    def sing(self):
        print("sing a song")

father = Parent()
father.sing()

class child1(Parent):
    pass
shit = child1()
shit.sing()
#상속에 대한 이해

class child2(Parent)
    def dance(self):
        print("유후~")
b = child2()
b.dance()
shit.dance()
#춤을 출 수 있나요?

#상속은 왜 쓸까? 코드의 간편화

#마지막 상속 정리 및 자동매매 구현시 자주 나오는 예제 이해

class window():
    def __init__(self):
        print("메인 윈도우 생성!")

class message_box(window):
    def __init__(self):
        print("메시지 박스 생성!")

example1 = message_box()

class title(window):
    def __init__(self):
        super().__init__()
        print("메시지 박스 생성!")
example2 = title()

#super()의 역할과 생성자 이해하셨나요?
#시간이 된다면 __name__ 뭔지 직접 보여주면 좋을 듯
