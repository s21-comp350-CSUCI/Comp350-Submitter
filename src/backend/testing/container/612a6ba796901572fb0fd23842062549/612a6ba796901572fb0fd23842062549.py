import sys
#is the string used in the MD5 hash ArthurHTestSimpleCalculationAndPrint
#program just adds two numbers

def main():
  sum = 0
  for i in range(1, len(sys.argv)):
    sum+= int(sys.argv[i])
  print(sum)

main()

#test2.in and test2.out are the test files for this.