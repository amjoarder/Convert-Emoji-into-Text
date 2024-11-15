import demoji

#https://www.geeksforgeeks.org/videos/convert-emoji-into-text-in-python/

text = "Good Morning! 😊 🌹 🚂"

'''
#this works too
emoji_found = demoji.findall(text)

print(emoji_found)
'''

text_description = demoji.replace_with_desc(text, sep=",")

print(text_description)