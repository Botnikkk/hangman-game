import operator
import pickle as p
import asyncio 
import random

file_path = "user_data"


def int_check(answer) :
    integer = -1
    while integer < 1 :
        try : 
            int(answer)
            integer = int(answer)
        except : 
            print("Please enter a valid integer !")
            answer = input("Enter the number of hints you wish to purchase\n- ") 
            continue
    return int(answer)

def centre(symbol, title) :
    #aligns the title in centre with symbols around it
    print(str(symbol)*(64-int((len(title)/2))) + title + (64-int((len(title)/2)))*str(symbol) + 2*"\n")

def ans_check(option_list) :

    #prints and detetcs the answers and returns the choose answer
    for i in option_list : 
        centre(symbol=" ", title=("* " + str(i)))

    answer = input("Choose a option\n- ")
    while answer.lower() not in option_list : 
        print("Not a valid answer !")
        answer = input("Choose a option\n- ")
    return answer

def signup():

    #opening the file
    file = open(file_path, "ba+")
    file.seek(0,0)

    #storing existing ids
    id_data = []
    while True : 

        try : 
            values = p.load(file) 
            id_data.append(values["id"])    

        except EOFError :
            break
    
    centre(symbol="=", title=" Sign up page ")

    #taking id input
    id_input = input("Enter ID that you wish to register wish\n- ")
    while id_input.lower() in id_data :
        print("ID already exists")
        id_input = input("Enter ID that you wish to register wish\n- ")
    
    #taking pass input
    pass_input = input("Enter a 8 or more character long password\n- ")
    while len(pass_input) < 8:
        print("Password is too short")
        pass_input = input("Enter a 8 character long password\n- ")
    
    #storing data
    update_dic = {"id" : id_input.lower(), "pass" : pass_input.lower(), "hints" : 0, "points" : 0, "score" : 0}
    p.dump(update_dic, file)
    file.close()

    centre(symbol="=", title="")
    login()

async def login() :

    centre(symbol="=", title=" Login page ")

    file = open(file_path, "br+")

    #sorting existing ids
    id_data = []
    pass_data = []
    while True : 

        try : 
            values = p.load(file) 
            id_data.append(values["id"])
            pass_data.append(values["pass"])    

        except EOFError :
            break

    id_trials = 2
    pass_trials = 2

    #checking id
    input_id = input("Enter your ID\n- ")
    if input_id in id_data and id_trials > -1 : 
            index = id_data.index(input_id)
            #checking pass
            input_pass = input("Enter your password\n- ")
            if input_pass.lower() != pass_data[index] :

                while input_pass != pass_data[index] and pass_trials > 0 : 

                    print("Incorrect password!\nTrial left = {trials}".format(trials=pass_trials))
                    input_pass = input("Enter your password\n- ")
                    pass_trials -= 1

                    if input_pass == pass_data[index] and id_trials > -1 :
                        break
    else:
        while input_id not in id_data and id_trials > 0 :
            print("ID wasn't found\nTrials left = {trials}".format(trials=id_trials))
            input_id = input("Enter your ID\n- ")
            id_trials -= 1

            if input_id in id_data and id_trials > -1 : 
                index = id_data.index(input_id)
                break
        #checking pass
        input_pass = input("Enter your password\n- ")
        if input_pass.lower() != pass_data[index] :

            while input_pass != pass_data[index] and pass_trials > 0 : 

                print("Incorrect password!\nTrial left = {trials}".format(trials=pass_trials))
                input_pass = input("Enter your password\n- ")
                pass_trials -= 1

                if input_pass == pass_data[index] and id_trials > -1 :
                    break
    
    
    #welcome screen
    if input_id in id_data and input_pass == pass_data[index] :
        centre(symbol="-", title=" Welcome {user} ".format(user=input_id))
        await homescreen(input_id)
    else : 
        centre(symbol="=", title=" You were logged out ")

async def homescreen(user):
    #printing home bar
    centre(symbol="=", title=" Home Page ")

    #printing and detecting option choices
    option_list = ["play", "leaderboard", "guide and info", "hint shop", "user info", "log out"]
    answer = ans_check(option_list)

    #performing tasks based on choice
    if answer == option_list[0] :
        await startgame(user)

    elif answer == option_list[1] :
        await leaderboard(user)

    elif answer == option_list[2] :
        await info(user)

    elif answer == option_list[3] :
        await hint_shop(user)
        
    elif answer == option_list[4] :
        await user_info(user)

    elif answer == option_list[5] :
         centre(symbol="=", title=" You were logged out ")
   
async def info(user):

    #fetching and printing the file
    file = open("info.txt", "r+")
    file.seek(0,0)
    lines = file.readlines()
    for i in lines : 
        print(i,end="")
    
    #returning to homescreen
    option_list = ["back"]
    answer = ans_check(option_list)

    if answer == "back" :
        await homescreen(user)

async def user_info(user) :

    #opening file and printing and detecting options
    file = open(file_path, "rb+")
    centre(symbol="=", title=" User Info ")
    option_list = ["my info", "another user info", "back"]
    answer = ans_check(option_list)

    if answer == option_list[0] : 

        #iterating through file to find and print data
        while True : 

            try : 
                values = p.load(file) 
                if values["id"] == user : 
                    string = "Info of {}".format(user)
                    centre(symbol= "-",title=string)
                    print("Hints = {hints}\nPoints = {points}\nScore = {score}".format(hints=values["hints"], points=values["points"], score = values["score"]))

            except EOFError :
                break

    elif answer == option_list[1] : 

        #admin check
        if user in ["nikhil", "ekta"] :
            
            #admin
            input_id = input("Enter the ID you wish to search for\n- ")
            found = 0
            while True : 

                try : 
                    values = p.load(file) 
                    if values["id"] == input_id.lower() :
                        string = "Info of {}".format(input_id)
                        centre(symbol= "-",title=string)
                        print("Hints = {hints}\nPoints = {points}\nScore = {score}".format(hints=values["hints"], points=values["points"], score = values["score"]))
                        found = 1
                except EOFError :
                    break
            if found == 0 :
                print("No user with such ID was found")
        else  : 

            #not admin
            centre("-" ,"Only admins can use this option !")
    elif answer == option_list[2] :
       await homescreen(user)
    
    answer = ans_check(option_list=["back"])
    await homescreen(user)
    file.close()

async def leaderboard(user) :

    #pinting heading 
    centre("=", " Leaderboard ")
    file = open(file_path, "rb+")

    #collecting user data with points
    user_list = {}
    while True : 

            try : 
                value = p.load(file) 
                user_list.update({value["id"] : value["points"]})
                if value["id"] == user : 
                    user_data = value
            except EOFError :
                break

    #sorting and printing the user data
    sorted_dic = sorted(user_list.items(), key=operator.itemgetter(1), reverse=True)
    user_rank = 0
    rank = 1
    for i in sorted_dic :
        if rank < 11 :
            string = "Rank {rank} -> {id}".format(rank=rank,id=i[0]) + " "*(10- len(i[0])) + "points : {points}".format(points=i[1])
            print(50*" ", string)
            if i[0] == user : 
                user_rank = rank
            rank += 1
        else :
            break

    #printing self rank
    if user_rank == 0 : 
        user_rank = " * "
    print(2*"\n")
    centre(" ", "Your rank")
    string = "Rank {rank} -> {id}".format(rank=user_rank,id=user_data["id"]) + " "*(10- len(i[0]))+ "points : {points}".format(points=user_data["points"])
    print(50*" ", string, "\n")

    answer = ans_check(option_list=["back"])
    await homescreen(user)

async def hint_shop(user) : 
    centre("=", " Hint shop ")

    file = open(file_path, "rb+")
    file.seek(0,0)

    #printing prices
    price_str = """
    * For more than 1 hints purchased  : 3 points per hint

    * For more than 6 hints purchased  : 2 points per hint
    
    * For more than 10 hints purchased  : 1 point per hint
    """
    centre(" ", price_str)

    #back option
    centre(symbol=" ", title=("* " + "back"))

    #storing data to dump later and detecting current user
    all_users = []
    while True : 

        try : 
            values = p.load(file) 
            if values["id"] == user : 
                user_dic = values
            else :
                all_users.append(values)

        except EOFError :
            break
    #printing balance
    string = "Points balance : {points}  hints balance : {hints}".format(points=user_dic["points"], hints=user_dic["hints"])
    centre(" ", string)

    #purchase and price checking
    answer = input("Enter the number of hints you wish to purchase\n- ")
    if answer.lower() != "back" :

        #confirming ineteger
        answer = int_check(answer)

        #determining cost
        if answer < 10 : 
            cost = 2
        elif answer < 6 :
            cost = 3
        elif answer >= 10 :
            cost = 1

        #total ammount
        total = cost*answer

        #checking user info and informing if points not enough
        if user_dic["points"] >= total :
            user_dic.update({"hints" : user_dic["hints"] + answer})
            user_dic.update({"points" : user_dic["points"] - total})
            string = " Your succsecfully paid {points} points and purchased {ammount} hints ".format(points=total,ammount=answer)
            centre("-",string )
        else :
            print("Not enough points !")

        #updating data
        all_users.append(user_dic)

        file.close()
        file = open("user_data", "bw+")

        #dumping the final data
        file.seek(0,0)
        for i in all_users : 
            p.dump(i, file)
        file.close()
    await homescreen(user)

async def startgame(user) :

    #initiating the game
    centre("=", " Starting the game ") 
    print("your game will be starting in.....\n") 
    await asyncio.sleep(0.5) 
    for i in range(1,4) :
        print(4-i)
        await asyncio.sleep(1)

    #iterating rounds
    round = 1
    centre(" ", " Round{round} ! ".format(round=round))
    guessed = word_choose(round, user)
    while guessed == "yes" :
        round += 1
        centre(" ", " Round{round} ! ".format(round=round))
        guessed  = word_choose(round,user)

    print("Do you wish to play again?")
    ans = ans_check(option_list=["yes", "no"])
    if ans == "yes" :
        await startgame(user)
    homescreen(user)

def word_choose(round,user) :

    #extrating data
    file = open("word_data.txt", "r+")
    words = file.readlines()
    file.close()

    #choosing a suitable word and points via rounds 
    word_choosen = random.choice(words) 
    if round < 4 :
        while len(word_choosen) > 8 :
            word_choosen = random.choice(words)
        point = 1
    elif round < 10 : 
        while len(word_choosen) > 10 and len(word_choosen) < 7 :
             word_choosen = random.choice(words)
        point = 3
    else : 
        while len(word_choosen) > 15 and len(word_choosen) < 10 :
             word_choosen = random.choice(words)
        point = 5

    #storing word indexes and characters
    word_choosen = word_choosen[:len(word_choosen)-1]
    revealed_words = int(len(word_choosen)/3)
    file.close()
    word_list = []
    index_list= []
    num = 0
    for i in word_choosen :
        if i != "\n" :
            if i not in word_list : 
                word_list.append(i)
            index_list.append(num)
            num += 1
    #making the scarmbled word for user
    print_list = []
    for i in range(len(word_choosen)) :
        print_list.append("_")

    for i in range(revealed_words) :
        index = random.choice(index_list)
        print_list[index] = (list(word_choosen))[index]
        index_list.remove(index)
    

    #storing trials and initiating main game
    word_str = ""
    trials = 10
    while word_str != word_choosen and trials > 0 :

        #Making and printing the word
        word_str = ""
        for i in print_list :
            word_str += i 
        word_str = word_str.strip() 
        centre(" ", word_str)
        if word_str != word_choosen :
            #taking input
            input_word = input("Enter a word\n-")
            while len(input_word)  > 1 and  not input_word.isalpha():
                print("Please Enter a single letter")
                input_word = input("Enter a word\n-")

            #checking if input is correct
            if input_word in word_list : 

                centre("-", " Correct Guess ")
                index = 0 
                for i in word_choosen :
                    if i == input_word.lower() : 
                        print_list[index] = input_word
                    index += 1
            else : 
                trials -= 1
                centre("-", " Incorrect guess ! ")
                centre(" ", "Trials left : {trials}".format(trials=trials))
    
    file = open("user_data", "rb+")
    file.seek(0,0)
    all_users = []
    while True : 

        try : 
            values = p.load(file) 
            if values["id"] == user : 
                user_dic = values
            else :
                all_users.append(values)
        except EOFError :
            break
    file.close()
    #checking if the user was able to guess the word
    if trials == 0 : 
        guessed = "no"
        centre("-", " You couldn't guess the word ! The game has ended ! ")
        centre(" ", " The word was : {word} ".format(word=word_choosen))
    else : 
        guessed = "yes"
        user_dic.update({"points" : user_dic["points"] + point})
        centre("-", " You guessed the word ! You gained {points} points ! ".format(points=point))
    all_users.append(user_dic)

    file = open("user_data", "bw+")

    #dumping the final data
    file.seek(0,0)
    for i in all_users : 
        p.dump(i, file)
    file.close()

    return guessed




#checking if file exists, creates if not
try : 
    file = open(file_path, "br+")
except :
    file = open(file_path, "bw+")
file.close()

#cool entry screen 
string = """
================================================================================================================================
|                                                                                                                              |
|                        ░█─░█ ─█▀▀█ ░█▄─░█ ░█▀▀█ ░█▀▄▀█ ─█▀▀█ ░█▄─░█ 　 ░█▀▀█ ─█▀▀█ ░█▀▄▀█ ░█▀▀▀                              | 
|                        ░█▀▀█ ░█▄▄█ ░█░█░█ ░█─▄▄ ░█░█░█ ░█▄▄█ ░█░█░█ 　 ░█─▄▄ ░█▄▄█ ░█░█░█ ░█▀▀▀                              |
|                        ░█─░█ ░█─░█ ░█──▀█ ░█▄▄█ ░█──░█ ░█─░█ ░█──▀█ 　 ░█▄▄█ ░█─░█ ░█──░█ ░█▄▄▄                              |
|                                                                                                                              |
|                                           𝙱𝚢 𝙽𝚒𝚔𝚑𝚒𝚕 𝙲𝚑𝚊𝚞𝚍𝚑𝚊𝚛𝚢 𝚊𝚗𝚍 𝙴𝚔𝚝𝚊 𝚂𝚒𝚗𝚐𝚕𝚊                                                |
|                                                                                                                              |
================================================================================================================================
"""

#forever running loop for the game
while 1 < 2 :
    print(string)
    centre( " ","Are you a existing user ?")
    answer  = ans_check(option_list=["yes", "no"])   
    if answer == "yes" :
        asyncio.run(login())
    else :
        signup()

