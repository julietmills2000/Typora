def show_magicians(printed_names):
	for printed_names in printed_names:
		print(str(printed_names).title())

def make_great(changed_lists):
	for i in range(4):
		changed_lists[i]='the Great '+changed_lists[i]
	return changed_lists

magicians=['job','jane','stand','smile']
make_great(magicians[:])
show_magicians(magicians)

make_great(magicians)
show_magicians(magicians)


