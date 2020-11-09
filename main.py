from tkinter import *
from tkinter import filedialog
import hash


def choose_file_callback(root, label_to_update):
    """ Choose a file from the local disk and display the path in the GUI """
    root.filename = filedialog.askopenfilename(initialdir="C:\\", title="Select a file")
    label_to_update.config(text=root.filename)


def radio_button_selection(selection, filepath, label):
    """ Get selection from the radio button

    Parameters
    ----------
    selection: int
        Algorithm choice between MD5 and SHA-256
    filepath: str
        A string representing the absolute path of the file
    label: Label()
        Text label representing the final hash (result)
    """
    algorithm_choice = selection.get()

    if algorithm_choice == 1:
        result_hash = hash.md5(filepath)
    elif algorithm_choice == 2:
        result_hash = hash.sha256(filepath)
    else:
        result_hash = "Error while computing hash"

    label.config(text=result_hash)


def initialize_gui():
    """ Initialize all the graphical elements """

    #Initial Configuration
    root = Tk()
    root.geometry("500x500")  # Height and Width Specification
    root.configure(background='#c9c7c7')  # Background will be Silver Lake Blue
    root.title("Hash Verifier")
    root.resizable(False, False)  # Gui is not resizable
    #root.iconbitmap("img/icon.bmp") #fix the icon #FIXME: the image must be a bitmap and not png/jpg


    # This frame is a container for all his children
    frame = Frame(root, bg="#f1f1f1")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    welcome_label = Label(frame, text="Choose the file and select the algorith:", font=('Futura',11,'bold'))
    welcome_label.place(relx = 0.15, rely = 0.1)

    file_label = Label(frame, text="No file chosen!",font=('Futura',11,'italic') )
    file_label.place(relx=0.15, rely=0.25)

    choose_file_button = Button(text="Choose File", command=lambda : choose_file_callback(root,file_label))
    choose_file_button.place(relx=0.43, rely=0.4)

    var = IntVar()
    md5_radioButton = Radiobutton(frame, text="MD5", variable=var, value=1, font=('Futura',11,'bold'),command=lambda : radio_button_selection(var,root.filename, result_label))
    sha256_radioButton = Radiobutton(frame, text="SHA256", variable=var, value=2, font=('Futura',11,'bold'), command=lambda: radio_button_selection(var,root.filename, result_label))

    md5_radioButton.place(relx=0.4, rely = 0.5)
    sha256_radioButton.place(relx=0.4, rely = 0.6)

    result_label = Label(frame, text="", font=('Futura',7,'italic'))
    result_label.place(relx=0.1, rely=0.8)

    root.mainloop()


def main():
    initialize_gui()


if __name__ == "__main__":
    main()