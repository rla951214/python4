class Person:
  # initialize(초기화)를 줄임말 init 
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def say_hello(self, to_name):
    print("안녕! " + to_name + " 나는 " + self.name)

  def introduce(self):
    print("내 이름은" + self.name + "그리고 나는" + str(self.age) + " 살이야 ")

jungtae = Person(" 정태 ", 27)
jungtae.introduce()


# 상속에 대한 예 
class Police(Person):
  def arrset(self, to_arrset):
    print("넌 체포됬다, " + to_arrset)

class Programmer(Person):
  def program(self, to_program):
    print("파이썬 너무 재밌다~ 다음엔 어떤 공부를 해볼까 ? : " + to_program)

jungtae = Person(" 정태 ", 27)
sangho = Police(" 상호 ", 27)
kyoungmin = Programmer(" 경민 ", 21)

sangho.introduce()
sangho.arrset("정태")
kyoungmin.program("파이썬의 패키지, 모듈에 대해서 공부해보자 !! ")
print(" 파이썬 : " + "그럼 다음 공부를 하러 가볼까 정태 ? ")
print(" 정태 : " + "좋아 지금 바로가자 !! ")

