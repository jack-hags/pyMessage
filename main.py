import os
import config
import sys
import re
import lyricsgenius

genius = lyricsgenius.Genius("pqu_9c429m_N2wlcBsYUl1CQh8OBZrdCSeJLGJMdbqtB3Ixa2-sWS1c32Al0jTS0")

# GET SONG
text = input("Enter a song name.\nThe first result will be the song that is played.\nMAKE SURE TO BE SPECIFIC WHEN TYPING THE SONG NAME!\n")
print(text)
song = genius.search_song(text)
print("I found a song! Here's the lyrics:"+song.lyrics)

# FORMAT LYRICS SO THAT THERE ARE NO SPACES OR BRACKETS
lyrics = song.lyrics
#m_lyrics = re.sub("[\(\[].*?[\)\]]", "", lyrics)
m_lyrics = re.sub("[\[].*?[\]]", "", lyrics)
f_lyrics = m_lyrics.split("\n")
non_empty_lines = [line for line in f_lyrics if line.strip() != ""]

final = ""
for line in non_empty_lines:
      final += line + "\n"
final = final.replace("878EmbedShare URLCopyEmbedCopy", "")
f = open("ly.txt", "w")
f.write(final)
f.close()

# GET NUMBER
finalNumber = ""
num = input("Enter the number you want to send all of these lyrics to.\nMake sure that you type it correctly!\n")
if num:
    number = input("Is this number correct: "+num+"\nIf it's wrong you won't be able to change it.\nType (y/n)\n")
    if number == "y":
        finalNumber = num
        print("Running... Please wait.")
    elif number == "n":
        print("Terminated. Run this again.")
        sys.exit()
    else:
        print("Not a valid input. Restart from the beginning.")
        sys.exit()
            
# READ TXT FILE AND GET WORDS
def get_words(file_path):
    with open(file_path, 'r') as f:
     text = f.readlines()[0]
    words = text.split()
    return words


def get_lines(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text

# SEND MESSAGE
def send_message(phone_number, message):
    os.system('osascript sendMessage.applescript {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
        #words = get_words('ly.txt')
        # for word in words:
        #send_message('6197516857', word)
        text = get_lines('ly.txt')
        for line in text:
            send_message(finalNumber, line)
