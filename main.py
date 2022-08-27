import operator
import pickle as p

file_path = "user_data"


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

def login() :

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
        homescreen(input_id)
    else : 
        centre(symbol="=", title=" You were logged out ")

def homescreen(user):
    #printing home bar
    centre(symbol="=", title=" Home Page ")

    #printing and detecting option choices
    option_list = ["play", "leaderboard", "guide and info", "hint shop", "user info", "log out"]
    answer = ans_check(option_list)

    #performing tasks based on choice
    if answer == option_list[0] :
        a=1

    elif answer == option_list[1] :
        leaderboard(user)

    elif answer == option_list[2] :
        info(user)

    elif answer == option_list[4] :
        user_info(user)

    elif answer == option_list[5] :
        centre(symbol="=", title=" You were logged out ")
   
def info(user):

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
        homescreen(user)

def user_info(user) :

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
            print("Only admins can use this option !")
    elif answer == option_list[2] :
        homescreen(user)
    
    answer = ans_check(option_list=["back"])
    homescreen(user)
    file.close()

def leaderboard(user) :

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
    homescreen(user)




#checking if file exists, creates if not
try : 
    file = open(file_path, "br+")
except :
    file = open(file_path, "bw+")
file.close()

string = """
================================================================================================================================
|                                                                                                                              |
|                        ░█─░█ ─█▀▀█ ░█▄─░█ ░█▀▀█ ░█▀▄▀█ ─█▀▀█ ░█▄─░█ 　 ░█▀▀█ ─█▀▀█ ░█▀▄▀█ ░█▀▀▀                              | 
|                        ░█▀▀█ ░█▄▄█ ░█░█░█ ░█─▄▄ ░█░█░█ ░█▄▄█ ░█░█░█ 　 ░█─▄▄ ░█▄▄█ ░█░█░█ ░█▀▀▀                              |
|                        ░█─░█ ░█─░█ ░█──▀█ ░█▄▄█ ░█──░█ ░█─░█ ░█──▀█ 　 ░█▄▄█ ░█─░█ ░█──░█ ░█▄▄▄                              |
|                                                                                                                              |
================================================================================================================================
"""

while 1 < 2 :
    print(string)
    centre( " ","Are you a existing user ?")
    answer  = ans_check(option_list=["yes", "no"])   
    if answer == "yes" :
        login()
    else :
        signup()
