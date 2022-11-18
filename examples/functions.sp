var c = ""
var c = "# Using functions in Sp!"
var c = "# The functions are very useful to store commands and execute them!"
var c = "# You can use the functions everywere, the syntax is:"
var c = "#     func name(parameter)"
var c = "#         your code"
var c = "#     end"
var c = "# Here you have an example:"
func code()
    print("This is a code!")

    if 1 == 1 then
        print("This is a condition!")
    end
end

var c = "# You can also add parameters to the function to make it more useful"
var c = "# in your code or in anyone's else code"
var c = "# Here you have an example, this function can multiply to 4"
var c = "# any number, just have to put it in the parameters"
func multi_four(number)
    var result = number * 4
    return result
end

var c = "# And the last useful thing about functions"
var c = "# Functions can be just returning a value automatecly or just to return another"
var c = "# function with different parameters to make easier the code"
var c = "# Just use the '->', here's an exmaple"
func write_line(text) -> print(text)
func mult_four(number) -> number * 4


var c = "# And this is for just calling the functions"
code()

var c = "# Now you can save and print returning functions"
var function = multi_four(3)

print(function)
print(mult_four(4))