import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time


stream = cv2.VideoCapture("mp4.mp4")
def play(speed):
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=width, height=height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    canvas.create_text(184, 36, fill='black', font='Times 26 bold', text='Decision Pending')
    
def goal():
    thread = threading.Thread(target=pending, args=("goal",))
    thread.daemon = 1
    thread.start()

def free_Kick():
    thread = threading.Thread(target=pending, args=("free_Kick",))
    thread.daemon = 1
    thread.start()

def penalty():
    thread = threading.Thread(target=pending, args=("penalty",))
    thread.daemon = 1
    thread.start()

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=width, height=height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    
    time.sleep(1)

    frame = cv2.cvtColor(cv2.imread("sponser.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=width, height=height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    
    time.sleep(1.5)
    
    if decision == 'penalty':
        decisionImg = "penalty.jpg"
    
    elif decision == 'goal':
        decisionImg = "goal.jpg"
    
    elif decision == 'free_Kick':
        decisionImg = "free kick.jpg"
    
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=width, height=height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

width = 650
height = 368

windows = tkinter.Tk()
windows.title("Afnan's Refree Decision Review System")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(windows, width=width, height=height)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

btn = tkinter.Button(windows, text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(windows, text="<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(windows, text="Next (slow) >>", width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(windows, text="Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(windows, text="Goal", width=50, command=goal)
btn.pack()

btn = tkinter.Button(windows, text="Free Kick", width=50, command=free_Kick)
btn.pack()

btn = tkinter.Button(windows, text="Penalty", width=50, command=penalty)
btn.pack()


windows.mainloop()