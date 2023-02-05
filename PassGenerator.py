from tkinter import*
import customtkinter
import sys
import secrets
import string

#Main Window
root=customtkinter.CTk()
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
root.title("Password Generator")
root.minsize(400,300)

# Password Generator Function
def passgen():
    # secure random string
    l = pass_len.get()
    n=int(l)
    # secure password
    password = "".join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(n)))
    # Clear txtbox
    pass_show.configure(state="normal")
    pass_show.delete("0.0", END)
    # Insert password
    pass_show.insert("0.0",password)
    pass_show.configure(state="disabled")


# Copy To Clipboard Function
def clipboard():
    # Clear the clipboard
	root.clipboard_clear()
	# Copy to clipboard
	root.clipboard_append(pass_show.get("0.0","end"))
    

# Create Frame
frame_txt=customtkinter.CTkFrame(master=root,corner_radius=10)
frame_txt.pack(pady=20,padx=20)

# Lenght Entry Box
pass_len= customtkinter.CTkEntry(master=frame_txt,
                               placeholder_text="Enter Charecter Length",
                               width=300,
                               height=40,
                               font=("Consolas",20),
                               corner_radius=10)

pass_len.grid(row=1,column=0,columnspan=2,pady=20, padx=20)

# Output Box
pass_show=customtkinter.CTkTextbox(frame_txt,font=("Consolas",20),text_color="gray",bg_color="transparent",width=300, height=20)
pass_show.grid(row=2,column=0,columnspan=2, pady=20, padx=20)
pass_show.configure(state="disabled")

# Generate Button
gen_bt=customtkinter.CTkButton(master=frame_txt,
                                 width=120,
                                 height=40,
                                 border_width=0,
                                 corner_radius=10,
                                 fg_color="black",
                                 text="Generate Password",
                                 command=passgen)
gen_bt.grid(row=3,column=0,padx=20,pady=20)

# Create Copy Button
Copy_bt= customtkinter.CTkButton(master=frame_txt,
                                 width=120,
                                 height=40,
                                 border_width=0,
                                 corner_radius=10,
                                 text="Copy to clipboard",
                                 fg_color="black",
                                 command=clipboard)
Copy_bt.grid(row=3,column=1,padx=20,pady=20)

root.mainloop()
