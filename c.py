import tkinter as tk
from tkinter import PhotoImage
import webbrowser

# variable to store images
# 0 = compressor
# 1 = evaporator
# 2 = expansion valve
# 3 = condenser
# 4 = dryer
top_image = -1
left_image = -1
right_top_image = -1
right_bottom_image = -1
bottom_image = -1


def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    win.geometry(f"{width}x{height}+{x}+{y}")


window = tk.Tk()
window.title("AC System")
center_window(window, 1200, 800)


top_panel = tk.Frame(window, height=40, bg="#e0e0e0")
top_panel.pack(side="top", fill="x")


def clear_data():
    global top_image, left_image, right_top_image, right_bottom_image, bottom_image
    top_image = -1
    left_image = -1
    right_top_image = -1
    right_bottom_image = -1
    bottom_image = -1
    canvas1.delete("all")
    canvas2.delete("all")
    canvas3.delete("all")
    canvas4.delete("all")
    print("Data cleared.")


def check_answer():
    global top_image, left_image, right_top_image, right_bottom_image, bottom_image
    if top_image == 0:
        canvas1.config(highlightbackground="green", highlightthickness=2)
    else:
        canvas1.config(highlightbackground="red", highlightthickness=2)

    if left_image == 1:
        canvas2.config(highlightbackground="green", highlightthickness=2)
    else:
        canvas2.config(highlightbackground="red", highlightthickness=2)

    if right_top_image == 3:
        canvas3.config(highlightbackground="green", highlightthickness=2)
    else:
        canvas3.config(highlightbackground="red", highlightthickness=2)

    if right_bottom_image == 4:
        canvas5.config(highlightbackground="green", highlightthickness=2)
    else:
        canvas5.config(highlightbackground="red", highlightthickness=2)

    if bottom_image == 2:
        canvas4.config(highlightbackground="green", highlightthickness=2)
    else:
        canvas4.config(highlightbackground="red", highlightthickness=2)


new_button = tk.Button(top_panel, text="New", command=clear_data)
new_button.pack(side="left", padx=5, pady=5)

check_button = tk.Button(top_panel, text="Check", command=check_answer)
check_button.pack(side="left", padx=5, pady=5)


canvas_frame = tk.Frame(window, bg="white")
canvas_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)


# Create a 3x3 grid of canvases
def show_image(canvas, image_path, position, ans):
    canvas.delete("all")  # Clear previous image
    img = PhotoImage(file=image_path)
    canvas.image = img  # Keep a reference to avoid garbage collection
    canvas.create_image(0, 0, anchor="nw", image=img)

    if position == "top":
        global top_image
        top_image = ans
        canvas1.config(highlightbackground="white", highlightthickness=0)
    elif position == "left":
        global left_image
        left_image = ans
        canvas2.config(highlightbackground="white", highlightthickness=0)
    elif position == "right_top_image":
        global right_top_image
        right_top_image = ans
        canvas3.config(highlightbackground="white", highlightthickness=0)
    elif position == "right_bottom_image":
        global right_bottom_image
        right_bottom_image = ans
        canvas5.config(highlightbackground="white", highlightthickness=0)
    elif position == "bottom":
        global bottom_image
        bottom_image = ans
        canvas4.config(highlightbackground="white", highlightthickness=0)

    print(f"Clicked on canvas1, {position}: {ans}")


def on_canvas1_click(event):
    popup = tk.Menu(window, tearoff=0)
    popup.add_command(
        label="Compressor",
        command=lambda: show_image(canvas1, "compressor.png", "top", 0),
    )
    popup.add_command(
        label="Evaporator",
        command=lambda: show_image(canvas1, "evaporator.png", "top", 1),
    )
    popup.add_command(
        label="Expansion Valve",
        command=lambda: show_image(canvas1, "expasion.png", "top", 2),
    )
    popup.add_command(
        label="Condenser",
        command=lambda: show_image(canvas1, "condensor.png", "top", 3),
    )
    popup.add_command(
        label="Dryer", command=lambda: show_image(canvas1, "dryer.png", "top", 4)
    )
    popup.post(event.x_root, event.y_root)


def on_canvas2_click(event):
    popup = tk.Menu(window, tearoff=0)
    popup.add_command(
        label="Compressor",
        command=lambda: show_image(canvas2, "compressor.png", "left", 0),
    )
    popup.add_command(
        label="Evaporator",
        command=lambda: show_image(canvas2, "evaporator.png", "left", 1),
    )
    popup.add_command(
        label="Expansion Valve",
        command=lambda: show_image(canvas2, "expasion.png", "left", 2),
    )
    popup.add_command(
        label="Condenser",
        command=lambda: show_image(canvas2, "condensor.png", "left", 3),
    )
    popup.add_command(
        label="Dryer", command=lambda: show_image(canvas2, "dryer.png", "left", 4)
    )
    popup.post(event.x_root, event.y_root)


def on_canvas3_click(event):
    popup = tk.Menu(window, tearoff=0)
    popup.add_command(
        label="Compressor",
        command=lambda: show_image(canvas3, "compressor.png", "right_top_image", 0),
    )
    popup.add_command(
        label="Evaporator",
        command=lambda: show_image(canvas3, "evaporator.png", "right_top_image", 1),
    )
    popup.add_command(
        label="Expansion Valve",
        command=lambda: show_image(canvas3, "expasion.png", "right_top_image", 2),
    )
    popup.add_command(
        label="Condenser",
        command=lambda: show_image(canvas3, "condensor.png", "right_top_image", 3),
    )
    popup.add_command(
        label="Dryer",
        command=lambda: show_image(canvas3, "dryer.png", "right_top_image", 4),
    )
    popup.post(event.x_root, event.y_root)


def on_canvas4_click(event):
    popup = tk.Menu(window, tearoff=0)
    popup.add_command(
        label="Compressor",
        command=lambda: show_image(canvas4, "compressor.png", "bottom", 0),
    )
    popup.add_command(
        label="Evaporator",
        command=lambda: show_image(canvas4, "evaporator.png", "bottom", 1),
    )
    popup.add_command(
        label="Expansion Valve",
        command=lambda: show_image(canvas4, "expasion.png", "bottom", 2),
    )
    popup.add_command(
        label="Condenser",
        command=lambda: show_image(canvas4, "condensor.png", "bottom", 3),
    )
    popup.add_command(
        label="Dryer", command=lambda: show_image(canvas4, "dryer.png", "bottom", 4)
    )
    popup.post(event.x_root, event.y_root)


def on_canvas5_click(event):
    popup = tk.Menu(window, tearoff=0)
    popup.add_command(
        label="Compressor",
        command=lambda: show_image(canvas5, "compressor.png", "right_bottom_image", 0),
    )
    popup.add_command(
        label="Evaporator",
        command=lambda: show_image(canvas5, "evaporator.png", "right_bottom_image", 1),
    )
    popup.add_command(
        label="Expansion Valve",
        command=lambda: show_image(canvas5, "expasion.png", "right_bottom_image", 2),
    )
    popup.add_command(
        label="Condenser",
        command=lambda: show_image(canvas5, "condensor.png", "right_bottom_image", 3),
    )
    popup.add_command(
        label="Dryer",
        command=lambda: show_image(canvas5, "dryer.png", "right_bottom_image", 4),
    )
    popup.post(event.x_root, event.y_root)


canvas1 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas1.grid(row=0, column=1, padx=10, pady=10)
canvas1.bind("<Button-1>", on_canvas1_click)

canvas2 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas2.grid(row=2, column=0, padx=10, pady=10)
canvas2.bind("<Button-1>", on_canvas2_click)

canvas3 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas3.grid(row=1, column=2, padx=10, pady=10)
canvas3.bind("<Button-1>", on_canvas3_click)

canvas4 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas4.grid(row=4, column=1, padx=10, pady=10)
canvas4.bind("<Button-1>", on_canvas4_click)

canvas5 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas5.grid(row=3, column=2, padx=10, pady=10)
canvas5.bind("<Button-1>", on_canvas5_click)

canvas6 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas6.grid(row=0, column=0)
canvas6.image = PhotoImage(file="1.png")
canvas6.create_image(0, 0, anchor="nw", image=canvas6.image)
canvas6.config(highlightbackground="white", highlightthickness=0)

canvas7 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas7.grid(row=0, column=2)
canvas7.image = PhotoImage(file="2.png")
canvas7.create_image(0, 0, anchor="nw", image=canvas7.image)
canvas7.config(highlightbackground="white", highlightthickness=0)

canvas8 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas8.grid(row=4, column=0)
canvas8.image = PhotoImage(file="5.png")
canvas8.create_image(0, 0, anchor="nw", image=canvas8.image)
canvas8.config(highlightbackground="white", highlightthickness=0)

canvas9 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas9.grid(row=4, column=2)
canvas9.image = PhotoImage(file="4.png")
canvas9.create_image(0, 0, anchor="nw", image=canvas9.image)
canvas9.config(highlightbackground="white", highlightthickness=0)

canvas10 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas10.grid(row=2, column=2)
canvas10.image = PhotoImage(file="3.png")
canvas10.create_image(0, 0, anchor="nw", image=canvas10.image)
canvas10.config(highlightbackground="white", highlightthickness=0)

canvas11 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas11.grid(row=3, column=0)
canvas11.image = PhotoImage(file="6.png")
canvas11.create_image(0, 0, anchor="nw", image=canvas11.image)
canvas11.config(highlightbackground="white", highlightthickness=0)

canvas12 = tk.Canvas(canvas_frame, bg="white", width=200, height=100)
canvas12.grid(row=1, column=0)
canvas12.image = PhotoImage(file="7.png")
canvas12.create_image(0, 0, anchor="nw", image=canvas12.image)
canvas12.config(highlightbackground="white", highlightthickness=0)

# Configure the grid to expand properly
canvas_frame.grid_rowconfigure(0, weight=1)
canvas_frame.grid_rowconfigure(1, weight=1)
canvas_frame.grid_rowconfigure(2, weight=1)
canvas_frame.grid_columnconfigure(0, weight=1)
canvas_frame.grid_columnconfigure(1, weight=1)
canvas_frame.grid_columnconfigure(2, weight=1)

window2 = None  # Initialize window2 as None


def show_data(fram, window):
    for widget in fram.winfo_children():
        widget.destroy()

    if window == "Main":
        canvas_info = tk.Canvas(fram, bg="white", width=1000, height=600)
        canvas_info.grid(row=0, column=0)
        canvas_info.image = PhotoImage(file="14.png")
        canvas_info.create_image(0, 0, anchor="nw", image=canvas_info.image)
        canvas_info.config(highlightthickness=0)

        link_button = tk.Button(
            fram,
            text="Link",
            font=("Arial", 16),
            bg="white",
            command=lambda: window2.after(0, lambda: window2.destroy()) or window.after(0, lambda: window.destroy()) or webbrowser.open("https://youtu.be/zUiWd5gopmw?si=dg8C6j40gFQVmFV7"),
        )
        link_button.grid(row=1, column=0, pady=10)

    if window == "Evaporator":
        canvas_info = tk.Canvas(fram, bg="white", width=200, height=100)
        canvas_info.grid(row=0, column=0)
        canvas_info.image = PhotoImage(file="evaporator.png")
        canvas_info.create_image(0, 0, anchor="nw", image=canvas_info.image)
        canvas_info.config(highlightthickness=0)

        label = tk.Label(
            fram, text="Evaporator Information", font=("Arial", 16), bg="white"
        )
        label.grid(row=1, column=0, pady=10)

        text = tk.Text(fram, wrap="word", width=50, height=20)
        text.grid(row=2, column=0, padx=10, pady=10)
        text.insert(
            "1.0",
            "Evaporator : สารทำความเย็นในรูปของละอองฝอยที่ไหลผ่านในตัว Evaporator จะดูดซับความร้อนภายในรถ ทำให้อากาศภายในรถเย็นขึ้น และเกิดกระบวนการกลายเป็นไออย่างทันทีทันใด ทำให้สารทำความเย็นกลับมาอยู่ในสถานะก๊าซอีกครั้ง และถูกส่งกลับมายัง Compressor",
        )

    if window == "Compressor":
        canvas_info = tk.Canvas(fram, bg="white", width=200, height=100)
        canvas_info.grid(row=0, column=0)
        canvas_info.image = PhotoImage(file="compressor.png")
        canvas_info.create_image(0, 0, anchor="nw", image=canvas_info.image)
        canvas_info.config(highlightthickness=0)

        label = tk.Label(
            fram, text="Compressor Information", font=("Arial", 16), bg="white"
        )
        label.grid(row=1, column=0, pady=10)

        text = tk.Text(fram, wrap="word", width=50, height=20)
        text.grid(row=2, column=0, padx=10, pady=10)
        text.insert(
            "1.0",
            "Compressor : ทำหน้าที่ ดูดสารทำความเย็นที่มาจากอีวาปอเรเตอร์ และทำการอัดให้กลายเป็นสารทำความเย็นที่สถานะก๊าซ จากนั้นจะส่งผ่านไปยัง Condenser",
        )

    if window == "Condenser":
        canvas_info = tk.Canvas(fram, bg="white", width=200, height=100)
        canvas_info.grid(row=0, column=0)
        canvas_info.image = PhotoImage(file="condensor.png")
        canvas_info.create_image(0, 0, anchor="nw", image=canvas_info.image)
        canvas_info.config(highlightthickness=0)

        label = tk.Label(
            fram, text="Condenser Information", font=("Arial", 16), bg="white"
        )
        label.grid(row=1, column=0, pady=10)

        text = tk.Text(fram, wrap="word", width=50, height=20)
        text.grid(row=2, column=0, padx=10, pady=10)
        text.insert(
            "1.0",
            "Condenser : ทำหน้าเปลี่ยนสารทำความเย็นในสถานะก๊าซให้กลายเป็นสถานะของเหลวผ่านการควบแน่น จากนั้นส่งต่อไปยัง Receiver Dryer",
        )

    if window == "Dryer":
        canvas_info = tk.Canvas(fram, bg="white", width=200, height=100)
        canvas_info.grid(row=0, column=0)
        canvas_info.image = PhotoImage(file="dryer.png")
        canvas_info.create_image(0, 0, anchor="nw", image=canvas_info.image)
        canvas_info.config(highlightthickness=0)

        label = tk.Label(
            fram, text="Expansion Valve Information", font=("Arial", 16), bg="white"
        )
        label.grid(row=1, column=0, pady=10)

        text = tk.Text(fram, wrap="word", width=50, height=20)
        text.grid(row=2, column=0, padx=10, pady=10)
        text.insert(
            "1.0",
            "Receiver Dryer :  ทำหน้าที่ ดูดซับความชื้น กรองสิ่งสกปรกในระบบ และเป็นที่พักของสารทำความเย็น จากนั้นจะถูกส่งต่อไปยัง Expansion Valve",
        )

    if window == "Expansion":
        canvas_info = tk.Canvas(fram, bg="white", width=200, height=100)
        canvas_info.grid(row=0, column=0)
        canvas_info.image = PhotoImage(file="expasion.png")
        canvas_info.create_image(0, 0, anchor="nw", image=canvas_info.image)
        canvas_info.config(highlightthickness=0)

        label = tk.Label(
            fram, text="Expansion Valve Information", font=("Arial", 16), bg="white"
        )
        label.grid(row=1, column=0, pady=10)

        text = tk.Text(fram, wrap="word", width=50, height=20)
        text.grid(row=2, column=0, padx=10, pady=10)
        text.insert(
            "1.0",
            "Expansion Valve : ทำหน้าที่ ลดแรงดันของสารทำความเย็น และฉีดสารทำความเย็นในสถานะที่เป็นของเหลวในรูปแบบของฝอยละอองเข้าไปที่ Evaporator",
        )


def show_window2():
    global window2
    if window2 is None or not window2.winfo_exists():  # Check if window2 doesn't exist
        window2 = tk.Toplevel(window)
        window2.title("Info")
        center_window(window2, 1200, 800)
        # top_panel2 = tk.Frame(window2, height=40, bg="#e0e0e0")
        # top_panel2.pack(side="top", fill="x")
        # new_button2 = tk.Button(top_panel2, text="Main", command=window2.withdraw)
        # new_button2.pack(side="left", padx=5, pady=5)

        top_panel_info = tk.Frame(window2, height=40, bg="#e0e0e0")
        top_panel_info.pack(side="top", fill="x")

        canvas_frame2 = tk.Frame(window2, bg="white")
        canvas_frame2.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        main_button = tk.Button(
            top_panel_info,
            text="Main",
            command=lambda: show_data(canvas_frame2, "Main"),
        )
        main_button.pack(side="left", padx=5, pady=5)

        evaporator_button = tk.Button(
            top_panel_info,
            text="Evaporator",
            command=lambda: show_data(canvas_frame2, "Evaporator"),
        )
        evaporator_button.pack(side="left", padx=5, pady=5)

        compressor_button = tk.Button(
            top_panel_info,
            text="Compressor",
            command=lambda: show_data(canvas_frame2, "Compressor"),
        )
        compressor_button.pack(side="left", padx=5, pady=5)
        
        condenser_button = tk.Button(
            top_panel_info,
            text="Condenser",
            command=lambda: show_data(canvas_frame2, "Condenser"),
        )
        condenser_button.pack(side="left", padx=5, pady=5)

        dryer_button = tk.Button(
            top_panel_info,
            text="Dryer",
            command=lambda: show_data(canvas_frame2, "Dryer"),
        )
        dryer_button.pack(side="left", padx=5, pady=5)

        expansion_button = tk.Button(
            top_panel_info,
            text="Expansion",
            command=lambda: show_data(canvas_frame2, "Expansion"),
        )
        expansion_button.pack(side="left", padx=5, pady=5)

        link_button = tk.Button(
            top_panel_info,
            text="Link",
            command=lambda: webbrowser.open("https://youtu.be/zUiWd5gopmw?si=dg8C6j40gFQVmFV7"),
        )
        link_button.pack(side="left", padx=5, pady=5)

        canvas_info = tk.Canvas(canvas_frame2, bg="white", width=1000, height=600)
        canvas_info.grid(row=0, column=0)
        canvas_info.image = PhotoImage(file="14.png")
        canvas_info.create_image(0, 0, anchor="nw", image=canvas_info.image)
        canvas_info.config(highlightthickness=0)

    else:
        if window2.state() == "withdrawn":
            window2.deiconify()
        else:
            window2.withdraw()


show_button = tk.Button(top_panel, text="Show info", command=show_window2)
show_button.pack(side="left", padx=5, pady=5)

window.mainloop()