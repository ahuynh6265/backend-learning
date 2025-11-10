#from week4 cs50p 
import sys

#check for errors 
if len(sys.argv) < 2:
  sys.exit("Too few arguments")


#print name tags
for arg in sys.argv[1:-1]:
  print("hello, my name is", arg )



#print("I am", sys.argv[2], "years old")