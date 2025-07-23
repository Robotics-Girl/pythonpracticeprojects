import tkinter as tk 
actions = []
redo_list = []
current_color = "#ffddee"
colors = {"Pink":"#ffddee", "Mint": "#b4f2d0", "Blue": "#82caff", "Peach": "#f9c6b7"}
brush_size = 4 
screen = tk.Tk()
screen.title("🎨 Kawaii Drawing Pad")
screen.geometry("600x500")
screen.configure(bg="#fff1f8")
canvas = tk.Canvas(screen, width = "550", height = "450", bg="#fffaf0")
canvas.pack(pady=20)
def draw(event): 
    global current_color, brush_size, oval_id
    x = event.x 
    y = event.y 
    r= brush_size
    oval_id = canvas.create_oval(x - r, y - r, x + r, y + r, fill=current_color, outline=current_color)
    actions.append({"id": oval_id, "x": x, "y": y, "color" : current_color, "size" : brush_size})
canvas.bind("<B1-Motion>", draw)
def change_color(new_color): 
    global current_color
    current_color = new_color 
def undo(): 
    global actions, redo_list, last_id
    if actions: 
        last_action = actions.pop()
        canvas.delete(last_action["id"])
        redo_list.append(last_action)
def redo():
    global actions, redo_list
    if redo:
        last_action = redo.pop()
        x = last_action["x"]
        y = last_action["y"]
        r = last_action["size"]
        color = last_action["color"]

        new_id = canvas.create_oval(
            x - r, y - r, x + r, y + r,
            fill=color,
            outline=color
        )
        last_action["id"] = new_id
        actions.append(last_action)
frame = tk.Frame(screen, width = "100", height = "50", bg = "#fff1f8")
frame.pack(pady=10)
for color_name, hex_code in colors.items():
    btn = tk.Button(
        frame, 
        text=color_name, 
        bg="#fff1f8", 
        width=6, 
        relief="flat", 
        command=lambda c=hex_code: change_color(c)
    )
    btn.pack(side="left", padx=5)
def clear_canvas():
    canvas.delete("all")
def update_brush_value(val): 
    global brush_size
    brush_size = int(val)
clear_button = tk.Button(screen, text = "Clear", bg = "#fff1f8", width = 6, command = clear_canvas)
clear_button.pack(pady=10)
brush_slider = tk.Scale(screen, from_=1, to=20, orient="horizontal", length=200, label="Brush Size", command = update_brush_value )
brush_slider.pack()
redo_button = tk.Button(screen, text = "Redo", bg = "#fff1f8", width = 6, command = redo)
redo_button.pack(pady=10)
undo_button = tk.Button(screen, text = "Undo", bg = "#fff1f8", width = 6, command = undo)
undo_button.pack(pady=10)
screen.mainloop()