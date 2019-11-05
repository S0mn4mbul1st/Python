x , y = 10, 15
print(x ,y )

x , y = y , x
print ( x,y )

z = x + y
print("X = ", x, "\nY = ", y, "\nSum = ", z)


str = "Aykhan Imanov"
print("Reverse of string : " , str[::-1])


str2 = ["I" , "go" , "to" , "school" ]
print( " ".join(str2) )


n = -1
boolean = 1 < n < 10
print(boolean)

boolean = -5 < n < 10
print(boolean)



class MyEnum:
    Aykhan,Geeks, For, Geeks = range(4)


print(MyEnum.Geeks)
print(MyEnum.For)
print(MyEnum.Aykhan)
print(MyEnum.Geeks)


def func():
    return 1,2,3,4

a,b,c,d = func()

print (a,b,c,d)




test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print("\nThe List:", test)
print("Most Frequent Value In A List : ",max(set(test), key = test.count))


import sys
val = "Hello World"
print(sys.getsizeof(val))


str3 = "Hello World\n"
print ( 3 * str3)



matrix = [ [1,2,3] , [4,5,6] ]

print(matrix)