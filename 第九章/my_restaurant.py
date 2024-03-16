"""创建一个表示餐馆的类"""
class Restaurant():

	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_serverd=0

	def describe_restaurant(self):
		print("Restaurant's name is :"+self.restaurant_name.title()+".")
		print("Cuisine's type is :"+self.cuisine_type+".")

	def open_restaurant(self):
		print("The restaurant is open!")

	def read_number(self):
		print("This restaurant has "+str(self.number_serverd)+" persons in there!")

	def set_number_served(self,person):
		self.number_serverd=person


	def increment_number_served(self,ps):
		self.number_serverd+=ps
