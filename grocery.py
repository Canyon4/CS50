import sys
try:

    ls1 = []
    ls2 = []
    while True:
          userInput = input("Input: ")
          ls1.append(userInput)

except EOFError:
     for i in ls1:
          if (i not in ls2 ):
               ls2.append(i)
     print("\n")
     ls2 = sorted(ls2)
     for c in (ls2):
          print(str(ls1.count(c)) + " " + c.upper())
     sys.exit()