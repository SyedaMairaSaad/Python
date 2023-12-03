
hrs = input("Enter Hours:")
rate = input("Enter Rate per Hour:")
try:
    hrs=float(hrs)
    rate=float(rate)
except:
    print('Error: Input is not number')
    quit()

if hrs>40:
    out=40*rate
    outExtra=(hrs-40)*float(rate)*1.5
    out=out+outExtra
else:
     out=float(hrs)*float(rate)
print(out)