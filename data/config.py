import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Sp config")
        #setting window size
        width=838
        height=497
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        font = 'sans-serif'
        GLabel_139=tk.Label(root)
        ft = tkFont.Font(family=font,size=27)
        GLabel_139["font"] = ft
        GLabel_139["fg"] = "#333333"
        GLabel_139["justify"] = "center"
        GLabel_139["text"] = "Sponky"
        GLabel_139.place(x=180,y=70,width=321,height=56)

        GLabel_743=tk.Label(root)
        ft = tkFont.Font(family=font,size=27)
        GLabel_743["font"] = ft
        GLabel_743["fg"] = "#333333"
        GLabel_743["justify"] = "center"
        GLabel_743["text"] = "Configuration"
        GLabel_743.place(x=420,y=80,width=164,height=44)

        GButton_12=tk.Button(root)
        GButton_12["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=font,size=10)
        GButton_12["font"] = ft
        GButton_12["fg"] = "#000000"
        GButton_12["justify"] = "center"
        GButton_12["text"] = "Uninstall program"
        GButton_12.place(x=110,y=180,width=211,height=31)
        GButton_12["command"] = self.GButton_12_command

        self.entry = tk.Entry(root)
        self.installed_in = self.entry.get()
        self.entry["borderwidth"] = "1px"
        ft = tkFont.Font(family=font,size=10)
        self.entry["font"] = ft
        self.entry["fg"] = "#333333"
        self.entry["justify"] = "center"
        self.entry["text"] = "Selected installation place"
        self.entry.place(x=440,y=200,width=358,height=30)

        GLabel_722=tk.Label(root)
        GLabel_722["activebackground"] = "#000000"
        GLabel_722["activeforeground"] = "#000000"
        ft = tkFont.Font(family=font,size=10)
        GLabel_722["font"] = ft
        GLabel_722["fg"] = "#333333"
        GLabel_722["justify"] = "center"
        GLabel_722["text"] = ""
        GLabel_722.place(x=400,y=170,width=30,height=270)

        GLabel_764=tk.Label(root)
        ft = tkFont.Font(family=font,size=13)
        GLabel_764["font"] = ft
        GLabel_764["fg"] = "#333333"
        GLabel_764["justify"] = "center"
        GLabel_764["text"] = "You installed sponky in:"
        GLabel_764.place(x=510,y=160,width=209,height=30)

        GButton_446=tk.Button(root)
        GButton_446["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=font,size=10)
        GButton_446["font"] = ft
        GButton_446["fg"] = "#000000"
        GButton_446["justify"] = "center"
        GButton_446["text"] = "Reinstall Sponky"
        GButton_446.place(x=110,y=230,width=211,height=30)
        GButton_446["command"] = self.GButton_446_command

        GButton_285=tk.Button(root)
        GButton_285["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=font,size=10)
        GButton_285["font"] = ft
        GButton_285["fg"] = "#000000"
        GButton_285["justify"] = "center"
        GButton_285["text"] = "Help"
        GButton_285.place(x=110,y=280,width=211,height=30)
        GButton_285["command"] = self.GButton_285_command

        GButton_719=tk.Button(root)
        GButton_719["bg"] = "#dd9696"
        ft = tkFont.Font(family=font,size=10)
        GButton_719["font"] = ft
        GButton_719["fg"] = "#000000"
        GButton_719["justify"] = "center"
        GButton_719["text"] = "Quit"
        GButton_719.place(x=160,y=390,width=105,height=30)
        GButton_719["command"] = self.GButton_719_command

        GButton_366=tk.Button(root)
        GButton_366["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=font,size=10)
        GButton_366["font"] = ft
        GButton_366["fg"] = "#000000"
        GButton_366["justify"] = "center"
        GButton_366["text"] = "Close and open in console"
        GButton_366.place(x=110,y=330,width=212,height=30)
        GButton_366["command"] = self.GButton_366_command

        GButton_279=tk.Button(root)
        GButton_279["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=font,size=10)
        GButton_279["font"] = ft
        GButton_279["fg"] = "#000000"
        GButton_279["justify"] = "center"
        GButton_279["text"] = "Save changes"
        GButton_279.place(x=680,y=430,width=130,height=30)
        GButton_279["command"] = self.GButton_279_command

        GButton_391=tk.Button(root)
        GButton_391["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=font,size=10)
        GButton_391["font"] = ft
        GButton_391["fg"] = "#000000"
        GButton_391["justify"] = "center"
        GButton_391["text"] = "Discard changes"
        GButton_391.place(x=540,y=430,width=130,height=30)
        GButton_391["command"] = self.GButton_391_command

        GRadio_742=tk.Radiobutton(root)
        ft = tkFont.Font(family=font,size=10)
        GRadio_742["font"] = ft
        GRadio_742["fg"] = "#333333"
        GRadio_742["justify"] = "center"
        GRadio_742["text"] = "English"
        GRadio_742.place(x=580,y=310,width=85,height=25)
        GRadio_742["command"] = self.GRadio_742_command

        GLabel_362=tk.Label(root)
        ft = tkFont.Font(family=font,size=13)
        GLabel_362["font"] = ft
        GLabel_362["fg"] = "#333333"
        GLabel_362["justify"] = "center"
        GLabel_362["text"] = "Language"
        GLabel_362.place(x=550,y=280,width=143,height=30)

    # Uninstall program btn
    def GButton_12_command(self):
        print("command")

    # Reinstall program btn
    def GButton_446_command(self):
        print("command")

    # Help btn
    def GButton_285_command(self):
        print("command")

    # Quit btn
    def GButton_719_command(self):
        print("command")

    # Close and open console btn
    def GButton_366_command(self):
        print("command")


    # Save changes btn
    def GButton_279_command(self):
        print(self.installed_in)

    # Discard changes btn
    def GButton_391_command(self):
        self.entry.insert(0, 'Installed-in...')

    # English (the only one :v)
    def GRadio_742_command(self):
        print("command")

def opn():
    root = tk.Tk()
    app = App(root)
    root.mainloop()