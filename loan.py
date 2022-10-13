import os
import sys
from time import sleep

def main():
	print("")
	a=float(input("\33[93m[\33[91m+\33[93m]\33[95m ENTER THE PRICE OF GOODS :\33[92m "))
	b=float(input("\33[93m[\33[91m+\33[93m]\33[95m ENTER THE DOWN PAYMENT :\33[92m  "))
	ab=a-b
	print ("\33[93m[\33[91m+\33[93m]\33[95m REMAINING BLANCE IS :\33[93m ",ab)
	print ("")
	c=float(input("\33[93m[\33[91m+\33[93m]\33[95m ENTER THE NUMBER OF MONTHLY INSTALLMENT :\33[92m "))
	s=float(input("\33[93m[\33[91m+\33[93m]\33[95m ENTER THE ANUAL INTEREST RATE : \33[92m "))
	cr=ab/c
	print("\33[93m[\33[91m+\33[93m]\33[95m MONTHLY LOAN PART IS : \33[93m",cr)
	print ("")
	l=cr*s/100*1/12
	print("\33[93m[\33[91m+\33[93m]\33[95m THE INTEREST RATE OF MONTHLY LOAN PART IS :\33[93m ",l)
	print ("")
	e=c/2
	r=c+1
	d=e*r
	print("\33[93m[\33[91m+\33[93m]\33[95m NUMBER OF MONTHLY UNITS IS : \33[93m ",d)
	print ("")
	x=l*d
	print ("\33[93m[\33[91m+\33[93m]\33[95m FULL OF INTEREST RATE IS :\33[93m ",x)
	w=ab+x
	print ("\33[93m[\33[91m+\33[93m]\33[95m FULL OF PAYMENT IS : \33[93m ",w)
	print ("")
	z=w/c
	print ("\33[93m[\33[91m+\33[93m]\33[95m MONTHLY INSTALMENT IS : \33[92m ",z)
	print ("")













b="""\33[91m  /$$                                     /$$       /$$                                     
| $$                                    | $$      | $$                                     
| $$        /$$$$$$   /$$$$$$  /$$$$$$$ | $$$$$$$ | $$  /$$$$$$                            
| $$       /$$__  $$ |____  $$| $$__  $$| $$__  $$| $$ /$$__  $$                           
| $$      | $$  \ $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$| $$$$$$$$                           
| $$      | $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$| $$_____/                           
| $$$$$$$$|  $$$$$$/|  $$$$$$$| $$  | $$| $$$$$$$/| $$|  $$$$$$$                           
|________/ \______/  \_______/|__/  |__/|_______/ |__/ \_______/                           
           
\33[93m          /$$$$$$                                 /$$     /$$                    
                   /$$__  $$                               | $$    |__/                    
                  | $$  \__//$$   /$$ /$$$$$$$   /$$$$$$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
                  | $$$$   | $$  | $$| $$__  $$ /$$_____/|_  $$_/  | $$ /$$__  $$| $$__  $$
                  | $$_/   | $$  | $$| $$  \ $$| $$        | $$    | $$| $$  \ $$| $$  \ $$
                  | $$     | $$  | $$| $$  | $$| $$        | $$ /$$| $$| $$  | $$| $$  | $$
                  | $$     |  $$$$$$/| $$  | $$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
                  |__/      \______/ |__/  |__/ \_______/   \___/  |__/ \______/ |__/  |__/
                                                                                           
                                                                                           
                                                                                           """
def bn():
 os.system('clear')
 for x in b :
	 print(x, end="")
	 sys.stdout.flush()
	 sleep(0.0003)
bn()
main()
