import tkinter
import random
import time
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
window.mainloop
a = ['red','blue','yellow','purple','green','pink','orange']
x0 = 30
y0 = 5
x1 = 220
y1 = 195
v = 19
for c in range(10):
    R = 0
    for R in range(19):
        color = random.choice(a)
        time.sleep(0.05)
        canvas.update()
        canvas.create_oval(x0, y0, x1, y1, outline=color)
        x0 += 5
        y0 += 5
        x1 -= 5
        y1 -= 5
    R = 0
    for R in range(19):
        time.sleep(0.05)
        canvas.update()
        canvas.create_oval(x0, y0, x1, y1, outline='white')
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5
window.mainloop()