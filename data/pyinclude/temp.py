import os

def delete():
    path = "../temp/"
    ids = path + "ids/json/"

    if os.path.exists(path+"ids.json"):
        os.remove(path+"ids/json/ids.json")
    else:
        pass