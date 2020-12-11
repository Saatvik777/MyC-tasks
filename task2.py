list = []
num = int(input("no. of elements"))
for n in range(0,num):
  elements = int(input())
  list.append(elements)

for i in list:
    if i >0:
        print(i,end = " ")
