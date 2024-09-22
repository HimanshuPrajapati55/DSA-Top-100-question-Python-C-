import random

def birthday_paradox_simulation(n_people, trials=1000):
    def has_duplicate_birthdays(num_people):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        return len(birthdays) != len(set(birthdays))
    
    count = sum(has_duplicate_birthdays(n_people) for _ in range(trials))
    probability = count / trials
    return probability

def main():
    for n in range(5, 101, 5):
        prob = birthday_paradox_simulation(n)
        print(f"Probability of having the same birthday with {n} people: {prob:.2f}")

if __name__ == "__main__":
    main()
