def make_album(singer_name,album_name,sum_song=''):
	"""返回一个包含这两项信息的字典"""
	album={'singer':singer_name,'al':album_name}
	if sum_song:
		album['sum']=sum_song	
	return album
while True:
	print("\nPlease tell me about the album.")
	print("(enter'q'to quit)")
	singer_name=input("Singer: ")
	if singer_name=='q':
		break
	album_name=input("Album：")
	if album_name=='q':
		break
	album=make_album(singer_name,album_name)
	print(album)
