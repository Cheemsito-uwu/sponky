from data import *

class BuiltInFunction(BaseFunction):
  def __init__(self, name):
    super().__init__(name)

  def execute(self, args):
    res = RTResult()
    exec_ctx = self.generate_new_context()

    method_name = f'execute_{self.name}'
    method = getattr(self, method_name, self.no_visit_method)

    res.register(self.check_and_populate_args(method.arg_names, args, exec_ctx))
    if res.should_return(): return res

    return_value = res.register(method(exec_ctx))
    if res.should_return(): return res
    return res.success(return_value)
  
  def no_visit_method(self, node, context):
    raise Exception(f'No execute_{self.name} method defined')

  def copy(self):
    copy = BuiltInFunction(self.name)
    copy.set_context(self.context)
    copy.set_pos(self.pos_start, self.pos_end)
    return copy

  def __repr__(self):
    return f"<built-in function {self.name}>"

  #####################################

  def execute_print(self, exec_ctx):
    print(str(exec_ctx.symbol_table.get('value')))
    return RTResult().success(Number.null)
  execute_print.arg_names = ['value']
  
  def execute_print_ret(self, exec_ctx):
    return RTResult().success(String(str(exec_ctx.symbol_table.get('value'))))
  execute_print_ret.arg_names = ['value']
  
  def execute_input(self, exec_ctx):
    text = input()
    return RTResult().success(String(text))
  execute_input.arg_names = []

  def execute_input_int(self, exec_ctx):
    while True:
      text = input()
      try:
        number = int(text)
        break
      except ValueError:
        print(f"'{text}' must be an integer. Try again!")
    return RTResult().success(Number(number))
  execute_input_int.arg_names = []

  def execute_clear(self, exec_ctx):
    os.system('cls' if os.name == 'nt' else 'cls') 
    return RTResult().success(Number.null)
  execute_clear.arg_names = []

  def execute_is_number(self, exec_ctx):
    is_number = isinstance(exec_ctx.symbol_table.get("value"), Number)
    return RTResult().success(Number.true if is_number else Number.false)
  execute_is_number.arg_names = ["value"]

  def execute_is_string(self, exec_ctx):
    is_number = isinstance(exec_ctx.symbol_table.get("value"), String)
    return RTResult().success(Number.true if is_number else Number.false)
  execute_is_string.arg_names = ["value"]

  def execute_is_list(self, exec_ctx):
    is_number = isinstance(exec_ctx.symbol_table.get("value"), List)
    return RTResult().success(Number.true if is_number else Number.false)
  execute_is_list.arg_names = ["value"]

  def execute_is_function(self, exec_ctx):
    is_number = isinstance(exec_ctx.symbol_table.get("value"), BaseFunction)
    return RTResult().success(Number.true if is_number else Number.false)
  execute_is_function.arg_names = ["value"]

  def execute_append(self, exec_ctx):
    list_ = exec_ctx.symbol_table.get("list")
    value = exec_ctx.symbol_table.get("value")

    if not isinstance(list_, List):
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        "First argument must be list",
        exec_ctx
      ))

    list_.elements.append(value)
    return RTResult().success(Number.null)
  execute_append.arg_names = ["list", "value"]

  def execute_pop(self, exec_ctx):
    list_ = exec_ctx.symbol_table.get("list")
    index = exec_ctx.symbol_table.get("index")

    if not isinstance(list_, List):
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        "First argument must be list",
        exec_ctx
      ))

    if not isinstance(index, Number):
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        "Second argument must be number",
        exec_ctx
      ))

    try:
      element = list_.elements.pop(index.value)
    except:
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        'Element at this index could not be removed from list because index is out of bounds',
        exec_ctx
      ))
    return RTResult().success(element)
  execute_pop.arg_names = ["list", "index"]

  def execute_extend(self, exec_ctx):
    listA = exec_ctx.symbol_table.get("listA")
    listB = exec_ctx.symbol_table.get("listB")

    if not isinstance(listA, List):
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        "First argument must be list",
        exec_ctx
      ))

    if not isinstance(listB, List):
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        "Second argument must be list",
        exec_ctx
      ))

    listA.elements.extend(listB.elements)
    return RTResult().success(Number.null)
  execute_extend.arg_names = ["listA", "listB"]

  def execute_len(self, exec_ctx):
    list_ = exec_ctx.symbol_table.get("list")

    if not isinstance(list_, List):
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        "Argument must be list",
        exec_ctx
      ))

    return RTResult().success(Number(len(list_.elements)))
  execute_len.arg_names = ["list"]

  def execute_run(self, exec_ctx):
    fn = exec_ctx.symbol_table.get("fn")

    if not isinstance(fn, String):
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        "Second argument must be string",
        exec_ctx
      ))

    fn = fn.value

    try:
      with open(fn, "r") as f:
        script = f.read()
    except Exception as e:
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        f"Failed to load script \"{fn}\"\n" + str(e),
        exec_ctx
      ))

    _, error = run(fn, script)
    
    if error:
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        f"Failed to finish executing script \"{fn}\"\n" +
        error.as_string(),
        exec_ctx
      ))

    return RTResult().success(Number.null)
  execute_run.arg_names = ["fn"]

  def execute_make(self, exec_ctx):
    dir = str(exec_ctx.symbol_table.get('directory'))
    proj = str(exec_ctx.symbol_table.get('project_name'))

    # Code
  execute_make.arg_names = ["directory", "project_name"]

  def execute_rand(self, exec_ctx):
    num = rn.randint(0, 1)
    num = int(num)
    return RTResult().success(Number(num))
  execute_rand.arg_names = []

  def execute_use(self, exec_ctx):
    name = str(exec_ctx.symbol_table.get('name'))
    user = os.getlogin()

    if name == "sys":
      return RTResult().success(String("C:/Users/" + user + "/Desktop/Sponky/SP languaje/sp libs/sys.sp"))
    elif name == "math":
      return RTResult().success(String("C:/Users/" + user + "/Desktop/Sponky/SP languaje/sp libs/math.sp"))
    elif name == "console":
      return RTResult().success(String("C:/Users/" + user + "/Desktop/Sponky/SP languaje/sp libs/console.sp"))
    elif name == "files":
      return RTResult().success(String("C:/Users/" + user + "/Desktop/Sponky/SP languaje/sp libs/files.sp"))
    elif name == "init" or name == "wnd":
      return RTResult().success(String("C:/Users/" + user + "/Desktop/Sponky/SP languaje/sp libs/init.sp"))
  execute_use.arg_names = ["name"]

  def execute_pass(self, exec_ctx):
    return RTResult().success(Number.null)
  execute_pass.arg_names = []

  def execute_int(self, exec_ctx):
    thing = exec_ctx.symbol_table.get("thing")

    return RTResult().success(Number(thing))
  execute_int.arg_names = ["thing"]

  def execute_string(self, exec_ctx):
    obj = exec_ctx.symbol_table.get("obj")

    return RTResult().success(String(obj))
  execute_string.arg_names = ["obj"]


  # Files

  def execute_wf1daffl(self, exec_ctx):
    filename = str(exec_ctx.symbol_table.get('filename'))
    text = str(exec_ctx.symbol_table.get('text'))
    mode = str(exec_ctx.symbol_table.get('mode'))

    if mode == "a":
      f = open(filename, 'a')
      f.write(text)
      f.close()
    elif mode == "w":
      f = open(filename, 'w')
      f.write(text)
      f.close()
    elif mode == "x":
      if os.path.exists(filename):
        print(">>> The file was aleady created!")
      else:
        f = open(filename, 'x')
        f.write(text)
        f.close()
    else:
      print(">>> Can't understand the mode fopen(filename, text, >>mode<<)")
    
    return RTResult().success(Number.null)
  execute_wf1daffl.arg_names = ["filename", "text", "mode"]

  def execute_rf1daffl(self, exec_ctx):
    filename = str(exec_ctx.symbol_table.get('filename'))
    
    f = open(filename, 'r')
    filetext = f.read()
    return RTResult().success(String(filetext))
  execute_rf1daffl.arg_names = ["filename"]

  def execute_df1daffl(self, exec_ctx):
    filename = str(exec_ctx.symbol_table.get('filename'))

    if os.path.exists(filename):
      os.remove(filename)
    else:
      print(f">>> The file you especified ('{filename}') does not exist")

    return RTResult().success(Number.null)
  execute_df1daffl.arg_names = ["filename"]

  def execute_rnf1dffl(self, exec_ctx):
    filename = str(exec_ctx.symbol_table.get('filename'))
    new_name = str(exec_ctx.symbol_table.get('new_name'))

    if os.path.exists(filename):
      os.rename(filename, new_name)
    else:
      print(f">>> The file you especified ('{filename}') does not exist")

    return RTResult().success(Number.null)
  execute_rnf1dffl.arg_names = ["filename", "new_name"]

  def execute_wn1wind(self, exec_ctx):
    global window
    window = Tk()

    name = str(exec_ctx.symbol_table.get('name'))
    size = str(exec_ctx.symbol_table.get('size'))
    bg_color = str(exec_ctx.symbol_table.get('bg_color'))

    if bg_color != Number(0):
      window.geometry(size)
      window.title(name)
      window.config(background=bg_color)
    else:
      window.geometry(size)
      window.title(name)
      window.config(background="white")
    
    return RTResult().success(Number.null)
  execute_wn1wind.arg_names = [
    "name",
    "size",
    "bg_color"
  ]

  def execute_ad1wind(self, exec_ctx):
    type = str(exec_ctx.symbol_table.get('type'))
    text = str(exec_ctx.symbol_table.get('text'))

    if type == "button":
      global button
      button = Button(window, text=text)
      button.pack()
    elif type == "label":
      global label
      label = Label(window, text=text, font=('Arial', 12, 'bold'))
      label.pack()

    return RTResult().success(Number.null)
  execute_ad1wind.arg_names = ["type", "text"]

  def execute_po1wind(self, exec_ctx):
    type = str(exec_ctx.symbol_table.get('type'))
    x_ = str(exec_ctx.symbol_table.get('x'))
    y_ = str(exec_ctx.symbol_table.get('y'))

    x = int(x_)
    y = int(y_)

    if type == "button":
      button.place(x=x, y=y)
    elif type == "label":
      label.place(x=x, y=y)

    return RTResult().success(Number.null)
  execute_po1wind.arg_names = ["type", "x", "y"]

  def execute_po1cons(self, exec_ctx):
    x_ = str(exec_ctx.symbol_table.get('x'))
    y_ = str(exec_ctx.symbol_table.get('x'))

    x = int(x_)
    y = int(y_)
    print("%c[%d;%df" % (0x1B, y, x), end='')
    return RTResult().success(Number.null)
  execute_po1cons.arg_names = ["x", "y"]

  def execute_def(self, exec_ctx):
    if built != True:
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        f"This kind of data just can be used on built structures"
      ))

    number = str(exec_ctx.symbol_table.get('number'))
    number = int(number)

    global value
    global name
    global value1
    global name1
    global value2
    global name2
    global value3
    global name3
    global value4
    global name4
    global value5
    global name5
    global value6
    global name6
    global value7
    global name7
    global value8
    global name8
    global value9
    global name9

    if number == 1:
      one = True
      value = exec_ctx.symbol_table.get('value')
      name = str(exec_ctx.symbol_table.get('name'))
    elif number == 2:
      two = True
      value1 = exec_ctx.symbol_table.get('value')
      name1 = str(exec_ctx.symbol_table.get('name'))
    elif number == 3:
      three = True
      value2 = exec_ctx.symbol_table.get('value')
      name2 = str(exec_ctx.symbol_table.get('name'))
    elif number == 4:
      four = True
      value3 = exec_ctx.symbol_table.get('value')
      name3 = str(exec_ctx.symbol_table.get('name'))
    elif number == 5:
      five = True
      value4 = exec_ctx.symbol_table.get('value')
      name4 = str(exec_ctx.symbol_table.get('name'))
    elif number == 6:
      six = True
      value5 = exec_ctx.symbol_table.get('value')
      name5 = str(exec_ctx.symbol_table.get('name'))
    elif number == 7:
      seven = True
      value6 = exec_ctx.symbol_table.get('value')
      name6 = str(exec_ctx.symbol_table.get('name'))
    elif number == 8:
      eight = True
      value7 = exec_ctx.symbol_table.get('value')
      name7 = str(exec_ctx.symbol_table.get('name'))
    elif number == 9:
      nine = True
      value8 = exec_ctx.symbol_table.get('value')
      name8 = str(exec_ctx.symbol_table.get('name'))
    elif number == 10:
      ten = True
      value9 = exec_ctx.symbol_table.get('value')
      name9 = str(exec_ctx.symbol_table.get('name'))
    else:
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        "The id you provied to 'def' is not usable"
      ))

    return RTResult().success(Number.null)
  execute_def.arg_names = ["number", "this", "name", "value"]

  def execute_get(self, exec_ctx):
    this = str(exec_ctx.symbol_table.get('this'))

    if this == name: return RTResult().success(String(str(value)))
    if this == name1: return RTResult().success(String(str(value1)))
    if this == name2: return RTResult().success(String(str(value2)))
    if this == name3: return RTResult().success(String(str(value3)))
    if this == name4: return RTResult().success(String(str(value4)))
    if this == name5: return RTResult().success(String(str(value5)))
    if this == name6: return RTResult().success(String(str(value6)))
    if this == name7: return RTResult().success(String(str(value7)))
    if this == name8: return RTResult().success(String(str(value8)))
    if this == name9: return RTResult().success(String(str(value9)))
  execute_get.arg_names = ["this"]

  def execute_ge2keys(self, exec_ctx):
    pass
  execute_ge2keys.arg_names = ["key"]

  def execute_strequal(self, exec_ctx):
    str1 = str(exec_ctx.symbol_table.get('one'))
    str2 = str(exec_ctx.symbol_table.get('two'))

    if str1 != str2:
      return RTResult().success(Number(0))
    else:
      return RTResult().success(Number(1))
  execute_strequal.arg_names = ["one", "two"]

  def execute_er3inte(self, exec_ctx):
    type = str(exec_ctx.symbol_table.get('err_type'))
    det = str(exec_ctx.symbol_table.get('details'))

    if type == "RTError":
      return RTResult().failure(RTError(
        self.pos_start, self.pos_end,
        det
      ))
    elif type == "IllegalCharError":
      return RTResult().failure(IllegalCharError(
        self.pos_start, self.pos_end,
        det
      ))
    elif type == "ExpectedCharError":
      return RTResult().failure(ExpectedCharError(
        self.pos_start, self.pos_end,
        det
      ))
    elif type == "InvalidSyntaxError":
      return RTResult().failure(InvalidSyntaxError(
        self.pos_start, self.pos_end,
        det
      ))
    else:
      print(">>> Undefined or incorrect type of error")
  execute_er3inte.arg_names = ["err_type", "details"]