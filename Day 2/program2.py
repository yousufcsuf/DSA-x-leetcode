def printNum(num):
    count=0
    while num > 0:
        count += 1
        num=int(num/10)
        print(num)

    print("count: "+str(count))

def main():
    num = int(input("Please enter a number"))
    printNum(num)


if __name__ == "__main__":
    main()

        
