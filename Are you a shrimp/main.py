import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import matplotlib.pyplot as plt



def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def show_new_window(statistic):
    new_window = tk.Toplevel(root)

    random_number = random.randint(1, 10)
    statistic["pic" + str(random_number)] += 1

    if random_number > 5:
        new_window.title("You are a Shrimp")
    else:
        new_window.title("You are no Shrimp")
    image_path = "img/" + str(random_number) + ".png"


    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)

    # Keep a reference to the image to prevent garbage collection
    panel = tk.Label(new_window, image=img)
    panel.img_ref = img

    panel.pack(side="bottom", fill="both", expand="yes")

    # Center the new window
    center_window(new_window)
    print(statistic)
    plot_bar_chart(statistic)


def plot_bar_chart(statistic):
    labels = list(statistic.keys())
    values = list(statistic.values())

    plt.bar(labels, values)
    plt.xlabel('Pictures')
    plt.ylabel('Counts')
    plt.title('Picture Statistics')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    statistic = {"pic1": 0, "pic2": 0, "pic3": 0, "pic4": 0, "pic5": 0,
                     "pic6": 0, "pic7": 0, "pic8": 0, "pic9": 0, "pic10": 0}

    root = tk.Tk()
    root.title("Are you a Shrimp App")

    clickable_image_path = "AreYouAShrim.png"
    clickable_img = Image.open(clickable_image_path)
    clickable_img = ImageTk.PhotoImage(clickable_img)

    canvas = tk.Canvas(root, width=clickable_img.width(), height=clickable_img.height())
    canvas.pack()

    canvas.create_image(0, 0, anchor=tk.NW, image=clickable_img)

    canvas.bind("<Button-1>", lambda event: show_new_window(statistic))

    root.mainloop()
