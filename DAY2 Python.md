# 📚 CS50W DAY 2 - Python 学习笔记

## 📌 学习内容总结

### python
因为之前有过算法基础，所以简单的语法都直接过了，主要学习和复习其中的面向对象，修饰器，异常处理

# 1.面向对象
创造一个新类型，以某种方式表示其它类型的数据，创建一个对象类

classes.py

```py
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)
```
result:

2
8

创建一个叫做init的函数，它通过将两个输入储存在对象内部，储存在一个名为x和一个名为y的属性中来创建一个点，然后p是一个调用这个函数的点，就可以得到p.x & p.y

```py
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No avaliable seats for {person}.")
```
现在有一个人员名单，对于这些人的每个人，尝试把他们添加到航班上，调用函数flight.add_passenger，如果成功返回True保存在success变量中，打印成功添加。反之False，打印没有可用座位。


# 装饰器 decorators
装饰器是python中获取一个函数，并修改该函数，为该函数添加一些额外行为的方式

decorators.py
```py
def announce(f):
    def wrapper():
        print("About to run the function.")
        f()
        print("Done with the function.")
    return wrapper

@announce
def (hello):
    print("Hello world!")

hello() 
```
result:

About to run the function.
Hello world!
Done with the function.

hello函数被包裹在announce装饰器中，announce装饰器的作用是获取hello函数作为输出，然后得到一个新函数，首先打印警告"About to run the function."，然后运行hello()，再打印警告"Done with the function."

以后可能在用于检测用户登录

# 3.lambda
lambda.py
```py
people = [
    {"name": "Harry", "house", "Gryffindor"}
    {"name": "Cho", "house", "Ravenclaw"}
    {"name": "Draco", "house", "Slytherin"}
]

people.sort(key = lambda person: person["name"])

print(people)
```

# 4.异常处理
exceptions.py
```py
try:
    x = int(input())
    y = int(input())
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)
```
异常处理通常是一个很有用的工具，在你预计你的程序可能会出现一些异常的情况下，你可以提前对结果进行应对，优雅地处理这些错误，给用户显示一个友好的错误信息便于理解出现了什么问题，也可以及时退出程序避免程序完全崩溃