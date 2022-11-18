func create_window(title, size, color) -> wn1wind(title, size, color)
func add(type, text, id) -> ad1wind(type, text, id)

func add_button(text, id) -> ad1wind("button", text, id)
func add_label(text, id) -> ad1wind("label", text, id)

func button_place(x, y) -> po1wind("button", x, y)
func label_place(x, y) -> po1wind("label", x, y)
func on_click(button_id) -> co1wind(button_id)