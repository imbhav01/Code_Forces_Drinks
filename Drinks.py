x = int(input())
z = str(input()).split()
s = 0
for i in range(0,x):
    s = s+int(z[i])
    
y = (s/(100*x))*100

print("{:.12f}".format(y))   


