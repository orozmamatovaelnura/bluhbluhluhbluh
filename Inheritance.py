#1
class Poems:
  def __init__(self,year,autor,modern_rating):
    self.release_year=year
    self.writer=autor
    self.rating=modern_rating

eugene_onegin=Poems(1833,'Alexander Pushkin','73%')
Ozymandias=Poems(1818,'P.Shelley','84%')
The_Rime_of_the_Ancient_Mariner=(1798,'S.Coleridge','85%')
print()

#2
class Human:
  def __init__(self,name,age,favorite_lesson):
    self.name=name
    self.age=age
    self.fav_lesson=favorite_lesson

class Teacher(Human):
  def __init__(self,name,age,favorite_lesson,specialty,salary,):
    super().__init__(name,age,favorite_lesson)
    self.speciality=specialty
    self.salary=salary

class Student(Human):
  def __init__(self,name,age,favorite_lesson,grade):
    super().__init__(name,age,favorite_lesson)
    self.grade=grade
# Свойство favorite_lesson одинаково как для учителя,так и для ученика,его можно вынети в класс Human

Jessie=Human('Jessica Parter',26,'IT science')

Richard=Teacher('Richard Romanovich',38,'Math','math and physics teacher',28000)
Cattie=Student('Catherine Riddle',18,'Bio',11)
print()

#3
class School:
  def wear_uniform(self):
    return("В школе все должны носить форму")
  
class University:
  def wear_uniform(self):
    return("Можно носить любую одежду, если ты студент")

jij=School()
print(jij.wear_uniform())

MIT=University()
print(MIT.wear_uniform())

print()
#4

class Human:
  def eat_spaghetti(self):
    print("Я могу есть спагетти")

class Robot:
  def drink_oil(self):
    print("Я могу  потреблять машинное масло")

class Cyborg(Human,Robot):
  pass

Titan1010=Cyborg()
Titan1010.eat_spaghetti()
Titan1010.drink_oil()
