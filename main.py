import pickle as p

file_path = "user_data"


def centre(symbol, title) :
    print(str(symbol)*(64-int((len(title)/2))) + title + (64-int((len(title)/2)))*str(symbol) + 2*"\n")


def ans_check(option_list) :

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
    
    centre(symbol="=", title="Sign up page")

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

    centre(symbol="=", title="Login page")

    file = open(file_path, "br+")

    #storing existing ids
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
    
    if input_id in id_data and input_pass == pass_data[index] :
        centre(symbol="=", title=" Welcome {user} ".format(user=input_id))
        homescreen(input_id)
    else : 
        centre(symbol="=", title="You were logged out")


def homescreen(user):
    option_list = ["play", "leaderboard", "guide and info", "hint shop", "user info"]
    answer = ans_check(option_list)
    if answer == option_list[2] :
        info(user)
    
    
def info(user):
    file = open("info.txt", "r+")
    file.seek(0,0)
    lines = file.readlines()
    for i in lines : 
        print(i,end="")
    
    option_list = ["back"]
    answer = ans_check(option_list)

    if answer == "back" :
        homescreen(user)
    











#checking if file exists, creates if not
try : 
    file = open(file_path, "br+")
except :
    file = open(file_path, "bw+")
file.close()

while 1 < 2 :
    answer  = input("Are you a existing user?\n- ")
    while answer.lower() not in ["yes", "no"] :
        print("Invalid answer")
        answer  = input("Are you a existing user?\n- ")
    if answer == "yes" :
        login()
    else :
        signup()
