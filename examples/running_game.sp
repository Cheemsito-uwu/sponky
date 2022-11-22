run(console)
run(sys)
run(init)

func game()
    var game_over = false;
    var points = 0;
    var x = 12
    var y = 5

    while not game_over then 
        gotoxy(x, y)
        print("*")

        if game.is_pressed("a") then
            var x = x - 1
        elif game.is_pressed("d") then 
            var x = x + 1
        elif game.is_pressed("s") then
            var y = y + 1
        elif game.is_pressed("w") then 
            var y = y - 1
        else
            null
        end

        gotoxy(x, y)
        print(" ")
    end
end

game()