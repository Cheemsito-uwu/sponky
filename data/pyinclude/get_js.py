import js2py
import os

##########################

def file(gt_filename):
    userlogin = os.getlogin()
    filename = "C:/Users/" + userlogin + "/Desktop/Sponky/SP languaje/data/js-scripts/" + gt_filename

    return js2py.run_file(filename)

def create_code(code):
    return js2py.eval_js(code)