from tkinter import *

ventana =Tk()

# marco 1
marco1 = Frame()
marco1.grid(row=0, column=0)
marco1.config(width=100, height=100, bg="lightgrey")

# marco 2
marco2 = Frame()
marco2.grid(row=1, column=0)
marco2.config(width=100, height=100, bg="yellow")

# marco 3
marco3 = Frame()
marco3.grid(row=1, column=1)
marco3.config(width=100, height=100, bg="blue")

# marco 4
marco4 = Frame()
marco4.grid(row=2, column=0)
marco4.config(width=100, height=100, bg="green")

# marco 5
marco5 = Frame()
marco5.grid(row=0, column=1)
marco5.config(width=100, height=100, bg="black")

# marco 6
marco6 = Frame()
marco6.grid(row=2, column=1)
marco6.config(width=100, height=100, bg="orange")

ventana.mainloop()