import tkinter as tk 
BACKGROUND = "#fff1f8"         # soft pink
TIMER_COLOR = "#ffb3c1"        # soft rose
BUTTON_BG = "#fcd5ce"          # peach
BUTTON_ACTIVE = "#f8c4b4"      # peach darker
TEXT_COLOR = "#5d3a3a"         # warm brown
FONT = ("Helvetica", 14)
is_paused = False
remaining_time = 1500
timer_job = None 
pomodoro_count = 0 
is_work_session = True 
def start_timer(): 
    global is_paused, remaining_time, timer_job
    is_paused = False        
    remaining_time = 1500 
    start_button.config(state = "disabled")
    pause_button.config(state = "normal", text = "Pause")
    timer_label.config(fg="#ff6f91")
    count_down()
def count_down():
    global remaining_time, timer_job
    minutes = remaining_time //60 
    remaining_seconds = remaining_time % 60 
    timer_label.config(text=f"{minutes:02d}:{remaining_seconds:02d}")
    if remaining_time > 0:
        if not is_paused:
            remaining_time -=1
            timer_job = root.after(1000, count_down)
    else:
        if is_work_session: 
            pomodoro_count += 1 
            pomodoro_label.config(text=f"Pomodoros Completed: {pomodoro_count}")
        timer_label.config(text="Time's up!")
        pause_button.config(state="disabled")
def pause_resume_timer(): 
    global is_paused, timer_job, remaining_time
    if is_paused: 
        is_paused = False
        pause_button.config(text="Pause")
        count_down()
    else: 
        is_paused = True 
        pause_button.config(text="Resume")
        if timer_job is not None: 
            root.after_cancel(timer_job)
def reset_timer(): 
    global timer_job, remaining_time, is_paused
    root.after_cancel(timer_job)
    remaining_time = 1500 
    is_paused = False 
    start_button.config(state = "normal")
    pause_button.config(state = "disabled", text = "Pause")
    timer_label.config(text="25:00", fg="#ff6f91")
def start_short_break():
    global timer_job, remaining_time, is_paused
    root.after_cancel(timer_job)
    remaining_time = 300 
    is_paused = False 
    start_button.config(state = "disabled")
    pause_button.config(state = "normal")
    timer_label.config(text = "05:00")
    timer_label.config(fg="#82caff")
    count_down()
def start_long_break(): 
    global timer_job, remaining_time, is_paused
    root.after_cancel(timer_job)
    remaining_time = 900 
    is_paused = False 
    start_button.config(state = "disabled")
    pause_button.config(state = "normal")
    timer_label.config(text = "15:00")
    timer_label.config(fg="#b692f6") 
    count_down()
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("360x400")
root.configure(bg=BACKGROUND)
timer_label = tk.Label(root, text="25:00", font=("Comic Sans MS", 48, "bold"),
                       fg="#ff6f91", bg=BACKGROUND)
timer_label.pack(pady=15)

pomodoro_label = tk.Label(root, text="🍅 Pomodoros Completed: 0", font=FONT, fg=TEXT_COLOR, bg=BACKGROUND)
pomodoro_label.pack(pady=5)

# 🧁 Button Container
button_frame = tk.Frame(root, bg=BACKGROUND)
button_frame.pack(pady=10)

def kawaii_button(master, text, command):
    return tk.Button(master, text=text, command=command,
                     bg=BUTTON_BG, fg=TEXT_COLOR, activebackground=BUTTON_ACTIVE,
                     relief="flat", font=FONT, width=15, height=1)

start_button = kawaii_button(button_frame, "⏱ Start", start_timer)
start_button.grid(row=0, column=0, padx=5, pady=5)

pause_button = kawaii_button(button_frame, "⏸ Pause", pause_resume_timer)
pause_button.grid(row=0, column=1, padx=5, pady=5)
pause_button.config(state="disabled")

reset_button = kawaii_button(button_frame, "🔁 Reset", reset_timer)
reset_button.grid(row=1, column=0, padx=5, pady=5)

short_break_button = kawaii_button(button_frame, "☕ Short Break", start_short_break)
short_break_button.grid(row=1, column=1, padx=5, pady=5)

long_break_button = kawaii_button(button_frame, "💤 Long Break", start_long_break)
long_break_button.grid(row=2, column=0, columnspan=2, pady=5)
root.mainloop()