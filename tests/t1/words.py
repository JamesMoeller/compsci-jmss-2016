# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically
words = []
notQuit = True
while notQuit:
    response = input("Please type a word")
    if "quit" in response.lower().rstrip("!,.;:?"):
        notQuit = False
    else:
        words.append(response)

print(words)