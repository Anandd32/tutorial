def rvowels(str):
    return "".join(char for char in str if char.lower() not in "aeiou")
input_string = "how are you"
print("String after removing vowels:", rvowels(input_string))
