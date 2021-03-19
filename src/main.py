import datetime
from encrypt import *





def main():

    print("sweet-sauce.io")
    print("")
    val = input("enter your sweet secret sauce: ")
    print("")

    print("your sauce captured at: " + str(datetime.datetime.now()))
    print("")

    generate_key()

    print("your sauce is a secret now... ")
    print("")
    
    print("keep your key safe...")
    print("")

if __name__ == "__main__":
    main()