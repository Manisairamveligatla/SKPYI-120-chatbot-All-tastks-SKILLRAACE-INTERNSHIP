import demoji

demoji.download_codes()

def convert_emoji_to_text(text):
    return demoji.replace_with_desc(text, sep=":")

text_with_emojis = "I love playing cricket 🏏 and ludo 🎲! 😊"


text_with_descriptions = convert_emoji_to_text(text_with_emojis)

print(text_with_descriptions)
