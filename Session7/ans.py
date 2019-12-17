class human:
  name=None
  def __init__(self):
    print("i am new born!!")
  def sayHello(self):
    print(f"hello ma friend :)\nMy name is {self.name} I am very polit \U0001F60C\n")

person0=human()
person0.name="kasra"
person0.sayHello()
person1=human()
person1.sayHello()
person0.sayHello()
