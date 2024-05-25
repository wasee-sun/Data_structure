#* Python basics

#variables
# x1, num, y1, yx
# any name can be variable

1 # integer
2.5 # float
True # boolean
[1, 2, 3, 4] # list
(1, 2, 3, 4) # tuple
{1, 2, 3, 4} # set
x1 = "hello" # string
x2 = "@123"
print(x1 + " " + x2)

y1 = 2
y2 = 7
print(y1 + y2)
print(y1 - y2)
print(y1 * y2)
print(y2 / y1)
print(y2 // y1)
print(y2 % y1)

z1 = True
z2 = False

print(z1 and z2)
print(z1 or z2)
print(not z1)

i = 20
if i == 20:
    print("PERFECT NUMBER")
if i < 10:
    print("Number is short")
elif i > 30:
    print("Number is long")
else:
    print("Number is okay")
    
i = 20
if i % 2 != 0:
    if i < 10:
        print(" 1 Number is short")
    else:
        print(" 1 Number is long")
else:
    if i < 10:
        print(" 2 Number is short")
    else:
        print(" 2 Number is long")
    
    
x1 = ["A", "B", "C", "D", "E"]
#Index -5   -4   -3   -2   -1
# for j in range(0, len(x1)): # range(0, 1, 2, 3, 4)
#    print(x1[j])
# for i in x1:
#     print(i)
    
    
x1 = 20
i = 0
while i <= x1:
    print(i)
    i += 1

    
#Task 
# 1) Create if else task with any condition must be nested (2 and 3 nests)
# 2) for loop using range and string
# 3) while loop using a condition (inside for loop must be if else, print if once then else)
# 4) Inside while loop there will be for loop and if else
 