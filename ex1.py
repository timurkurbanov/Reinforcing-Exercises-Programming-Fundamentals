class Person:
  def __init__(self, emotions):
    self.pizza = emotions

  def pasta(self):
    for emotion, level in self.pizza.items():
      if level == 1:
        print(f"You look {emotion}")
      elif level == 2:
        print(f"You look {emotion}")
      elif level == 3:
        print(f"You look {emotion}")
      
emotions = {
  'tired': 1,
  'OK': 2,
  'good': 3
}
person1 = Person(emotions)

person1.pasta()