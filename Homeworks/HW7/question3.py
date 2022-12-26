import tkinter as tk


class Game:

  # define variables
  width = 400
  height = 300
  x = width / 2
  y = height / 2
  i = 10  # num of steps rob will take

  def __init__(self, root):
    #define variables
    self.position = "north"
    self.root = root
    self.root.title("HW 7: Robot")
    # create canvas
    self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
    self.canvas.pack()

    # robot on screen
    self.rob_img = tk.PhotoImage(file="robot-32x32.png")
    self.robot = self.canvas.create_image(self.x,
                                          self.y,
                                          image=self.rob_img,
                                          anchor=tk.NW)
    # register events
    print(tuple(self.canvas.coords(self.robot)))

    self.root.bind("<Button-1>", self.move_rob)

  def move_rob(self, event):

    prev = self.canvas.coords(self.robot)

    #check if robot on screen if not restart
    if (prev[0] >= self.width - 24 or prev[1] >= self.height - 24
        or prev[0] <= 24 or prev[1] < 24):
      self.position = "west"
      self.canvas.move(self.robot, self.x - prev[0], self.y - prev[1])
      self.i = 0

    # Move robot around on click
    if self.position == 'south':
      self.canvas.move(self.robot, 0, self.i)
      prev = self.canvas.coords(self.robot)
      self.position = 'west'

    elif self.position == 'west':
      self.canvas.move(self.robot, -self.i, 0)
      prev = self.canvas.coords(self.robot)
      self.position = 'north'

    elif self.position == 'north':
      self.canvas.move(self.robot, 0, -self.i)
      prev = self.canvas.coords(self.robot)
      self.position = 'east'

    elif self.position == 'east':
      self.canvas.move(self.robot, self.i, 0)
      prev = self.canvas.coords(self.robot)
      self.position = 'south'

    self.i += 10
    print(tuple(prev))


if __name__ == '__main__':

  # creates main window and call class
  root = tk.Tk()
  game = Game(root)

  # enter main loop
  root.mainloop()
