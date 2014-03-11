#my own quine in my own style without really knowing python
def main():
    x = "x = def main():  print x[4:15] + chr(10) + chr(32) + chr(32) + chr(32) + x[:4] + chr(34) + x + chr(34) + chr(10) + chr(32) + x[15:]"
    print x[4:15] + chr(10) + chr(32) + chr(32) + chr(32) + x[:4] + chr(34) + x + chr(34) + chr(10) + chr(32) + x[15:]

main()
#could be improved and will be improved. 
#pondering if I should write one in sml or java. 
