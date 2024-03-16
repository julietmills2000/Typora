sandwich_orders=['tuna','pastrami','honey wheat',
'pastrami','grain','pastrami']
print("Sorry,pastrami has been sold out!")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print(sandwich_orders)