"""
Matthew Kilpatrick
3-6-24
Nested For-Loop Work
Asking The User For Their Favorite Artist and Their Favorite Songs By Those Artist
Then Writing And Reading Them From A File
"""
def raven2():
    file_for_strings = open("RavenFile.txt", 'w') # This line opens a new file for us WRITE data to
    index = int(0)
    index_file_artist = int(0) # index for artists inside the text file
    index_file_songs = int(0) # index for songs inside the text file
    num_of_artist = int(input("How many arist are your favorite: "))
    num_of_songs = int(input("How many songs are your favorite: "))
    print("The number of artist will be entering: " + str(num_of_artist) + "\nThe number of songs we will be entering: " + str(num_of_songs))
    new_list = []
    index1 = int(0)
    index2 = int(0)
    # ⬇︎⬇︎⬇︎⬇︎⬇︎⬇︎⬇-Nested For-Loop︎-⬇︎⬇︎⬇︎⬇︎⬇︎⬇︎⬇︎⬇︎⬇︎⬇︎⬇
    print()
    for i in range(num_of_artist):
        i = str(input(f"Enter Artist #{index1+1}: ")) # ⬅︎⬅︎⬅︎⬅︎ This line uses the variable 'i' to GET the USER entered artist i
        file_for_strings.write(f"Artist #{index_file_artist+1}: {i}\n") # ⬅︎⬅︎⬅︎⬅︎ This line writes the ENTERED ARTIST to the file
        for j in range(num_of_songs):
            j = str(input(f"\tEnter Song #{index2+1}: "))
            file_for_strings.write(f"\tSong #{index_file_songs + 1}: {j}\n") # ⬅︎⬅︎⬅︎⬅︎This line writes the ENTERED SONGS to the file
            index2 += 1
            index_file_songs += 1
        print()
        index1+=1
        index_file_artist += 1
        index2 = 0 # Reset The Numbers Index To 0 BEFORE asking for the next set of songs:
        index_file_songs = 0 # Reset The Numbers Index To 0 BEFORE asking for the next set of songs BUT FOR THE INDEX IN THE FILE:
    file_for_strings.close() # ⬅︎⬅︎⬅︎⬅︎ REMEMBER TO CLOSE THE FILE!!!!!!!!!!!!!!!
if __name__ == '__main__':
    raven2()
print()
print("Users Favorite Artist and Songs: ")
# Reading from a file:
def ReadingRaven2():
    file_for_String = open("RavenFile.txt", "r") # open the file to READ from.
    for lines in file_for_String:
        line = str(lines) # convert everything in the file thats be read/lines that are being read
        print(f"{line}", end="")
if __name__ == '__main__':
    ReadingRaven2()

def main():
    list = []
    evenlist = []
    oddlist = []
    fiveSlist= []
    sevenSlist = []
    listOfAll = [[list], [evenlist], [oddlist], [fiveSlist], [sevenSlist]]
    count = int(0)
    index = int(0)
    count_of_evens = int(0)
    count_of_odds = int(0)
    count_of_5s = int(0)
    count_of_7s = int(0)
    sum_of_evens = int(0)
    sum_of_odds = int(0)
    sum_of_5s = int(0)
    sum_of_7s = int(0)
    sum = int(0)
    amount = int(input("How many numbers will be storing: "))
    print(f"The amount of numbers will be entering today: {amount}")
    for nums in range(0, amount):
        nums = int(input(f"{index+1}. Enter numbers: "))
        index+=1
        sum += nums
        if(nums % 2 == 0):
            count_of_evens += 1
            sum_of_evens += nums
            evenlist.append(nums)
       # elif(nums % 2 != 0):
            #count_of_odds += 1
            #sum_of_odds += nums
            #oddlist.append(nums)
        elif(nums % 5 == 0):
            count_of_5s += 1
            sum_of_5s += nums
            fiveSlist.append(nums)
        elif(nums % 7 == 0):
            count_of_7s +=1
            sum_of_7s += nums
            sevenSlist.append(nums)
    print(f'Number of Evens: {count_of_evens}')
    print(f'Number of Odds: {count_of_odds}')
    print(f'The Total Sum: {sum}')
    print(f'The number of multiples of 5s: {count_of_5s}')
    print(f'The number of multiples of 7s: {count_of_7s}')
    print(f'The sum of the all the multiples of 5s: {sum_of_5s}')
    print(f'The sum of the all the multiples of 7s: {sum_of_7s}')
    print(listOfAll)
if __name__ == '__main__':
    main()
