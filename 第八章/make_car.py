def make_car(manu,typ,**car_infos):
	car={}
	car['manufactor']=manu
	car['car_type']=typ
	for key,value in car_infos.items():
		car[key]=value
	return car
car_profile=make_car('subaru','outlook',color='blue',tow_package=True)
print(car_profile)