def remove_words(text, wordstoremove):
    words = text.split()  
    filtered_words = [word for word in words if word not in wordstoremove]
    return " ".join(filtered_words) 

text = input("Enter a string: ")
wordtoremove = input("Enter words to remove (separated by spaces): ").split()
new_text = remove_words(text, wordstoremove )
print("\nString after removing given words:")
print(new_text)
