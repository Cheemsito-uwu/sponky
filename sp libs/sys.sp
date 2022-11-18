run(interpreter)
run(files)

func system(command)
    if strequal(command, "cls") then
        cls();
    elif strequal(command, "pause") then
        print("Press any key to continue");
        input();
    elif strequal(command, "pause>null") then
        input();
    else
        #RTError("system(command) ->: Sorry, but the '" + command + "' command does not exists in the 'system(command)' functoon")
        if is_str(command) then
            return fread(command)
        elif is_num(command) or is_list(command) or is_fun(command) then
            return ">>> Error (no description)"
        else
            return null
        end
    end
end

func wait(time_)
    var float = 352.06
    var float = float * 10
    var time = time_ * float
    var make = 0

    while make < time then
        var make = make + 1
    end
end