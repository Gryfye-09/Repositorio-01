import tkinter as tk

ventana = tk.Tk()
ventana.title("LabelFrame en Tkinder")
ventana.geometry("800x600+20+20")
ventana.minsize(400, 300)
ventana.maxsize(900, 900)
ventana.config(bg="spring green")

frame1 = tk.Frame(ventana)
frame1.configure(width=350, height=250, bg="lightyellow", bd=5)
frame1.pack()

frame2 = tk.Frame(frame1)
frame2.configure(width=200, height=100, bg="lightcoral", bd=5)
frame2.pack()

boton = tk.Button(frame1, text="Boton dentro de Frame 1")
boton.pack()

ventana.mainloop()