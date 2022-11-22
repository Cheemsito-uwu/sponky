run(init)
run(files)
run(sys)

func xd(option) {
    if option == 1 { 
        print("1")
    elif option == 2:
        print("Hello world :D")
        print("Xd")
        return
    }
}

if strequal(sp.name, sp.main) {
    if file.exists("shell.py") {
        print(xd(2))
    else
        xd(1)
    }
}

for i = 0 to 3 {
    print(system("blue"))
    print(i)
}