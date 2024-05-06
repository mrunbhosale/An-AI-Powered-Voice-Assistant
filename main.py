# Libraries for the main application:
import tkinter as tk
from screeninfo import get_monitors
# Libraries for UI management:
from tkinter import *
import cv2
from PIL import Image, ImageTk
# Library for assisting functionality:
import subprocess
# User-defined Libraries:
from chat import get_response, bot_name

for m in get_monitors():
    w = m.width 
    h = m.height

# Declaring some useful variables: 
BG_COLOR = "black"
BG_COLOR2 = "white"
TEXT_COLOR = "white"
TEXT_COLOR2 = "white"
TEXT_COLOR3 = "black"
FONT = "Arial 11"
FONT_BOLD = "Helvetica 13 bold"

class BG_video:

    def __init__(self, parent, video_source):
        self.parent = parent
        self.video_source = video_source

        self.canvas = tk.Canvas(parent, width=w, height=h)
        self.canvas.pack()

        self.vid = cv2.VideoCapture(self.video_source, cv2.CAP_FFMPEG)
        self.update()

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            # Resize the frame to fit the canvas while maintaining aspect ratio
            canvas_ratio = self.canvas.winfo_width() / self.canvas.winfo_height()
            frame_ratio = frame.shape[1] / frame.shape[0]

            if canvas_ratio > frame_ratio:
                # Canvas is wider than frame
                new_width = int(self.canvas.winfo_height() * frame_ratio)
                new_height = self.canvas.winfo_height()
            else:
                # Canvas is taller than frame or they have the same aspect ratio
                new_width = self.canvas.winfo_width()
                new_height = int(self.canvas.winfo_width() / frame_ratio)

            resized_frame = cv2.resize(frame, (w, h))

            # Convert resized frame to ImageTk format
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)))

            # Clear previous image and draw new resized image
            self.canvas.delete("all")
            self.canvas.create_image((self.canvas.winfo_width() - new_width) // 2,
                                    (self.canvas.winfo_height() - new_height) // 2,
                                    anchor=tk.NW, image=self.photo)
        else:
            # If the video ends, rewind to the beginning
            self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.parent.after(10, self.update)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

class AppDesign(tk.Frame):

    def __init__(self, parent, video_source):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("C.Y.P.H.E.R")
        self.video_source = video_source

        self.bg_video = BG_video(self.parent, self.video_source)

        # Top container
        head_label = Label(self.parent, width=39, height=2, highlightthickness=1, bg=BG_COLOR, fg=TEXT_COLOR2,
                           text="C.Y.P.H.E.R Chat Access", font=FONT_BOLD)
        head_label.place(relx=0.8327, rely=0.57, anchor=tk.CENTER)
        head_label.configure(highlightbackground="grey")

        # Middle container
        line = Label(self.parent, width=64, height=17, bg=BG_COLOR2)
        line.place(relx=0.8327, rely=0.778, anchor=tk.CENTER)
        
        # Chat log window
        self.text_widget = Text(self.parent, width=49, height=13, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT)
        self.text_widget.place(relx=0.8277, rely=0.748, anchor=tk.CENTER)
        self.text_widget.configure(cursor="arrow", state="disabled")
        
        # Scroll bar
        scrollbar = Scrollbar(line)
        scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        scrollbar.configure(command=self.text_widget.yview)
        
        # Bottom container
        bottom_label = Label(self.parent, bg=BG_COLOR, highlightthickness=1, width=64, height=3)
        bottom_label.place(relx=0.8327, rely=0.928, anchor=tk.CENTER)
        bottom_label.configure(highlightbackground="grey")
        
        # Query box
        self.msg_entry = tk.Entry(bottom_label, bg="white", fg=TEXT_COLOR3, font=FONT, width=40)
        self.msg_entry.place(relx=0.43, rely=0.5, anchor=tk.CENTER)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # Send button
        send_button = Button(bottom_label, text="➤", font=FONT_BOLD, height=1, width=4, bg=BG_COLOR2,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.92, rely=0.5, anchor=tk.CENTER)

        # Loading the mic image
        self.raw_image = tk.PhotoImage(file=r"C:\Users\LENOVO\Desktop\C.Y.P.H.E.R\Resources\Mic.png")
        
        # Resizing the image
        self.mic_image = self.raw_image.subsample(6, 6)

        # Create a circular microphone button with transparent canvas as background
        self.button = tk.Button(self.parent, image=self.mic_image, command=self.record_audio, bg="dodgerblue", font=(18))
        self.button.place(relx=0.5, rely=0.9, anchor=tk.CENTER, width=80, height=80)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "User")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, tk.END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state="normal")
        self.text_widget.insert(tk.END, msg1)
        self.text_widget.configure(state="disabled")
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state="normal")
        self.text_widget.insert(tk.END, msg2)
        self.text_widget.configure(state="disabled")
        self.text_widget.see(tk.END)

    def record_audio(self):
        # Execute the voice_assistant1.py script using subprocess
        subprocess.Popen(["python", "voice_assistant.py"])

app = tk.Tk()
app.geometry(f"{w}x{h}")
app.iconbitmap(r"C:\Users\LENOVO\Desktop\C.Y.P.H.E.R\Resources\Logo.ico")
video_source = r"C:\Users\LENOVO\Desktop\C.Y.P.H.E.R\Resources\CYPHER.mp4"
final_app = AppDesign(app, video_source)
final_app.pack(fill=tk.BOTH, expand=True)
app.mainloop()