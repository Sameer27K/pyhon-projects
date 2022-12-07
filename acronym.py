# Ask the user for the phrase or text
phrase = input("Enter a phrase or text: ")

# Split the phrase into a list of words
words = phrase.split()

# Initialize the acronym variable
acronym = ""

# Iterate over the words in the phrase
for word in words:
    # Get the first letter of the word
    first_letter = word[0]
    # Add the first letter to the acronym (in uppercase)
    acronym += first_letter.upper()

# Print the acronym
print(acronym)
