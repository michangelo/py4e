def exercise_4_6():
    def computepay(h, r):
        # base conditional for overtime pay 
        if h > 40:
            return 40*r + (h-40)*1.5*r
        else:
            return h*r
        
    # input hours and rate     
    h = input("Enter Hours:")
    r = input("Enter rate per hour:")

    # ensure input is of type float 
    try: 
        h = float(h)
        r = float(r)
    except:
        print("Error. Use a float!")
        exit()
    
    # logic into function and print 
    p = computepay(h,r)
    return ("Pay", p)

exercise_4_6()

