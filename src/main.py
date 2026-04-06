from tkinter import Tk
from src.ui.ui import UI

def main():

    root = Tk()
    root.title("TBA")
    root.geometry("400x600")

    ui_screen = UI(root)
    ui_screen.start()

    root.mainloop()


if __name__ == "__main__":
    main()
