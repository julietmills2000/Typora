names=['小徐 ','小刘 ','小范 ']
print('不好意思，只能邀请两位嘉宾吃饭啦！')
greeting="您仍在受邀人名单之内 "
names.insert(0,'小李')
names.insert(2,'小黄')
names.append('小施')
l=len(names)
print(l)
poped_names=names.pop(0)
print(poped_names+'很抱歉，不能邀请您来吃饭')
poped_names=names.pop(0)
print(poped_names+'很抱歉，不能邀请您来吃饭')
poped_names=names.pop(0)
print(poped_names+'很抱歉，不能邀请您来吃饭')
poped_names=names.pop(0)
print(poped_names+'很抱歉，不能邀请您来吃饭')
print(greeting+names[0])
print(greeting+names[1])

del names[0]
del names[0]
print(names)