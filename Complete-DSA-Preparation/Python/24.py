def make_change(charged, given):
    # Define the bills and coins in descending order of value
    bills_and_coins = {
        '50': 50,
        '20': 20,
        '10': 10,
        '5': 5,
        '1': 1,
        '0.25': 0.25,
        '0.10': 0.10,
        '0.05': 0.05,
        '0.01': 0.01
    }
    
    # Calculate the change needed
    change = given - charged
    if change < 0:
        raise ValueError("Amount given is less than amount charged.")
    
    result = {}
    for denom, value in bills_and_coins.items():
        count = int(change // value)
        if count > 0:
            result[denom] = count
        change -= count * value
    
    return result

def main():
    try:
        charged = float(input("Enter the amount charged: "))
        given = float(input("Enter the amount given: "))
        
        change = make_change(charged, given)
        
        print("Change to be given:")
        for denom, count in change.items():
            print(f"${denom}: {count}")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
