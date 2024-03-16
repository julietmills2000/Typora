sandwich_orders=['tuna','honey wheat','grain']
finished_sandwiches=[]
while sandwich_orders:
	current_made=sandwich_orders.pop()
	print("I made you "+current_made+"sandwich. ")
	finished_sandwiches.append(current_made)
print("\nThe following sandwiches are : ")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())