a = 0 
b = 100 
c = 0 
avg = 0
mark = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range (1 , 20) :
    mark[i] = int(input("Enter the marks : "))
    if mark[i] > a :
        a = mark[i]

    if mark[i] < b :
        b = mark[i]

    if mark[i] <= 40 :
        c = c + 1

print ("The highest marks is ", a)
print ("The lowest mark is : ", b)
print ("The number of fail students are : ", c)

