import tkinter
import customtkinter as ctk
import PIL as pil
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 
root = ctk.CTk()
root.title("Password generator")
root.geometry("700x500")
root.minsize(700, 500)
root.maxsize(700, 500)    

#functions
def randompass():
    pass

def start():
    pass

def quit():
    pass

def tutorial():
    pass

def enter():
    pass

def copy():
    pass

#labels
MainMenu_label = ctk.CTkLabel(master= root,
                              text = "Password generator",
                              text_color = "white",
                              fg_color= "#01a6f8",
                              width= 200,
                              height= 25,
                              font=("Bold", 20),
                              corner_radius= 5)
MainMenu_label.pack(padx = 10,
                    pady = 10)

#Frames
MainMenu_sideFrame1 = ctk.CTkFrame(master= root, 
                                   fg_color="gray")
MainMenu_sideFrame1.pack(side = "right", 
                         padx = 20, 
                         pady = 20)

MainMenu_sideFrame2 = ctk.CTkFrame(master= root, 
                                   fg_color="gray")
MainMenu_sideFrame2.pack(side= "right", 
                         padx = 10, 
                         pady = 10)

MainMenu_Mainframe = ctk.CTkFrame(master= root,
                                  fg_color="gray",
                                  width = 500)
MainMenu_Mainframe.pack(side = "left",
                        padx = 20,
                        pady = 20,
                        fill = "both")

#buttons
randompass_btn = ctk.CTkButton(master= MainMenu_sideFrame1, 
                               text="random password", 
                               command=randompass)
randompass_btn.pack(pady = 10, 
                    padx = 10)

start_btn = ctk.CTkButton(master= MainMenu_sideFrame1, 
                          text="start", 
                          command=start)
start_btn.pack(pady = 10, 
               padx = 10)

quit_btn = ctk.CTkButton(master= MainMenu_sideFrame1, 
                         text="quit", 
                         command=quit)
quit_btn.pack(pady = 10, 
              padx = 10)

tutorial_btn = ctk.CTkButton(master= MainMenu_sideFrame1, 
                             text="tutorial", 
                             command=tutorial)
tutorial_btn.pack(pady = 10, 
                  padx = 10)

copy_btn = ctk.CTkButton(master= MainMenu_sideFrame2, 
                         text="copy", 
                         command=copy,
                         width = 10)
copy_btn.pack(pady = 5,
              padx = 5)

enter_btn = ctk.CTkButton(master= MainMenu_sideFrame2, 
                          text="Enter", 
                          command=enter,
                          width = 10)
enter_btn.pack(pady = 5, 
               padx = 5)




root.mainloop()