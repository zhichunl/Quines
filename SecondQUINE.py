# my quine: not as elegant
def main():
    x = "x = def main():  print x[4:15] + chr(10) + chr(32) + chr(32) + chr(32) + x[:4] + chr(34) + x + chr(34) + chr(10) + chr(32) + x[15:]"
    print x[4:15] + chr(10) + chr(32) + chr(32) + chr(32) + x[:4] + chr(34) + x + chr(34) + chr(10) + chr(32) + x[15:]

main()

