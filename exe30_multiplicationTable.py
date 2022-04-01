#Creating a multiplication table
#program is surprisingly simple, it is using the print, " " and looping to get the pattern


"""
for x in range(13):
    for y in range(13):
        print(f" {x} X {y} = {x * y}")

"""
print(" ",end=' ')
for x in range(13):
    print(f" {x} ",end=' ')
print("\n")

for x in range(13):
    print(f"{x}",end=' ')
    for y in range(13):
        print(f" {x * y} ",end=" ")
    print("\n")        
