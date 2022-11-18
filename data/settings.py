from pyinclude import config_settings as config

import tkinter as tk
import tkinter.font as tkFont
import os

class App:
    def __init__(self, root):
        #setting title
        self.root = root
        root.title("Sponky Language configurator")
        #setting window size
        width=826
        height=498
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.iconbitmap('C:/Users/' + os.getlogin() + '/Desktop/Sponky/SP languaje/data/res/settings-img.ico')

        GMessage_741=tk.Message(root)
        ft = tkFont.Font(family='sans-serif',size=32)
        GMessage_741["font"] = ft
        GMessage_741["fg"] = "#333333"
        GMessage_741["text"] = "Sponky config"
        GMessage_741.place(x=70,y=40,width=738,height=97)

        GButton_423=tk.Button(root)
        GButton_423["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='sans-serif',size=15)
        GButton_423["font"] = ft
        GButton_423["fg"] = "#000000"
        GButton_423["justify"] = "center"
        GButton_423["text"] = "Information"
        GButton_423.place(x=130,y=180,width=180,height=50)
        GButton_423["command"] = self.GButton_423_command

        GButton_368=tk.Button(root)
        GButton_368["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='sans-serif',size=15)
        GButton_368["font"] = ft
        GButton_368["fg"] = "#000000"
        GButton_368["justify"] = "center"
        GButton_368["text"] = "Uninstall program"
        GButton_368.place(x=340,y=180,width=180,height=50)
        GButton_368["command"] = self.GButton_368_command

        GButton_567=tk.Button(root)
        GButton_567["bg"] = "#ef9898"
        ft = tkFont.Font(family='sans-serif',size=10)
        GButton_567["font"] = ft
        GButton_567["fg"] = "#030000"
        GButton_567["justify"] = "center"
        GButton_567["text"] = "Quit"
        GButton_567.place(x=690,y=440,width=70,height=25)
        GButton_567["command"] = self.GButton_567_command

        GButton_539=tk.Button(root)
        GButton_539["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='sans-serif',size=15)
        GButton_539["font"] = ft
        GButton_539["fg"] = "#000000"
        GButton_539["justify"] = "center"
        GButton_539["text"] = "Advanced settings"
        GButton_539.place(x=340,y=260,width=180,height=50)
        GButton_539["command"] = self.GButton_539_command

        GButton_406=tk.Button(root)
        GButton_406["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='sans-serif',size=15)
        GButton_406["font"] = ft
        GButton_406["fg"] = "#000000"
        GButton_406["justify"] = "center"
        GButton_406["text"] = "Data"
        GButton_406.place(x=130,y=260,width=180,height=50)
        GButton_406["command"] = self.GButton_406_command

        GButton_882=tk.Button(root)
        GButton_882["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='sans-serif',size=15)
        GButton_882["font"] = ft
        GButton_882["fg"] = "#000000"
        GButton_882["justify"] = "center"
        GButton_882["text"] = "Reinstall program"
        GButton_882.place(x=550,y=180,width=180,height=50)
        GButton_882["command"] = self.GButton_882_command

        GButton_464=tk.Button(root)
        GButton_464["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='sans-serif',size=15)
        GButton_464["font"] = ft
        GButton_464["fg"] = "#000000"
        GButton_464["justify"] = "center"
        GButton_464["text"] = "Libraries configuration"
        GButton_464.place(x=550,y=260,width=180,height=50)
        GButton_464["command"] = self.GButton_464_command

        GButton_49=tk.Button(root)
        GButton_49["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='sans-serif',size=15)
        GButton_49["font"] = ft
        GButton_49["fg"] = "#000000"
        GButton_49["justify"] = "center"
        GButton_49["text"] = "Examples"
        GButton_49.place(x=130,y=340,width=180,height=50)
        GButton_49["command"] = self.GButton_49_command

        GButton_450=tk.Button(root)
        GButton_450["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='sans-serif',size=15)
        GButton_450["font"] = ft
        GButton_450["fg"] = "#000000"
        GButton_450["justify"] = "center"
        GButton_450["text"] = "Set"
        GButton_450.place(x=340,y=340,width=181,height=50)
        GButton_450["command"] = self.GButton_450_command

        GButton_12=tk.Button(root)
        GButton_12["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='sans-serif',size=15)
        GButton_12["font"] = ft
        GButton_12["fg"] = "#000000"
        GButton_12["justify"] = "center"
        GButton_12["text"] = "Information / Help"
        GButton_12.place(x=550,y=340,width=180,height=50)
        GButton_12["command"] = self.GButton_12_command

    # Iformation btn
    def GButton_423_command(self):
        self.root.quit()

        def info():
            def create(roota):
                #setting title
                roota.title("undefined")
                #setting window size
                width=826
                height=498
                screenwidth = roota.winfo_screenwidth()
                screenheight = roota.winfo_screenheight()
                alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                roota.geometry(alignstr)
                roota.resizable(width=False, height=False)

                GButton_58=tk.Button(roota)
                GButton_58["bg"] = "#f0f0f0"
                ft = tkFont.Font(family='Times',size=10)
                GButton_58["font"] = ft
                GButton_58["fg"] = "#000000"
                GButton_58["justify"] = "center"
                GButton_58["text"] = "&lt;- Back"
                GButton_58.place(x=10,y=10,width=100,height=30)
                GButton_58["command"] = GButton_58_command

                GLabel_588=tk.Label(roota)
                ft = tkFont.Font(family='Times',size=30)
                GLabel_588["font"] = ft
                GLabel_588["fg"] = "#333333"
                GLabel_588["justify"] = "center"
                GLabel_588["text"] = "Information"
                GLabel_588.place(x=300,y=60,width=235,height=92)

                GMessage_124=tk.Message(roota)
                ft = tkFont.Font(family='Times',size=16)
                GMessage_124["font"] = ft
                GMessage_124["fg"] = "#333333"
                GMessage_124["justify"] = "center"
                GMessage_124["text"] = "Version"
                GMessage_124.place(x=210,y=160,width=116,height=30)

                GMessage_332=tk.Message(roota)
                ft = tkFont.Font(family='Times',size=16)
                GMessage_332["font"] = ft
                GMessage_332["fg"] = "#333333"
                GMessage_332["justify"] = "center"
                GMessage_332["text"] = "of"
                GMessage_332.place(x=300,y=160,width=39,height=30)

                GMessage_232=tk.Message(roota)
                ft = tkFont.Font(family='Times',size=16)
                GMessage_232["font"] = ft
                GMessage_232["fg"] = "#333333"
                GMessage_232["justify"] = "center"
                GMessage_232["text"] = "Sponky:"
                GMessage_232.place(x=330,y=160,width=87,height=30)

                GLineEdit_989=tk.Entry(roota)
                GLineEdit_989["borderwidth"] = "1px"
                ft = tkFont.Font(family='Times',size=16)
                GLineEdit_989["font"] = ft
                GLineEdit_989["fg"] = "#333333"
                GLineEdit_989["justify"] = "center"
                GLineEdit_989["text"] = "0.6.7"
                GLineEdit_989.place(x=420,y=160,width=93,height=30)

                GLabel_922=tk.Label(roota)
                ft = tkFont.Font(family='Times',size=30)
                GLabel_922["font"] = ft
                GLabel_922["fg"] = "#333333"
                GLabel_922["justify"] = "center"
                GLabel_922["text"] = "About"
                GLabel_922.place(x=190,y=220,width=310,height=58)

                GLabel_543=tk.Label(roota)
                ft = tkFont.Font(family='Times',size=30)
                GLabel_543["font"] = ft
                GLabel_543["fg"] = "#333333"
                GLabel_543["justify"] = "center"
                GLabel_543["text"] = "Language"
                GLabel_543.place(x=380,y=230,width=197,height=36)

                GMessage_489=tk.Message(roota)
                ft = tkFont.Font(family='Times',size=18)
                GMessage_489["font"] = ft
                GMessage_489["fg"] = "#333333"
                GMessage_489["justify"] = "center"
                GMessage_489["text"] = "Reserved"
                GMessage_489.place(x=180,y=280,width=112,height=57)

                GMessage_976=tk.Message(roota)
                ft = tkFont.Font(family='Times',size=18)
                GMessage_976["font"] = ft
                GMessage_976["fg"] = "#333333"
                GMessage_976["justify"] = "center"
                GMessage_976["text"] = "Words"
                GMessage_976.place(x=250,y=290,width=136,height=41)

                GMessage_465=tk.Message(roota)
                ft = tkFont.Font(family='Times',size=10)
                GMessage_465["font"] = ft
                GMessage_465["fg"] = "#dd1054"
                GMessage_465["justify"] = "center"
                GMessage_465["text"] = "var"
                GMessage_465.place(x=110,y=330,width=52,height=30)

                GMessage_374=tk.Message(roota)
                ft = tkFont.Font(family='Times',size=10)
                GMessage_374["font"] = ft
                GMessage_374["fg"] = "#dd1054"
                GMessage_374["justify"] = "center"
                GMessage_374["text"] = "const"
                GMessage_374.place(x=120,y=320,width=127,height=51)

                GMessage_247=tk.Message(roota)
                ft = tkFont.Font(family='Times',size=10)
                GMessage_247["font"] = ft
                GMessage_247["fg"] = "#dd1054"
                GMessage_247["justify"] = "center"
                GMessage_247["text"] = "func"
                GMessage_247.place(x=190,y=330,width=88,height=32)

                GMessage_769=tk.Message(roota)
                ft = tkFont.Font(family='Times',size=18)
                GMessage_769["font"] = ft
                GMessage_769["fg"] = "#333333"
                GMessage_769["justify"] = "center"
                GMessage_769["text"] = "Built-in "
                GMessage_769.place(x=470,y=300,width=80,height=25)

                GMessage_207=tk.Message(roota)
                ft = tkFont.Font(family='Times',size=10)
                GMessage_207["font"] = ft
                GMessage_207["fg"] = "#333333"
                GMessage_207["justify"] = "center"
                GMessage_207["text"] = "Message"
                GMessage_207.place(x=550,y=300,width=80,height=25)

            def GButton_58_command():
                print(":v")

        aroot = tk.Tk()
        info(aroot)
        aroot.mainloop()


    def GButton_368_command(self):
        print("command")

    # quit button
    def GButton_567_command(self):
        self.root.quit()


    def GButton_539_command(self):
        print("command")


    def GButton_406_command(self):
        print("command")


    def GButton_882_command(self):
        print("command")


    def GButton_464_command(self):
        print("command")


    def GButton_49_command(self):
        print("command")


    def GButton_450_command(self):
        print("command")


    def GButton_12_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
