def add(a,b):
	return a + b

x = int(input("X: "))
y = int(input("Y: "))
f = open(input("file: "),"a")
for i in range(x,y):
	print("#" + str(add(i,x)),file=f)
