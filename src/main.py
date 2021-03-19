import datetime


def main():
    print("sweet-sauce.io")
    print("")
    val = input("enter your secret sauce: ")
    print("your sauce is: " + val)
    print("")
    dt = datetime.datetime.now()
    print("your sauce captured at: " + str(dt))

if __name__ == "__main__":
    main()