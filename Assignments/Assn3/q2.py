char = input("Enter the character: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if char.isalpha():
    if char in vowels:
        print(f'{char} is a Vowel.')
    else:
        print(f'{char} is a Consonant.')
else:
    print(f'{char} is neither a vowel nor a consonant.')   