scores = {"数学": 82, "国語": 74, "英語": 60, "理科": 92, "社会": 70}

science = scores["理科"]
social = scores["社会"]
score_difference = science - social
print(score_difference)

diff = scores["理科"] - scores["社会"]

print(f"{diff}点")

avg_score = sum(scores.values()) / len(scores)
print(f"{avg_score}点")
prefecture = "京都"
prefecture = "大阪"
prefecture = "千葉"

if prefecture == "東京":
  print(f"{prefecture}は日本の首都です")
elif prefecture == "京都":
  print(f"{prefecture}は日本の古都です")
elif prefecture == "大阪":
  print(f"{prefecture}は日本の台所です")
else:
  print(f"{prefecture}は日本です")

number = 7

if number % 2 == 1:
  print(f"{number}は奇数です")
else:
  print(f"{number}は偶数です")

for x in range(1, 10):
  print(x)

numbers = [10, 21, 100, 18, 2]
for n in numbers:
  if n >= 100:
    break
  print(f"{n}:繰り返し")
print(f"for文の終了")

scores = {"数学": 82, "国語": 74, "英語": 60, "理科": 92, "国語": 70}

for k, v in scores.items():
  print(f"{k}は{v}点です")

year = 115
def is_leap_years(year):
  if year % 400 == 0:
    return True
  elif year % 100 ==0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False

year = 2024
result = is_leap_years(year)
print(result)


for i in range(1,101):
  if i % 15 == 0:
    print("FizzBuzz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("Fizz")
  else:
    print(i)
class User:
  def __init__(self, name, mail_address, point):
    self.name = name
    self.mail_address = mail_address
    self.point = point

  def add_point(self, point):
    self.point += point

# user_1 = User("佐藤葵", "sato@example.com", 500)
user_2 = User("小林ゆい", "kobayashi@example.com", 1000)
user_2.point = 0
print(user_2.point)
# user_1.add_point(-100)
# print(user_1.point)
class Student:
  def __init__(self, name, math, japanese, 
              english, science, society):
      self.name = name
      self.math = math
      self.japanese = japanese
      self.english = english
      self.science = science
      self.society = society
  
  def avg_score(self):
      avg = (self.math + self.japanese + self.english
             + self.science + self.society) / 5
      return avg

student_1 = Student("斉藤そうま", 82, 74, 60, 92, 72)
s1_avg = student_1.avg_score()
# print(s1_avg)

class Product:
  def __init__(self, id, name, price, purchase_price):
    self.id = id
    self.name = name
    self.price = price
    self.purchase_price = purchase_price

  def purchase_late(self):
    late = self.purchase_price / self.price
    return late

product_1 = Product("A0001", "半袖クールTシャツ", 5000, 2250)
p1_late = product_1.purchase_late()
print(p1_late)

product_1.price = 6000
p1_late = product_1.purchase_late()
print(p1_late)

from my_packeges.my_module import Student

student_1 = Student("斉藤そうま", 82, 74, 60, 92, 72)
s1_avg = student_1.avg_score()
print(s1_avg)

from datetime import datetime
t = datetime.today()
print(t)
