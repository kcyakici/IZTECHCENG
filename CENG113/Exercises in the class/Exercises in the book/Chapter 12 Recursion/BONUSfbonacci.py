def fibonacci(step):

    if step == 1:
        return 1
    elif step == 2:
        return 1
    else:
        return fibonacci(step-2) + fibonacci(step-1)
        
# 1 1 2 3 5 8 13 21 34 55 89
def main():
    step = int(input("Give number: "))
    print(fibonacci(step))

if __name__ == "__main__":
    main()