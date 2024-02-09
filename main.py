import tkinter
from tkinter import *
import pygame
from pygame import mixer

###Sound###

# Loading the songs/sound effects
pygame.mixer.pre_init(28800, -16, 2, 2048) # setup mixer to avoid sound lag
mixer.init()

try:
	sound = mixer.Sound('button_click.wav')
	sound2 = mixer.Sound('exit_sound.mp3')
	# Setting the volume
	mixer.music.set_volume(0.7)
except:
	print("couldn't load sound files")

def clickSound():
	sound = mixer.Sound('button_click.wav')
	sound.set_volume(0.1)
	sound.play()

def exitSound():
	sound = mixer.Sound('exit_sound.mp3')
	sound.set_volume(0.1)
	sound.play()
###############
###Functions###

def rectangleWindow():
	def clearEntry():
		clickSound()
		user_entry_length.delete(0, END)
		user_entry_length.insert(0, "")
		user_entry_width.delete(0, END)
		user_entry_width.insert(0, "")

	def getUserEntryLength():
		value = 0
		try :
			# The get() could throw an exception if the user
			# enters a non-numerical answer, so handle it!
			value = float(user_entry_length.get())
		except ValueError:
			output_label.configure(text="Error! Enter a valid number.Please try again.")
			# clear the entry box
			clearEntry()
		else :
			pass

		finally :
			return value

	def getUserEntryWidth():
		value = 0
		try :
			# The get() could throw an exception if the user
			# enters a non-numerical answer, so handle it!
			value = float(user_entry_width.get())
		except ValueError:
			output_label.configure(text="Error! Enter a valid number.Please try again.")
			# clear the entry box
			clearEntry()
			value = 0
		else :
			pass
		finally :
			return value

	def calcArea() :
		clickSound()
		lgA = getUserEntryLength()
		wdA = getUserEntryWidth()
		if lgA == 0 or wdA == 0:
			output_label.configure(text="Error! Enter a valid number.Please try again.")
		else:
			# wdA = float(user_entry_width.get())
			str_area_ans = str(lgA * wdA)
			output_label.configure(text='The Area is ' + str_area_ans + 'cm²')

	def calcPerim():
		clickSound()
		lgP = getUserEntryLength()
		wdP = getUserEntryWidth()
		if lgP == 0 or wdP == 0:
			output_label.configure(text="Error! Enter a valid number.Please try again.")
		else:
			str_perim_ans = str((lgP*2) + (wdP*2))
			output_label.configure(text='The Perimeter is ' + str_perim_ans + 'cm')

	def closeSquareWindow():
		exitSound()
		rectangle_window.destroy()

	rectangle_window = Toplevel(window)
	rectangle_window.geometry("450x450")
	rectangle_window.title("Rectangle Formulas")
	label3 = Label(rectangle_window, text="Rectangle", font=('Helvetica', 28, 'underline'))
	label4 = Label(rectangle_window, text="Input length and width below", font=('Helvetica', 16))
	label3.grid(row=2, column=0, columnspan=2)
	label4.grid(row=6, column=0, sticky=W, pady=5)
	# length width user entries
	user_entry_length = Entry(rectangle_window, bd=2)
	user_entry_length.insert(0, "Length (cm)")
	user_entry_length.grid(row=8, column=0, padx=5)
	user_entry_width = Entry(rectangle_window, bd=2)
	user_entry_width.insert(0, "Width (cm)")
	user_entry_width.grid(row=10, column=0, padx=5)
	# clear button
	b_clear = Button(rectangle_window, text="clear", borderwidth=4, relief="ridge", command=clearEntry)
	b_clear.grid(row=12, column=0, padx=5, pady=5)
	b_clear.config(height=1, width=4)
	# calculate area button
	rec_area_btn = Button(rectangle_window, text='Calculate Area', borderwidth=4, relief="raised", bg='lightgray', fg='black', command=calcArea)
	rec_area_btn.grid(row=16, column=0,columnspan=2,padx=5, sticky=W)
	rec_area_btn.config(height=2, width=15)
	# image
	img2 = PhotoImage(file="square.gif")
	photoLabel2 = Label(rectangle_window, image=img2)
	photoLabel2.grid(row=15, rowspan=2, column=1, sticky=W)
	photoLabel2.image = img2
	# calc perimeter button
	rec_perim_btn = Button(rectangle_window, text='Calculate Perimeter', borderwidth=4, relief="raised", bg='lightgray', fg='black', command=calcPerim)
	rec_perim_btn.grid(row=15, column=0, pady=15, padx=5, sticky=W)
	rec_perim_btn.config(height=2, width=15)
	# output
	output_label = tkinter.Label(rectangle_window, text="Enter numbers, then click either button", font=('Helvetica', 16))
	output_label.grid(row=18, column=0, columnspan=2, sticky=W, pady=15)
	window.grid_rowconfigure(3, minsize=50)
	# quit button
	close_rectangle_window_btn = Button(rectangle_window, text='Close Window', borderwidth=6, relief="raised", bg='lightgray', fg='black', command=closeSquareWindow)
	close_rectangle_window_btn.grid(row=23, column=1, columnspan=2, )
	close_rectangle_window_btn.config(height=2, width=15)
###############

def circleWindow():

	def clearEntryC():
		clickSound()
		user_entry_radius.delete(0, END)
		user_entry_radius.insert(0, "")

	def getUserEntryRadius():
		value = 0
		try :
			# The get() could throw an exception if the user
			# enters a non-numerical answer, so handle it!
			value = float(user_entry_radius.get())
		except ValueError:
			output_label.configure(text="Error! Enter a valid number.Please try again.")
			# clear the entry box
			clearEntryC()
		else :
			calcAreaC()

		finally :
			return value

	def calcAreaC():
		clickSound()
		r = getUserEntryRadius()
		if r == 0:
			output_label.configure(text="Error! Enter a valid number.Please try again.")
		else:
			str_areaT_ans = str((3.14)*(r**2))
			output_label.configure(text='The Area is ' + str_areaT_ans + 'cm²')

	def calcCircum():
		clickSound()
		r = getUserEntryRadius()
		if r == 0:
			output_label.configure(text="Error! Enter a valid number.Please try again.")
		else :

			str_circum_ans = str((2)*(3.14)*(r))
			output_label.configure(text='The Circumference is ' + str_circum_ans + 'cm')

	def closeCircleWindow():
		exitSound()
		circle_window.destroy()
	circle_window = Toplevel(window)
	circle_window.geometry("450x400")
	circle_window.configure(bg='lightblue')
	circle_window.title("Circle Formulas")
	# entry Labels
	label5 = Label(circle_window, text="Circle", font=('Helvetica', 28, 'underline'))
	label5.config(bg='lightblue')
	label6 = Label(circle_window, text="Input radius below", font=('Helvetica', 16))
	label6.config(bg='lightblue')
	label5.grid(row=2, column=0, columnspan=2)
	label6.grid(row=6, column=0, sticky=W, pady=5)
	# user input
	user_entry_radius = Entry(circle_window, bd=2)
	user_entry_radius.insert(0, "radius (cm)")
	user_entry_radius.grid(row=8, column=0, padx=5)
	# image
	img3 = PhotoImage(file="circle.gif")
	photoLabel3= Label(circle_window, image=img3)
	photoLabel3.grid(row=15, rowspan=2, column=1, sticky=W)
	photoLabel3.image = img3
	# clear button
	b_clear = Button(circle_window, text="clear", borderwidth=4, relief="ridge", command=clearEntryC)
	b_clear.grid(row=12, column=0, padx=5, pady=5)
	b_clear.config(height=1, width=4)
	# calculate area button
	rec_area_btn = Button(circle_window, text='Calculate Area', borderwidth=4, relief="raised", bg='lightgray', fg='black', command=calcAreaC)
	rec_area_btn.grid(row=16, column=0, columnspan=2, padx=5, sticky=W)
	rec_area_btn.config(height=2, width=18)
	# calc circumference
	rec_perim_btn = Button(circle_window, text='Calculate Circumference', borderwidth=4, relief="raised", bg='lightgray', fg='black', command=calcCircum)
	rec_perim_btn.grid(row=15, column=0, pady=15, padx=5, sticky=W)
	rec_perim_btn.config(height=2, width=18)
	# output
	output_label = tkinter.Label(circle_window, text="Enter numbers, then click either button", font=('Helvetica', 16))
	output_label.config(bg='lightblue')
	output_label.grid(row=25, column=0, columnspan=2, sticky=W, pady=15)
	window.grid_rowconfigure(3, minsize=50)
	# quit button
	close_rectangle_window_btn = Button(circle_window, text='Close Window', borderwidth=6, relief="raised", bg='lightgray', fg='black', command=closeCircleWindow)
	close_rectangle_window_btn.grid(row=28, column=1, columnspan=2, )
	close_rectangle_window_btn.config(height=2, width=12)
###############

window = Tk()
# title
window.title("Tk dropdown example for calculations")
# Size
window.geometry('500x500')
window.configure(bg='lightgray')

# simple label
label1 = Label(window, text="Shape Formula Solver", font=('Helvetica', 32, 'underline'))
label1.configure(bg='lightgray')
label2 = Label(window, text="For some of your calculation needs", font=('Helvetica', 16), fg="black")
label2.configure(pady=5, bg='lightgray')
label1.pack()
label2.pack()
#################

tkvar = StringVar(window)

# Dictionary with options
choices = {'Rectangle','Circle'}
tkvar.set('Please choose a shape.')  # set the default option

# The drop down menu
label0 = Label(window, text="Supported Shapes", font=('Helvetica', 14))
label0.configure(bg='lightgray')
label0.pack()
optionmenu = OptionMenu(window, tkvar, *choices)
optionmenu.config(width=30)
optionmenu.configure(bg='lightblue')
optionmenu.pack()

# on change dropdown value
def change_dropdown(*args) :
	selection = tkvar.get()
	print('The current selection is %s.' % selection)
	if selection == "Rectangle" :
		rectangleWindow()
		clickSound()

	elif selection == "Circle":
		circleWindow()
		clickSound()

def closeWindow():
	window.destroy()

close_window_btn = Button(window, text='Quit', borderwidth=4, relief="raised", bg='lightgray', fg='black', command=closeWindow)
close_window_btn.pack(side=BOTTOM)
close_window_btn.config(height=2, width=15, bg='lightblue')

# link function to change dropdown
tkvar.trace('w', change_dropdown)

##########
img1 = PhotoImage(file="shapes.gif")
photoLabel = Label(window, image=img1)
# resize image
photoLabel.pack(pady=50)

# start the GUI
window.mainloop()
