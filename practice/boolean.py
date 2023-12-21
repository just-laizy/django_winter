# # Bool2
# a = int(input("Give the number : "))
# print((a%2)==1)

# # bool3
# a = int(input("Give the number : "))
# print((a%2)==0)

# # bool4 
# a = int(input("Give the number : "))
# b = int(input("Give the number : "))
# print(a >2 and b<=3)

# bool5
# a = int(input("Give the number a: "))
# b = int(input("Give the number b: "))
# print(a>=0 and b < -2)

# bool16
# a = int(input("Give num : "))
# print(a>9 and a<100 and a%2==0)

# bool17 
# a = int(input("Give num : "))
# print(a>99 and a<1000 and a%2==1)

# bool18
# a = int(input("Give num : "))
# b = int(input("Give num : "))
# c = int(input("Give num : "))
# a = a**2
# b = b**2
# c = c**2
# print(a == b or c == a or c == b)

# bool20
# a = int(input("Give num : "))
# b = a//100
# c = (a//10)%10
# d = a%10

# print(b != c and c != d and d != b)

#bool34

# x = int(input("x coordinate"))
# y = int(input("y coordinate"))


# c = (y%2==0 and x%2 == 1 and x<9 and y<9) or (y%2==1 and x%2 == 0 and x<9 and y<9) 
# print(c)

# bool35


# x = int(input("x coordinate "))
# y = int(input("y coordinate "))
# x1 = int(input("x1 coordinate "))
# y1 = int(input("y1 coordinate "))

# c = (y%2==0 and x%2 == 1 and x<9 and y<9) or (y%2==1 and x%2 == 0 and x<9 and y<9) 
# c1 = (y1%2==0 and x1%2 == 1 and x1<9 and y1<9) or (y1%2==1 and x1%2 == 0 and x1<9 and y1<9) 

# ans = c == c1
# print(ans)

# bool36


# x = int(input("x coordinate "))
# y = int(input("y coordinate "))
# x2 = int(input("x2 coordinate "))
# y2 = int(input("y2 coordinate "))

# ans = (x == x2 ) or (y == y2) 

# print(ans)

# bool37

# x = int(input("x coordinate "))
# y = int(input("y coordinate "))
# x1 = int(input("x1 coordinate "))
# y1 = int(input("y1 coordinate "))

# ans = (x1==x+1)and (y1 == y+1) or (x1 == x+1 and y1 == y+1)

# print(ans)

# bool38

x = int(input("x coordinate "))
y = int(input("y coordinate "))
x1 = int(input("x1 coordinate "))
y1 = int(input("y1 coordinate "))

h = abs(x1-x)
v = abs (y-y1)

ans = h==v
print(ans)
