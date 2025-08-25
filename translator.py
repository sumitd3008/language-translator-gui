from tkinter import END, WORD, Tk, Label, Frame, Text, Button
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Create reverse mapping (values to keys) for languages
lang_dict = {value.title(): key for key, value in LANGUAGES.items()}


def change(text="type", src="English", dest="Hindi"):
    try:
        # Convert language names to codes
        src_code = lang_dict.get(src.title(), "en")
        dest_code = lang_dict.get(dest.title(), "en")

        trans = Translator()
        trans1 = trans.translate(text, src=src_code, dest=dest_code)
        return trans1.text
    except Exception as e:
        return f"Error: {str(e)}"


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END).strip()
    if not masg:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, "Please enter text to translate!")
        return
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


# Toggle between Light and Dark Modes
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()


def apply_theme():
    if dark_mode:
        # Dark Theme Colors
        bg_color = "#2C2C2C"
        fg_color = "#FFFFFF"
        btn_color = "#5A5A5A"
        entry_bg = "#3C3C3C"
        combobox_bg = "#3C3C3C"
    else:
        # Light Theme Colors
        bg_color = "#FFE4C4"
        fg_color = "#000000"
        btn_color = "#008080"
        entry_bg = "#FFFFFF"
        combobox_bg = "#FFFFFF"

    root.config(bg=bg_color)
    header_frame.config(bg=btn_color)
    header_label.config(bg=btn_color, fg=fg_color)
    src_label.config(bg=bg_color, fg=fg_color)
    dest_label.config(bg=bg_color, fg=fg_color)
    Sor_txt.config(bg=entry_bg, fg=fg_color)
    dest_txt.config(bg=entry_bg, fg=fg_color)
    translate_btn.config(bg=btn_color, fg=fg_color)
    theme_btn.config(bg=btn_color, fg=fg_color)

    style = ttk.Style()
    style.configure("TCombobox", fieldbackground=combobox_bg, background=combobox_bg, foreground=fg_color)


# Main Window
root = Tk()
root.title("Translator")
root.geometry("625x700")
root.resizable(False, False)

dark_mode = False

# Header
header_frame = Frame(root)
header_frame.place(relwidth=1, relheight=0.15)

header_label = Label(header_frame, text="Language Translator", font=("Arial", 28, "bold"))
header_label.place(relx=0.5, rely=0.5, anchor="center")

frame = Frame(root)
frame.pack(pady=10)

# Source Text
src_label = Label(frame, text="Source Text:", font=("Arial", 16, "bold"))
src_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

Sor_txt = Text(frame, font=("Arial", 14), wrap=WORD, height=8, width=40, bd=2, relief="groove")
Sor_txt.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

src_scroll = ttk.Scrollbar(frame, command=Sor_txt.yview)
src_scroll.grid(row=1, column=3, sticky="ns")
Sor_txt.config(yscrollcommand=src_scroll.set)

# Language Selection
languages = [lang.title() for lang in LANGUAGES.values()]

comb_sor = ttk.Combobox(frame, value=languages, font=("Arial", 12), state="readonly")
comb_sor.grid(row=2, column=0, padx=10, pady=5)
comb_sor.set("English")

translate_btn = Button(frame, text="Translate", font=("Arial", 14, "bold"), command=data, relief="raised", bd=3)
translate_btn.grid(row=2, column=1, padx=10, pady=5)

comb_dest = ttk.Combobox(frame, value=languages, font=("Arial", 12), state="readonly")
comb_dest.grid(row=2, column=2, padx=10, pady=5)
comb_dest.set("Hindi")

# Destination Text
dest_label = Label(frame, text="Translated Text:", font=("Arial", 16, "bold"))
dest_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

dest_txt = Text(frame, font=("Arial", 14), wrap=WORD, height=8, width=40, bd=2, relief="groove")
dest_txt.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

dest_scroll = ttk.Scrollbar(frame, command=dest_txt.yview)
dest_scroll.grid(row=4, column=3, sticky="ns")
dest_txt.config(yscrollcommand=dest_scroll.set)

# Theme Toggle
theme_btn = Button(root, text="Toggle Dark Mode", font=("Arial", 12), command=toggle_theme, relief="raised", bd=3)
theme_btn.pack(pady=10)

apply_theme()
root.mainloop()
