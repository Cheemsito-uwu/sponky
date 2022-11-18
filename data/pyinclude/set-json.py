import time
import set
import random as rand

yes = [
    'y',
    'ye',
    'yes',
    'Yes',
    'YEs',
    'YES',
    'YE',
    'Y'
]

def main():
    print("Do you want to reset json requirements?")
    print("Proceed? (y/n)")
    select = input()

    if any(word in select for word in yes):
        int_value = str (rand.randint(2, 4))
        floating_value = str (rand.randint(1, 9))

        value_ = str(int_value+"."+floating_value)
        value = float(value_)

        time.sleep(value)
        set.location()
        print("Reestarting 'runs.json'")

        time.sleep(value-.4)
        print("Reestarting 'user.json'")

        time.sleep(value-.9)
        print("Reestarting 'words.json'")

        time.sleep(value-.6)
        print("From ../../.vscode ->")
        time.sleep(value-2.0)
        print("                 launch.json")
        time.sleep(value-.5)
        print("                 settings.json")
        
        time.sleep(value)
        print("\nEverything was reloaded succesfully!")
        input("Press any key to close...")
    else:
        pass

main()