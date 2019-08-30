#from collections import Counter

bottles = int(input("No. of bottles"))
radius = list(map(int, input("Enter radius here").split()))


res_list = (max([radius.count(i) for i in radius]))
print(res_list)
