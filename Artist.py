'''
Matthew Kilpatrick
3/29/24
Mastery Was Shown Here:
'''
import random
from tabulate import tabulate
def main():
    list_of_tuples = []

    # Loop through a range (for example, from 0 to 4)
    for i in range(5):
        # Create a tuple (for example, (i, i+1))
        a_tuple = (i, i + 1)

        # Append the tuple to the list
        list_of_tuples.append(a_tuple)
if __name__ == '__main__':
    main()

list = []
x = int(0)
y = int(0)
num_of_fav_artist = int(input("Enter your number of favorite artist: "))
num_of_fav_songs = int(input("Enter your number of fav songs for each artist: "))
for artist in range(num_of_fav_artist):
    artist = input(f"{x+1}. Enter your favorite artist: ")
    for songs in range(num_of_fav_songs):
        songs = input(f"\t{y+1}. Enter favorite songs: ")
        tuple = (artist, songs)
        list.append(tuple)
        y+=1
    x+=1
    y=0
for artist,songs in list:
    if artist == "LUCKI":
        print(songs)
alllove = ("I don't even like you niggas, Why wouldn't I bring my pistol? ,"
           "Why wouldn't I put this Jeep in Track and let you hear the engine? "
           "Did her wrong, she got me back, we don't even gotta mention")
attitiude = ("Blame is on my attitude and you already know what drugs do")
for lyrics in alllove:
    print(lyrics)
cout = int(0)
for lyrics in attitiude:
    if (lyrics == 'a'):
        cout+=1
print(cout)



