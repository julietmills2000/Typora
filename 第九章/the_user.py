from user import User
class Admin(User):
	def __init__(self,first_name,last_name,age):
		super().__init__(first_name,last_name,age)
		self.privileges=['can add post','can delete post','can ban user']

	def show_privileges(self):
		for privilege in self.privileges:
			print(privilege)