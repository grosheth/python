from tkinter import *
import string
import tkinter as ttk
import random
  
def generate_password():
    """generate_password

    Args:
        characters (list): Liste avec tout les characters
        numbers (list): Liste des nombres
        punct (list): Liste de ponctuation
    
    Returns:
        password: Un string
    """
    try:
        pass_list = []
        characters, numbers, punct = list(string.ascii_letters), list(string.digits), list(string.punctuation)
        characters.extend(punct)
        characters.extend(numbers)
        lgt = int(length.get())

        for _ in range(int(lgt)):
            pass_list.extend(characters[random.randint(0,len(characters))])

        password = ''.join(str(e) for e in pass_list)
        done.set(password)
    except IndexError:
        generate_password()
    except ValueError:
        pass

root = Tk()
root.title("Password Generator")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

length = StringVar()
length_entry = ttk.Entry(mainframe, width=7, textvariable=length)
length_entry.grid(column=2, row=1, sticky=(W, E))

done = StringVar()
ttk.Label(mainframe, textvariable=done).grid(column=2, row=2)
ttk.Button(mainframe, text="Generate password", command=generate_password).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="length").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="password").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

length_entry.focus()
root.bind("<Return>", generate_password)

root.mainloop()
