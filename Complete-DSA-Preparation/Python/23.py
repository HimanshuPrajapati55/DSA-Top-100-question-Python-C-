def count_divisions(n):
    if n <= 2:
        raise ValueError("The number must be greater than 2.")
    
    count = 0
    while n >= 2:
        n /= 2
        count += 1
    return count

def main():
    try:
        num = int(input("Enter a positive integer greater than 2: "))
        if num <= 2:
            raise ValueError("The number must be greater than 2.")
        
        divisions = count_divisions(num)
        print(f"You need to divide the number by 2 '{divisions}' times before it becomes less than 2.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
