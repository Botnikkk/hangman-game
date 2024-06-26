

import os
try:
    import operator
    import pickle as p
    import asyncio 
    import random
    import os
    import botnikkk as n
except :
    os.system('cls')
    print('Installing packages.....')
    os.system(' pip install -r requirements.txt')
    os.system('cls')
    import operator
    import pickle as p
    import asyncio 
    import random
    import os
    import botnikkk as n
input('Please enter fullscreen mode for best experience, input any key if you are in fullscreen mode - ')

file_path = "user_data"

async def signup(): 
    os.system('cls')
    n.centre("-", symbol="-")

    #opening the file
    file = open(file_path, "ab+")
    file.seek(0,0)

    #storing existing ids
    id_data = []
    while True : 

        try : 
            values = p.load(file) 
            id_data.append(values["id"])    

        except EOFError :
            break
    
    n.centre(symbol="=", title=" Sign up page ")

    #taking id input
    id_input = n.format_input("Enter ID that you wish to register wish")
    while id_input.lower() in id_data :
        n.centre("ID already exists")
        id_input = n.format_input("Enter ID that you wish to register wish")
    
    #taking pass input
    pass_input = n.format_input("Enter a 8 or more character long password")
    while len(pass_input) < 8:
        n.centre("Password is too short")
        pass_input = n.format_input("Enter a 8 or more character long password")
    
    #storing data
    update_dic = {"id" : id_input.lower(), "pass" : pass_input.lower(), "hints" : 3, "points" : 0, "score" : 0}
    p.dump(update_dic, file)
    file.close()

    n.centre("=",symbol='=')
    await login()

async def login() :
    os.system('cls')
    n.centre("-", symbol="-")
    n.centre(symbol="=", title=" Login page ")

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
    input_id = n.format_input("Enter your ID")
    if input_id in id_data  : 
            index = id_data.index(input_id)

    else:
        while input_id not in id_data and id_trials > 0 :
            n.centre(" No such ID was found ! you have {trials} trials left ".format(trials=id_trials))
            input_id = n.format_input("Enter your ID")
            id_trials -= 1

            if input_id in id_data and id_trials >= 0 : 
                index = id_data.index(input_id)
                break

    if id_trials >= 0 and input_id in id_data  :
        #checking pass
        input_pass = n.format_input("Enter your password")
        if input_pass.lower() != pass_data[index] :

            while input_pass != pass_data[index] and pass_trials > 0 : 

                n.centre(" incorrect password ! you have {trials} trials left ".format(trials=pass_trials))
                input_pass = n.format_input("Enter your password")
                pass_trials -= 1
                if input_pass == pass_data[index] :
                    break
    
        if pass_trials >= 0 and input_pass == pass_data[index] :
            #welcome screen
            if input_id in id_data and input_pass == pass_data[index] :
                n.centre(symbol="-", title=" Welcome {user} ".format(user=input_id))
                await homescreen(input_id)
        else : 
                n.centre(symbol="=", title=" You were logged out ")
    else : 
                n.centre(symbol="=", title=" You were logged out ")

async def homescreen(user):
    os.system('cls')
    n.centre("-", symbol="-")
    #printing home bar
    n.centre(symbol="=", title=" Home Page ")

    #printing and detecting option choices
    option_list = ["play", "leaderboard", "guide and info", "hint shop", "user info", "delete account", "log out"]
    answer = n.ans_check(option_list)

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
        await del_acc(user)

    elif answer == option_list[6] :
         n.centre(symbol="=", title=" You were logged out ")
   
async def info(user):
    os.system('cls')
    n.centre("-", symbol="-")
    #fetching and printing the file
    file = open("info.txt", "r+")
    lines = file.readlines()
    n.centre(" Guide to the game ", symbol='-')
    for i in lines :
        i = i.strip('\n')
        if i == 'Guide' or i == 'Info' :
            n.centre(i, symbol='-')
        else :
            n.centre(i)
    
    #returning to homescreen
    option_list = ["back"]
    n.ans_check(option_list)
    await homescreen(user)

async def user_info(user) :
    os.system('cls')
    n.centre("-", symbol="-")
    #opening file and printing and detecting options
    file = open(file_path, "rb+")
    n.centre(symbol="=", title=" User Info ")
    option_list = ["my info", "another user info", "back"]
    answer = n.ans_check(option_list)

    if answer == option_list[0] : 

        #iterating through file to find and print data
        while True : 

            try : 
                values = p.load(file) 
                if values["id"] == user : 
                    string = "Info of {}".format(user)
                    n.centre(symbol= "-",title=string)
                    string = "Hints = {hints}\nPoints = {points}\nScore = {score}".format(hints=values["hints"], points=values["points"], score = values["score"])
                    str_list = string.split("\n")
                    for i in str_list : 
                        n.centre(i)
            except EOFError :
                break
    elif answer == option_list[1] : 


        #admin check
        if user in ["nikhil", "ekta"] :
            
            #admin
            input_id = n.format_input("Enter the ID you wish to search for") 
            found = 0
            while True : 

                try : 
                    values = p.load(file) 
                    if values["id"] == input_id.lower() :
                        string = "Info of {}".format(input_id)
                        n.centre(symbol= "-",title=string)
                        string = "Hints = {hints}\nPoints = {points}\nScore = {score}".format(hints=values["hints"], points=values["points"], score = values["score"])
                        str_list = string.split("\n")
                        for i in str_list : 
                            n.centre(i)
                        found = 1
                except EOFError :
                    break
            if found == 0 :
                n.centre("No user with such ID was found")
        else  : 

            #not admin
            n.centre("-" ,"Only admins can use this option !")   
    if answer != option_list[2] :
        answer = n.ans_check(option_list=["back"])
    await homescreen(user)
    file.close()

async def leaderboard(user) :
    os.system('cls')
    n.centre("-", symbol="-")
    #pinting heading 
    n.centre(" Leaderboard ")
    file = open(file_path, "rb+")

    #collecting user data with points
    user_list = {}
    while True : 

            try : 
                value = p.load(file) 
                user_list.update({value["id"] : value["score"]})
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
            gap = 0
            if rank == 10 :
                gap = 1
            string = "Rank {rank} -> {id}".format(rank=rank,id=i[0]) + " "*(10- len(i[0]) - gap) + "score : {score}".format(score=i[1])
            n.centre(string)
            if i[0] == user : 
                user_rank = rank
            rank += 1
        else :
            break

    #printing self rank
    if user_rank == 0 : 
        user_rank = " * "
    n.centre("Your rank")
    string = "Rank {rank} -> {id}".format(rank=user_rank,id=user_data["id"]) + " "*(10- len(i[0]))+ "score : {score}".format(score=user_data["score"])
    n.centre(string)

    answer = n.ans_check(option_list=["back"])
    await homescreen(user)

async def hint_shop(user) : 
    os.system('cls')
    n.centre("-", symbol="-")
    n.centre(" Hint shop ")

    file = open(file_path, "rb+")
    file.seek(0,0)

    #printing prices
    n.centre ("* For more than 1 hints purchased  : 3 points per hint")
    n.centre("* For more than 6 hints purchased  : 2 points per hint")
    n.centre("* For more than 10 hints purchased  : 1 point per hint")

    #back option
    n.centre("* back")

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
    n.centre(string)

    #purchase and price checking
    answer = n.format_input("Enter the number of hints you wish to purchase -") 
    if answer.lower() != "back" :

        #confirming ineteger
        answer = n.int_check(answer)

        #determining cost
        if answer < 6 : 
            cost = 3
        elif answer < 10 :
            cost = 2
        elif answer >= 10 :
            cost = 1

        #total ammount
        total = cost*answer

        #checking user info and informing if points not enough
        if user_dic["points"] >= total :
            user_dic.update({"hints" : user_dic["hints"] + answer})
            user_dic.update({"points" : user_dic["points"] - total})
            string = " Your succsecfully paid {points} points and purchased {ammount} hints ".format(points=total,ammount=answer)
            n.centre(string )
        else :
            n.centre("Not enough points !")

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

    guessed = await newgame(user)
    #checking if player has exited
    if guessed != "back" :
        n.centre("Do you wish to play again?")
        ans = n.ans_check(option_list=["yes", "no"])
        if ans == "yes" :
            guessed = await newgame(user)
    await homescreen(user)

async def newgame(user) :
    os.system('cls')
    n.centre("-", symbol="-")
    #initiating the game
    n.centre(" Starting the game ") 
    n.centre("your game will be starting in.....") 
    await asyncio.sleep(0.5) 
    for i in range(1,4) :
        n.centre(str(4-i))
        await asyncio.sleep(1)

    #iterating rounds
    score = 0 
    round = 1
    guessed = await word_choose(round, user,score)
    while guessed == "yes" :
        score += 1
        round += 1
        n.centre(" Round - {round} ! ".format(round=round))
        guessed  = await word_choose(round,user,score)
    return guessed

async def word_choose(round,user,score) :
    os.system('cls')
    n.centre(" Round - {round} ! ".format(round=round))
    n.centre("-", symbol="-")
    #extracting user data
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
    words_guessed = []
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
        n.centre("-", symbol="-")
        back = "false"
        #hint data
        hint_used = "no"

        #Making and printing the word
        word_str = ""
        for i in print_list :
            word_str += i 
        guessed_str = "Words guessed till now : "
        for i in words_guessed : 
            guessed_str += i + ", "
        word_str = word_str.strip() 
        n.centre(word_str)
        n.centre(guessed_str)
        n.centre("* hint")
        n.centre("* back")
        if word_str != word_choosen :
            #taking input  
            input_word = n.format_input("Enter a word")
            while len(input_word)  > 1 or not input_word.isalpha():
                #if hint used
                if input_word.lower() == "hint" :
                    if user_dic['hints'] > 0 :
                        user_dic.update({"hints" : user_dic["hints"] - 1})
                        input_word = word_choosen[random.choice(index_list)]
                        n.centre( " You used a hint ! You now have {hints} hints left ".format(hints=user_dic['hints']))
                        hint_used = "yes"
                        break
                    else : 
                        n.centre("You've exhaushted all your hints!")
                #if player has exited
                elif input_word.lower( ) == "back" : 
                    back = "true"
                    break
                n.centre("Please Enter a single letter")
                input_word = n.format_input("Enter a word")
            os.system('cls')
            n.centre(" Round - {round} ! ".format(round=round))   

            if back != "true" :
                #checking if input is correct
                if input_word not in words_guessed :
                    words_guessed.append(input_word)
                if input_word in word_list : 
                    if hint_used == 'no' :
                        n.centre( " Correct Guess ")
                    index = 0 
                    for i in word_choosen :
                        if i == input_word.lower() : 
                            print_list[index] = input_word
                            if index in index_list :
                                index_list.remove(index)
                        index += 1
                    if trials <= 9 :          
                        print(hangman_list[9-trials])
                        n.centre(" ")
                        n.centre("Trials left : {trials}".format(trials=trials))
                else :
                    trials -= 1
                    n.centre( " Incorrect guess ! ")
                    print(hangman_list[9-trials])
                    n.centre(" ")
                    n.centre("Trials left : {trials}".format(trials=trials))
            else :
                break

    if score > user_dic['score'] :
        user_dic.update({"score" : score})
    #checking if the user was able to guess the word
    if back != "true" :
        if trials == 0 : 
            guessed = "no"
            n.centre( " You couldn't guess the word ! The game has ended ! ")
            n.centre(" The word was : {word} ".format(word=word_choosen))
        else : 
            guessed = "yes"
            user_dic.update({"points" : user_dic["points"] + point})
            n.centre( " You guessed the word ! You gained {points} points ! ".format(points=point))
            n.centre("Next round will start in.....") 
            await asyncio.sleep(0.5) 
            for i in range(1,4) :
                n.centre(str(4-i))
                await asyncio.sleep(1)

    #if player exits the game
    else :
        n.centre(" You exited the game ! ")
        guessed = "back"
    file = open("user_data", "bw+")
    all_users.append(user_dic)

    #dumping the final data
    file.seek(0,0)
    for i in all_users : 
        p.dump(i, file)
    file.close()

    return guessed

async def del_acc(user) :
    os.system('cls')
    n.centre("-", symbol="-")
    #printing main screen
    n.centre(" Accound deletion ")
    n.centre("Are you sure you wish to delete your account?")
    answer = n.ans_check(option_list=["yes", "no"])

    #storing user data
    all_users = []
    if answer == "yes" :
        file = open(file_path, "rb+")
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

        #confirmation
        trials  = 2
        password = n.format_input("Enter your password for confirmation")
        while password != user_dic["pass"] and trials > 0 :
            n.centre(" incorrect password ! you have {trials} trials left ".format(trials=trials))
            password = input("Enter your password for confirmation\n- ")
            trials -= 1
        if trials <= 0 : 
            n.centre(" Action revoked because you could not enter the correct password ! ")
            await homescreen(user)
            all_users.append(user_dic)
        else : 
            n.centre(" Sucssefully deleted account ! ")
        
        file = open(file_path, "wb+")
        for i in all_users : 
            p.dump(i,file)
        file.close()
        
    else : 
        n.centre(" Action revoked ! ")
        await homescreen(user)
    
        
    
#checking if file exists, creates if not
try : 
    file = open(file_path, "br+")
except :
    file = open(file_path, "bw+")
file.close()

#creating the list to print the hangman
file = open("hangman.txt", "r+")
hangman = file.readlines()
file.close()
hangman_list = []
string = ""
alignments = n.get_alignments()
left_align = alignments["left_align"]*" "
for i in hangman :
    try : 
        int(i.strip('\n'))
        hangman_list.append(string.rstrip("\n"))
        string = ""
    except :
        gap = " "*(129 - int((len(i))) - 50)
        string += left_align + "|" + " "*(50)  +  i.strip("\n") +  gap + "|\n"

#cool entry screen 
file = open("design.txt",encoding= "utf8")
lines = file.readlines()
file.close()


#forever running loop for the game
while 1 < 2 :
    os.system('cls')
    string = ""
    for i in  lines : 
        print(left_align + i.strip('\n'))
    n.centre("Are you a existing user ?")
    answer  = n.ans_check(option_list=["yes", "no", "exit game"])   
    if answer == "yes" :
        asyncio.run(login())
    elif answer == "no" :
        asyncio.run(signup())
    else :
        n.centre("Exited the game",symbol='=')
        break