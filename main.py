from tkinter import *
import time


#! ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
work_cycle = 1
tick_mark = ''
timer = None

#! ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global tick_mark,timer
    window.after_cancel(timer)
    tick_mark = ""
    tick.config(text=f"{tick_mark}")
    label_text.config(text='Timer',fg=GREEN)
    canvas.itemconfig(text_im,text='00:00')
    work_cycle = 1
      
#! ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global tick_mark
    if work_cycle == 1 or work_cycle == 3 or work_cycle == 5 or work_cycle == 7:
        label_text.config(text='Work',fg=PINK)
        countdown(WORK_MIN)
        
    if work_cycle == 2 or work_cycle == 4 or work_cycle == 6:
        label_text.config(text='Break',fg=RED)
        countdown(SHORT_BREAK_MIN)
        tick_mark = tick_mark + '✓'
        tick.config(text=f"{tick_mark}")
        
        
    if work_cycle == 8:
        label_text.config(text='Long Break',fg=RED)
        countdown(LONG_BREAK_MIN)
        tick_mark = tick_mark + '✓'
        tick.config(text=f"{tick_mark}")
        
#! ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global tick_mark,work_cycle,timer
    
    canvas.itemconfig(text_im,text=time.strftime("%M:%S", time.gmtime(count)))
    if count > 0:
        timer = window.after(1000,countdown,count -1)
    if count ==0:
        work_cycle = work_cycle + 1
        window.lift()
        window.attributes("-topmost", True)
        
#! ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=60,pady=60,background=YELLOW)


canvas = Canvas(height=224,width=200,background=YELLOW,highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(103,112,image=image)
text_im =canvas.create_text(103,125,text=f"00:00",font=(FONT_NAME,18),fill="white")
canvas.grid(row=1,column=2)


button1_start = Button(text='Start',command=start)
button1_start.grid(row=2,column=1)

button2_reset = Button(text='Reset',command=reset)
button2_reset.grid(row=2,column=4)

label_text = Label(text='Timer',font=(FONT_NAME,28,'bold'),fg=GREEN,background=YELLOW)
label_text.grid(row=0,column=2)

tick = Label(text=f'{tick_mark}',font=(FONT_NAME,18,'bold'),fg=GREEN,background=YELLOW)
tick.grid(row=2 ,column=2 )




window.mainloop()
