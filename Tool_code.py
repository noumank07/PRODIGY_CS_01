import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title("Ceaser Cipher Encyption and Decyption")
window.geometry("400x550")

def encrypt():
    encrypted_text = ""
    for char in plainenter.get():
        if char.isalpha():
            shifted = ord(char) + int(shiftenter.get())
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    label3["text"]=("Encrypted_text is ",encrypted_text )
    label3.config(fg="#451b07",bg="#d4c2ba")
    # Clear entry fields after encryption
    plainenter.delete(0, 'end')
    shiftenter.delete(0, 'end')



def decrypt():
    decrypted_text = ""
    for char in cipherenter.get():
        if char.isalpha():
            shifted = ord(char) - int(shiftdec.get())
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    label3["text"]=("Decrypted_text is ",decrypted_text )
    label3.config(fg="#451b07",bg="#d4c2ba")
    # Clear entry fields after decryption
    cipherenter.delete(0, 'end')
    shiftdec.delete(0, 'end')

head=tk.Label(window,text="Ceaser Cipher", font=("helvetica", 15, "bold"),fg="#530B1C")
head.pack()

label=tk.Label(window,text="Plain text", font=("helvetica", 10, "bold"),fg="#4E0B53")
label.pack(padx=10,pady=5)

plainenter=tk.Entry(window, relief="solid")
plainenter.pack(padx=2,pady=2)

label=tk.Label(window,text="Shift", font=("helvetica", 10, "bold"),fg="#4E0B53")
label.pack(padx=1,pady=1)
shiftenter=tk.Entry(window, relief="solid")
shiftenter.pack(padx=2,pady=2)

button=tk.Button(window, text="Encrypt", bg="#C0D0C9",command=encrypt)
button.pack(padx=2,pady=2)

label=tk.Label(window,text="Cipher text",font=("helvetica", 10, "bold"),fg="#4E0B53")
label.pack(padx=10,pady=5)

cipherenter=tk.Entry(window, relief="solid")
cipherenter.pack(padx=2,pady=2)

label=tk.Label(window,text="Shift", font=("helvetica", 10, "bold"),fg="#4E0B53")
label.pack()
shiftdec=tk.Entry(window, relief="solid")
shiftdec.pack(padx=2,pady=2)

button1=tk.Button(window, text="Decrypt", bg="#C0D0C9", command=decrypt)
button1.pack()

#create one label to show the result instead of message boxes.

label3=tk.Label(window,font=("helvetica", 10,"bold"))
label3.pack(padx=50,pady=50)

window.mainloop()
