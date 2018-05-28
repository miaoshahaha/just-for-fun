def HighLow_Method():        #HIGH-LOW-METHOD
    KeepGoing = True

    while KeepGoing:
        y1 = float(input("Input y1 : "))     # y = ax + b
        x1 = float(input("Input x1 : "))
        y2 = float(input("Input y2 : "))
        x2 = float(input("Input x2 : "))

        test = y2 - y1 #computation
        test2 = x2 -x1  #computation

        a = test / test2
        b = y1 - a * x1

        print ("y = %sx + %s" % (a,b))

HighLow_Method()
