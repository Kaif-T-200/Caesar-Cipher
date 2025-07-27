from tkinter import *
from tkinter import messagebox, filedialog

# MADE BY KAIF TARASAGAR
def encrypt(text, shift):
    result = ""
    for letter in text:
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            result += chr((ord(letter) - base + shift) % 26 + base)
        else:
            result += letter
    return result

# MADE BY KAIF TARASAGAR
def decrypt(text, shift):
    return encrypt(text, -shift)

def do_cipher():
    message = input_box.get("1.0", END).strip()
    try:
        shift = int(shift_entry.get())
        if shift < 0 or shift > 25:
            raise ValueError
    except:
        messagebox.showerror("Invalid Input", "Please enter a valid shift (0–25).")
        return

    if choice.get() == 1:
        result = encrypt(message, shift)
    else:
        result = decrypt(message, shift)

    result_box.delete("1.0", END)
    result_box.insert(END, result)
# MADE BY KAIF TARASAGAR
def reset_all():
    input_box.delete("1.0", END)
    shift_entry.delete(0, END)
    result_box.delete("1.0", END)
    choice.set(1)

# MADE BY KAIF TARASAGAR
def save_result():
    result = result_box.get("1.0", END).strip()
    if result == "":
        messagebox.showinfo("Empty", "Nothing to save.")
        return
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "w") as f:
            f.write(result)
        messagebox.showinfo("Saved", "Result saved successfully!")
# MADE BY KAIF TARASAGAR
def load_message():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "r") as f:
            data = f.read()
        input_box.delete("1.0", END)
        input_box.insert(END, data)

# MADE BY KAIF TARASAGAR
win = Tk()
win.title("Caesar Cipher")

Label(win, text="Enter Message:").grid(row=0, column=0, padx=10, pady=5, sticky=NW)
input_box = Text(win, height=4, width=40)
input_box.grid(row=0, column=1, padx=10, pady=5)

Label(win, text="Shift (0-25):").grid(row=1, column=0, padx=10, pady=5, sticky=W)
shift_entry = Entry(win)
shift_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)   # MADE BY KAIF TARASAGAR

choice = IntVar()
choice.set(1)
Radiobutton(win, text="Encrypt", variable=choice, value=1).grid(row=2, column=0, padx=10, pady=2, sticky=W)
Radiobutton(win, text="Decrypt", variable=choice, value=2).grid(row=2, column=1, padx=10, pady=2, sticky=W)
# MADE BY KAIF TARASAGAR
Button(win, text="Submit", command=do_cipher).grid(row=3, column=0, columnspan=2, pady=5)
Button(win, text="Reset", command=reset_all).grid(row=4, column=0, columnspan=2, pady=2)
Button(win, text="Save Result", command=save_result).grid(row=5, column=0, columnspan=2, pady=2)
Button(win, text="Load From File", command=load_message).grid(row=6, column=0, columnspan=2, pady=2)

Label(win, text="Result:").grid(row=7, column=0, padx=10, pady=5, sticky=NW)
result_box = Text(win, height=4, width=40)
result_box.grid(row=7, column=1, padx=10, pady=5)

win.mainloop()


                                            #-- MADE BY KAIF TARASAGAR 
                                               
                                             # https://www.linkedin.com/in/kaif-tarasgar-0b5425326/
                                              
                                             # https://x.com/Kaif_T_200 