# Import libraries
from tkinter import Canvas
from tkinter import Tk

screen = Tk()

# variables
screenWidth = 400
screenHeight = 300
shapeWidth = 15
shapeHeight = 15

can = Canvas(screen, screenWidth, screenHeight)
can.pack()

can.create_rectangle(
  (screenWidth / 2) - shapeWidth, (screenHeight / 2) - shapeWidth,
  (screenWidth / 2) + shapeWidth, (screenHeight / 2) + shapeHeight,
  fill="blue")

screen.mainloop()
