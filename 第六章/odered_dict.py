from collections import OrderedDict

python_lists=OrderedDict()
python_lists['append']='将元素添加到列表末尾'
python_lists['insert']='可在列表的任何位置添加新元素'
python_lists['pop']='删除列表末尾的元素'

for word,mean in python_lists.items():
	print(word+":"+mean)