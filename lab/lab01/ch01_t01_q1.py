def main():
    num = int(input("Type an integer: "))
    if num % 10 == 0 and num % 3 != 0:
        print(f'{num} is divisible by 10 and not divisible by 3.')
    else:
        print(f'{num} is not divisible by 10 or divisible by 3.')

if __name__ == "__main__":
    main()