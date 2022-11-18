func printint(value) -> print(value)
func gotoxy(x, y) -> po1cons(y, x)
func RTError(details) -> er3inte("RTError", details)
func IllegalCharError(details) -> er3inte("IllegalCharError", details)
func ExpectedCharError(details) -> er3inte("ExpectedCharError", details)
func InvalidSyntaxError(detail) -> er3inte("InvalidSyntaxError", detail)

func printbool(value)
    if value == true then
        print("true")
    elif value == false then
        print("false")
    elif value == null then
        print("null")
    end
end

