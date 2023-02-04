import tkinter as tk

root = tk.Tk()
root.geometry("350x600")
root.title("nooked")

label = tk.Label(root, text = "welcome to nooked!", font=('Arial', 26))
label.pack(pady = 26)

bookLabel = tk.Label(root, text = "enter a book title here:", font = ('Arial', 16)) 
bookLabel.pack(pady = 10)

btextbox = tk.Entry(root)
btextbox.pack()

book = ""
def get_book():
    text = btextbox.get()
    #print(text)
    bookname = text

bbutton = tk.Button(root, text="enter", command=get_book)
bbutton.pack()

emotionLabel = tk.Label(root, text = "enter an emotion here:", font  = ("Arial", 16))
emotionLabel.pack(pady = 26)

etextbox = tk.Entry(root)
etextbox.pack()

feeling = ""
def get_emotion():
    text = etextbox.get()
    #print(text)
    feeling = text

ebutton = tk.Button(root, text="enter", command=get_emotion)
ebutton.pack()

root.mainloop()