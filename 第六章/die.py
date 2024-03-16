"""包含以各种方式生成随机数的函数"""
from random import randint
"""创建一个骰子的类"""
class Die:
	def __init__(self,sides=6):
		self.sides=sides

	def roll_die(self):
		x=randint(1,self.sides)
		print(x)

six_die=Die()
for number in range(1,11):
	six_die.roll_die()

ten_die=Die(10)
for number in range(1,11):
	ten_die.roll_die()

twenty_die=Die(20)
for number in range(1,11):
	twenty_die.roll_die()
