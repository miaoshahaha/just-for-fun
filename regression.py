import matplotlib.pyplot as plt

x = []      # x variable
y = []      # y variable

def InputTheNum():
    global x
    global y
    x = []
    y = []

    EnterTheValue = True
    while EnterTheValue == True:
        resx = input("Input x value. \'e\' to exit. : ")
        if resx != 'e':
            resx =float(resx)
            x += [resx]
            print(x)
        else:
            EnterTheValue = False
            break
        resy = input("Input y value. : ")
        resy = float(resy)
        y += [resy]
        print(y)

InputTheNum()

print (x)
print (y)

numxx = sum(float(i*i) for i in x )  # x*x
numyy = sum(float(i*i) for i in y )  # y*y
numxy = sum(x[i]*y[i] for i in range(len(x)))
xxbar = numxx / len(x)
yybar = numyy / len(y)
numx = sum(float(i) for i in x )
numy = sum(float(i) for i in y )
ybar = numy / len(y)
xbar = numx / len(x)
b = (len(x) * numxy - numx * numy) / (len(x) * numxx - numx * numx)
a = ybar - b * xbar

print(b)
print(a)
print("y = %sx +%s" %(b,a))

plt.scatter(x,y, label ='test', s = 50 )
plt.xlabel('num of Service Reports')
plt.ylabel('cost')
plt.title('Cost & Management \nAccounting')
#plt.legend()
plt.show()


