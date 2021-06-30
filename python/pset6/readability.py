from cs50 import get_string

# counting letters

text = get_string("Please enter your text: ")

n_words = n_sent = n_letters = i = 0
length = len(text)

while i < length:

    if text[i].isalpha():
        n_let += 1

    # counting words

    if (i == 0 and text[i] != " ") or (i != length and text[i] == " " and text[i + 1] != " "):
        n_words += 1

    # counting letters

    if text[i] == "." or text[i] == "?" or text[i] == "!":
        n_sent += 1
    i += 1

# using the given formula

L = (n_letters / n_words) * 100
S = (n_sent / n_words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

# print

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
