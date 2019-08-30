bottles = int(input("No. of bottles"))
radius = list(map(int, input("Enter radius here").split()))

min_radius = min(radius)
l = []
for x in radius:
    if(min_radius > x):
        radius.remove(x)

