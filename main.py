import pickle as p

file_path = "user_data"

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
    

#checking if file exists, creates if not
try : 
    file = open(file_path, "br+")
except :
    file = open(file_path, "bw+")
file.close()


while 1 < 2:
    signup()

