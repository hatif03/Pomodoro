from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
def tick():
    marks =""
    for i in range(int((reps+1)/2)):
        marks += "✓"
    return marks
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    text_label.config(text="Timer")
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        text_label.config(text="Break", fg=RED, font=(FONT_NAME, 48), bg=YELLOW)
        count_down(LONG_BREAK_MIN*60)
    else:
        if reps % 2 == 0:
            text_label.config(text="Break", fg=PINK, font=(FONT_NAME, 48), bg=YELLOW)
            count_down(SHORT_BREAK_MIN*60)
        else:
            text_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 48), bg=YELLOW)
            count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 == 1:
            tick_label.config(text= tick())
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=110, pady=80, bg=YELLOW)

blank_label = Label(text="")
blank_label.grid(row=0, column=0)

text_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 48), bg=YELLOW)
text_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 12), bd=2, command=start_timer)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 12), bd=2, command=reset_timer)
reset_button.grid(row=3, column=2)

tick_label = Label(fg=GREEN, font=(FONT_NAME, 16), bg=YELLOW)
tick_label.grid(row=4, column=1)


window.mainloop()
