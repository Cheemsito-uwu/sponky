func sqrt(num) -> sp4math("sqrt", num, null, null)
func hypotenuse(num1, num2) -> sp4math("hypotenuse", num1, num2, null)
func hyp(num1, num2) -> hypotenuse(num1, num2)
func calculate(things) -> sp4math("calculate", things, null, null)

var math.e = 2.718281828448904
var math.pi = math_pi

func math.abs(num)
    if num < 0 then 
        var res = num - num - num
        return res
    else
        var res = num - num - num
        return res
    end
end

func pow(num, pot)
    var result = num

    for i = 1 to pot then
        var result = result * num
    end

    return result
end

func concat(num, plus)
    var num = num + plus
    return num
end

func plus(num)
    var num = num + 1
    return num
end

func random(num_since, num_to)
    var times = num_to
    var number = 0

    for i = 1 to times - num_since then
        var adding = rand()

        if adding > num_to then
            break
        else
            var number = adding + number
        end
    end

    var rand_num = number + num_since
    return rand_num
end