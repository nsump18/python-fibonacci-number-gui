'''
Nathanael sumpter

SDEV220

4/24/2018
'''
def sumDigits(n):
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    return tot
def main():
    n = int(input("Enter an integer: "))
    print('The sum of the digits is '+str(sumDigits(n)))
main()
