def vowels(n):
    vowels = "aeiouAEIOU"
    count = 0

    for char in n:
        if char in vowels:
            count += 1
    return count



data = "hello"
vowel_count = vowels(data)
print(f"Number pf vowels in '{data}': '{vowel_count}' ")
