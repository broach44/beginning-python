def emoji_converter(message_input):
    words = message_input.split(' ')

    emojis = {
        ":)": "🙂",
        ":(": "☹"
    }

    output = ""

    for word in words:
        output += emojis.get(word, word) + " "

    return output


message = input(">")

print(emoji_converter(message))
