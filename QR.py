import pyqrcode
from tkinter import *
from tkinter import messagebox
def generateQR():
	inputString = enterTextField.get()
	scale = enterScaleField.get()

	if len(scale):

		try:

			scale = int(scale)

		except:
			messagebox.showerror("Error",
				"Scale should be integer value ex: 1, 2, 3 ...")

			return

	else:
		scale = 5

	if len(inputString):
		qrCode = pyqrcode.create(inputStirng)

		savePath = "D:\\QRcode\\" + inputString + "_" + str(scale)

		qrCode.svg(savePath + ".svg", scale = scale)

		qrCode.png(savePath + ".png", scale = scale)

		messagebox.showinfo('Success', "Your QR code is generated and save at this path :" + savePath + ".png/.svg")

	else:
		messagebox.showerror("Error", "Text field is empty")


def clearAll():

	enterTextField.delete(0,END)

	enterTextField.focus_set()

if __name__ == "__main__":

	window = Tk()

	window.configure(background = 'light green')

	window.geometry("600x100")

	window.title("QR CODE GENERATOR")

	enterTextLabel = Label(window, text = "Enter Text",fg = 'black', bg = 'grey')

	enterTextLabel.grid(row = 2, column = 1, sticky = "E", padx = "10", pady = '10')

	enterScaleLabel = Label(window, text = "Enter Scale", fg ='black', bg = 'grey')

	enterScaleLabel.grid(row = 2, column = 4, sticky = "E", padx = "10", pady = "10")

	enterTextField = Entry(window)

	enterTextField.grid(row = 2, column = 2, sticky = "E", ipadx = "60", pady = "10")

	enterScaleField = Entry(window)

	enterScaleField.grid(row = 2, column = 5, sticky = "E", pady = "10")

	generateButton = Button(window, text = "Generate", bg = "red", fg = "black", command = generateQR)

	clearButton = Button(window, text = "Clear", bg = "red", fg = "black", command = clearAll)

	generateButton.grid(row = 3, column = 3)

	clearButton.grid(row = 4, column = 3, pady = "5")

	window.mainloop()

			


