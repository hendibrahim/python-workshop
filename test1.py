def computepay (h, r) :
    if h <= 40 :
        p = r*h
    else :
        p = r*40 + (r*1.5 * (h-40))
        return p
try:
    inp = raw_input("enter hours: ")
    hours = float(inp)
    inp = raw_input("enter rate: ")
    rate = float(inp)
except:
    print "Error, please enter a numeric input"
    quit()

pay = computepay(hours, rate)
print pay


