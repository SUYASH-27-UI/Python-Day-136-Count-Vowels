text = input("Enter a word or sentence: ")

count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print("Total vowels:", count)
