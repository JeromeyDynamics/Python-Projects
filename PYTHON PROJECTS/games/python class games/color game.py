import tkinter #python GUI
import random

colors = ['Red', 'Blue', 'Green', 'Pink', 'Yellow', 'Orange', 'White', 'Purple', 'Black', 'Brown']
timeleft = 30
score = 0

def startGame(event):
    if timeleft == 30:
        countdown() #start countdown timer

    nextColor() #show the color/next color/next color.....

def nextColor():#when ever enter then runs
    global score #global means that you can use anywhereoutside but, have to call again to use in another def(still haft to make it)
    global timeleft

    if timeleft > 0: #checking that the game is currently in play
        text.focus_set() #makes the text box active
        if text.get().lower() == colors[1].lower(): #.lower() makes it so that they have to  wright in lowercase
            score+=1
        text.delete(0, tkinter.END) #deletes text
        random.shuffle(colors)
        label.config(fg = str(colors[1]), text = str(colors[0])) #figure is the color and text is the text(figure doesn't work so use fg)
        scoreLabel.config(text = "Score: " + str(score))

def countdown():
    global timeleft #creates a global variable called timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: " + str(timeleft))
        timeLabel.after(1000, countdown) #run function again after 1 second


root = tkinter.Tk() #named our GUI (graphical user interface) tool root

root.title("The Color Game") #sets the title of the GUI

root.geometry("400x400") #set the size of the GUI

instructions = tkinter.Label(root, text = "Type in the color of the word, not the word text", font = ('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text = "Press enter to start", font = ('Helvetica', 12)) #after pressing enter turns to score
scoreLabel.pack()

timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), font = ('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font = ('Helvetica', 50))
label.pack()

text = tkinter.Entry(root) #creates text box
text.pack()

root.bind('<Return>', startGame) #program the return key to call the startGame function

text.focus_set()

root.mainloop() #starts the GUI