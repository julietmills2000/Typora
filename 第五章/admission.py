current_users=['juliet','celien','jack',"mike",'sasha']
new_users=['juliet','violet','elizath','william','jack']
current_users_0=[]
for current_user in current_users:
	name=current_user.lower()
	current_users_0.append(name)

for new_user in new_users:
	if new_user.lower() in current_users_0:
		print(f"{new_user}已经存在，请重新输入！")
	else:
		print(f"{new_user}可以正常使用")

	