import json
import csv
import hashlib

users = r"Tables\users.json"

#Internal functions DONT TOUCH THIS 
def __read_file_json(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

def __read_file_csv(file_name):
    data = []
    with  open(file_name, "r") as file:
        content = csv.reader(file)
        next(content)

        for row in content:
            data.append(row)

    return data

def __add(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def __find_by_nickname(data, nickname):
    for user in data:
        if user["nickname"] == nickname:
            return user
        
    return

    
def __maximum_id(data):
    maximum = 0
    for user in data:
        if user["id"] > maximum:
            maximum = user["id"] + 1

    return maximum


def __hash_password(password):
    password_bytes = password.encode('utf-8')
    
    hash_object = hashlib.sha256()
    
    hash_object.update(password_bytes)
    
    hashed_password = hash_object.hexdigest()
    
    return hashed_password


def __check_if_instructor(instructor_code):
    return instructor_code == "aua_bocavik"

#External Functions
def modify(nickname, firstname, lastname, password):
    data = __read_file_json(users)
    user = __find_by_nickname(data, nickname)

    if user:
        data.remove(user)
        user["firstname"] = user["firstname"] if user["firstname"] == firstname else firstname
        user["lastname"] = user["lastname"] if user["lastname"] == lastname else lastname

        new_password = __hash_password(password)
        user["password"] = user["password"] if user["password"] == new_password else new_password

        data.append(user)
        __add(data, users)


def register(nickname, firstname, lastname, password, status = "student", instructor_code = None):
    data = __read_file_json(users)
    if __find_by_nickname(data, nickname):
        return False
    
    if instructor_code and not __check_if_instructor(instructor_code):
        return False
    
    password = __hash_password(password)
    new_user = {
        "id":__maximum_id(data), 
        "nickname":nickname, 
        "firstname":firstname, 
        "lastname":lastname, 
        "status":status, 
        "grades":[],
        "questions":[], 
        "password":password,
        }

    
    data.append(new_user)
    __add(data, users)

    return True


def login(nickname, password):
    data = __read_file_json(users)
    current_user = __find_by_nickname(data, nickname)
    if not current_user:
        return False
    
    current_password = __hash_password(password)
    original_password = current_user["password"] 

    return current_password == original_password


def remove(nickname):
    data = __read_file_json(users)
    current_user = __find_by_nickname(data, nickname)

    if not current_user:
        return False
    
    data.remove(current_user)

    __add(data, users)

    return True

# Example usages:
#register("lav_txa777", "Grno","Petrsyan","lavtxaemes")
#login("lav_txa777","lavtxaemes")
#remove("lav_txa777")
#modify("AceCoder", "Aced", "Coder", "AceCoder123")