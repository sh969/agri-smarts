import tkinter as tk
import sys

HEIGHT = 200
WIDTH = 400

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

def exitApp():
   print("Bye bye...")
   sys.exit()


# create tk object
root = tk.Tk()
root.attributes("-fullscreen", True)

# # create canvas in specified size
# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# canvas.pack()

# add frame
frame = tk.Frame(root, bg="#80c1ff")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# add text
text = tk.Text(frame)
text.insert(tk.INSERT, "Hello...")
text.insert(tk.END, "Bye Bye.....")
text.pack()

# add button with function
button = tk.Button(root, text="Exit", command=exitApp)
button.pack()

# run the gui loop
root.mainloop()