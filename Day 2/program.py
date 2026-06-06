def printNum(num):
    print(str(num % 10) + " ")
    if num > 10:
        return printNum(num // 10)  # use // for integer division
    return None


def main():
    num = int(input("Insert a number: "))
    print("You entered:", num)
    printNum(num)

if __name__ == "__main__":
    main()