import telebot
try:
    with open("text.txt", "r") as file:
        idlist = file.read().splitlines() # there we make list of ids from text.txt
        idlist = ["1", "2", "3", "4"] # example
        idel = 4 # example
except telebot.apihelper.ApiException as e:
    index_to_del = idlist.index(str(idel)) # we found id which blocked your bot
    if 0 <= index_to_del < len(idlist): # checking the id exists
        del idlist[index_to_del] # delet id from list
    with open("text.txt", "w") as file: 
        for el in idlist: 
            file.writelines(f'{el}\n') # rewriting your file

# was
#1
#2
#3
#4
# the fourth id blocked your bot, we take a bug and delet this id
# now
#1
#2
#3
