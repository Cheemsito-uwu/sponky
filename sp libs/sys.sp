run(files)

func system(command) {
    if strequal(command, "cls") {
        cls()
    elif strequal(command, "pause"):
        print("Press any key to continue")
        input()
    elif strequal(command, "pause>null"):
        input()

    # The system colors
    elif strequal(command, "blue"):
        return sp4math("just color", "[[blue]]", null, null)
    elif strequal(command, "white"):
        return sp4math("just color", "[[white]]", null, null)
    elif strequal(command, "red"):
        return sp4math("just color", "[[red]]", null, null)
    elif strequal(command, "green"):
        return sp4math("just color", "[[green]]", null, null)
    elif strequal(command, "yellow"):
        return sp4math("just color", "[[yellow]]", null, null)
    elif strequal(command, "magenta"):
        return sp4math("just color", "[[magenta]]", null, null)
    elif strequal(command, "black"):
        return sp4math("just color", "[[black]]", null, null)
    elif strequal(command, "blue"):
        return sp4math("just color", "[[blue]]", null, null)

    # If isn't any of the other ones
    else
        #RTError("system(command) ->: Sorry, but the '" + command + "' command does not exists in the 'system(command)' functoon")
        
        if is_str(command) {
            # This will execute a file if it is in your computer
            if(file.exists(command)) {
                return fread(command)
            }
        elif is_num(command) or is_list(command) or is_fun(command):
            return ">>> Error (no description)"
        else
            return null
        }
    }
}

func wait(time_) {
    var float = 352.06
    var float = float * 10
    var time = time_ * float
    var make = 0

    while make < time {
        var make = make + 1
    }
}