import os
import sys
from time import sleep

def main():
	print ("")
	print ("")
	print ("")
	a=float(input("\33[93m[\33[91m+\33[93m]\33[95m ENTER THE PRICE OF GOODS \33[93mRs :\33[92m "))
	print ("")
	b=float(input("\33[93m[\33[91m+\33[93m]\33[95m ENTER THE DOWN PAYMENT \33[93mRs :\33[92m  "))
	ab=a-b
	print ("")
	print ("\33[93m[\33[91m+\33[93m]\33[95m REMAINING BLANCE IS :\33[93mRs\33[91m ",ab)
	print ("")
	c=float(input("\33[93m[\33[91m+\33[93m]\33[95m ENTER THE NUMBER OF MONTHLY INSTALLMENT :\33[92m "))
	print ("")
	s=float(input("\33[93m[\33[91m+\33[93m]\33[95m ENTER THE ANUAL INTEREST RATE : \33[92m "))
	cr=ab/c
	print ("")
	print("\33[93m[\33[91m+\33[93m]\33[95m MONTHLY LOAN PART IS : \33[93m",cr)
	print ("")
	l=cr*s/100*1/12
	print("\33[93m[\33[91m+\33[93m]\33[95m THE INTEREST RATE OF MONTHLY LOAN PART IS :\33[93m ",l)
	print ("")
	e=c/2
	r=c+1
	d=e*r
	print("\33[93m[\33[91m+\33[93m]\33[95m NUMBER OF MONTHLY UNITS IS : \33[93m",d)
	print ("")
	x=l*d
	print ("\33[93m[\33[91m+\33[93m]\33[95m FULL OF INTEREST RATE IS :\33[93m ",x)
	w=ab+x
	print ("")
	print ("\33[93m[\33[91m+\33[93m]\33[95m FULL OF PAYMENT IS \33[93m Rs :\33[91m ",w)
	print ("")
	z=w/c
	print ("\33[93m[\33[91m+\33[93m]\33[95m MONTHLY INSTALMENT IS \33[93mRs : \33[96m",z)
	print ("")
	print ("")
def m():
   a=float(input("\33[93m[\33[91m+\33[93m]\33[95m ENTER THE PRICE OF GOODS :\33[92m "))
   for x in a :
     print (x,end="")
     sys.stdout.flush()
     sleep(3)

c="""\33[91m
██╗      █████╗  █████╗ ███╗  ██╗██████╗ ██╗     ███████╗
██║     ██╔══██╗██╔══██╗████╗ ██║██╔══██╗██║     ██╔════╝
██║     ██║  ██║███████║██╔██╗██║██████╦╝██║     █████╗
██║     ██║  ██║██╔══██║██║╚████║██╔══██╗██║     ██╔══╝
███████╗╚█████╔╝██║  ██║██║  ███║██████╦╝███████╗███████╗
╚══════╝ ╚════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═════╝ ╚══════╝╚══════╝
\33[93m
   ███████╗██╗   ██╗███╗  ▇▇╗ █████╗ ████████╗██╗ █████╗ ███╗  ██╗
   ██╔════╝██║   ██║████╗ ██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗ ██║
   █████╗  ██║   ██║██╔██╗██║██║  ╚═╝   ██║   ██║██║  ██║██╔██╗██║
   ██╔══╝  ██║   ██║██║╚████║██║  ██╗   ██║   ██║██║  ██║██║╚████║
   ██║     ╚██████╔╝██║ ╚███║╚█████╔╝   ██║   ██║╚█████╔╝██║  ███║
   ╚═╝      ╚═════╝ ╚═╝  ╚══╝ ╚════╝    ╚═╝   ╚═╝ ╚════╝ ╚═╝  ╚══╝   \33[93m[\33[91m+\33[93m]\33[95  v 2.0     """


def bn():
 os.system('clear')
 for x in c :
         print(x, end="")
         sys.stdout.flush()
         sleep(0.003)
bn()
main()
