import os
import json

def location():
  loguser = "C:/Users/" + os.getlogin()

  logi = str(loguser)

  with open('runs.json', 'r') as f:
    runs = json.load(f)
  
  runs['location'] = {}
  runs['location']['libs'] = {}
  runs['location']['libs']['sys'] = str(logi + "/Desktop/Sponky/SP languaje/sp libs/sys.sp")
  runs['location']['libs']['math'] = str(logi + "/Desktop/Sponky/SP languaje/sp libs/math.sp")
  runs['location']['libs']['console'] = str(logi + "/Desktop/Sponky/SP languaje/sp libs/console.sp")
  runs['location']['libs']['files'] = str(logi + "/Desktop/Sponky/SP languaje/sp libs/files.sp")
  runs['location']['libs']['init'] = str(logi + "/Desktop/Sponky/SP languaje/sp libs/init.sp")

  with open(logi+'/Desktop/Sponky/SP languaje/data/runs.json', 'w') as f:
    json.dump(runs, f)

class Check:
  def user_json():
    loguser = "C:/Users/" + os.getlogin()
    logi = str(loguser)

    with open(logi + "/Desktop/Sponky/SP languaje/data/user.json", "r") as f:
      user = json.load(f)
    
    reg = user['registered']

    if reg == False:
      user['registered'] = True

      with open(logi+"/Desktop/Sponky/SP languaje/data/user.json", "w") as f:
        json.dump(user, f)

      return False
    elif reg == True:
      return True

check = Check