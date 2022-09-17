def translate(phrase):
    conversion = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            conversion = conversion + "V"
        else:
            conversion = conversion + letter.lower()
    return conversion


user_input = input("Please enter a phrase: ")
print(translate(user_input))
