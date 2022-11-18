run(console)
run(sys)

func game()
    var game_over = false;
    var points = 0;
    var x = 12
    var y = 5

    while not game_over then 
        gotoxy(x, y)
        print("*")

        var key = input()

        if strequal(key, "a") == true then
            var x = x - 1
        elif strequal(key, "d") == true then 
            var x = x + 1
        elif strequal(key, "s") == true then
            var y = y + 1
        elif strequal(key, "w") == true then 
            var y = y - 1
        else
            null
        end

        gotoxy(x, y)
        print(" ")
    end
end

game()