

bottles = int(input("No. of bottles"))
radius = list(map(int, input("Enter radius here").split()))


#res_list = (max([radius.count(i) for i in radius]))
#print(res_list)

mlist=[]

for x in radius:
    mlist.append(radius.count(x))

print(max(mlist))
