

def is_db_name_correct(db_name):
    return len(db_name.replace(" ", "")) > 0

def take_db_information():
    db_name = input("Input database name ?")
    db_user = input("Input database user ?")
    db_password = input("Input database password ?")
    db_host = input("Input database host ?")
    db_port = input("Input database port ?")


