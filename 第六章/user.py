favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
staffs=['jen','sarah','edward','phil','juliet']
for staff in staffs:
	if staff in favorite_languages.keys():
		print(staff+',谢谢参与调查！')

	else:
		print(staff+',您还未参与调查，请点击下方链接参与调查')
	

   	  
	    