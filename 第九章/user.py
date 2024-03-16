class User:

	def __init__(self,first_name,last_name,age):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.login_attempts=0


	def describe_user(self):
		print("First name is :"+self.first_name.title()+'.')
		print("Last name is :"+self.last_name.title()+'.')
		print("Age is :"+str(self.age)+'.')
		print("已经尝试登录："+str(self.login_attempts)+'.')

	def greet_user(self):
		print(self.first_name+' '+self.last_name+',hello!')

	def increment_login_attempts(self):
		self.login_attempts+=1

	def reset_login_attempts(self):
		self.login_attempts=0



