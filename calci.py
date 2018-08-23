# created on 11th August 2018, Saturday

import tkinter as tk

class Calculator(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.input()
		self.labelandButtons()

	def input(self):
		self.spacelabel = tk.Label(root,text=" ").pack()
		self.e1 = tk.Entry(root)
		self.e1.pack(side="top", anchor="w")
		self.e2 = tk.Entry(root)
		self.e2.pack(side="top", anchor="w")		

	def labelandButtons(self):
		self.ansLabel = tk.Label(root)
		self.ansLabel.pack(side="bottom", anchor="w")

		self.add = tk.Button(root, text="+", command=self.add).pack(side="left")
		self.subtract = tk.Button(root, text="-", command=self.subtract).pack(side="left")
		self.multiply = tk.Button(root, text="*", command=self.multiply).pack(side="left")
		self.divide = tk.Button(root, text="/", command=self.divide).pack(side="left")
		self.moduluss= tk.Button(root, text="%", command=self.modulus).pack(side="left")
		
	def add(self):
		result = float(self.e1.get()) + float(self.e2.get())
		self.ansLabel.configure(text= "Result: " + str(result))
	def subtract(self):
		result = float(self.e1.get()) - float(self.e2.get())
		self.ansLabel.configure(text= "Result: " + str(result))
	def multiply(self):
		result = float(self.e1.get()) * float(self.e2.get())
		self.ansLabel.configure(text= "Result: " + str(result))
	def divide(self):
		result = float(self.e1.get()) / float(self.e2.get())
		self.ansLabel.configure(text= "Result: " + str(result))
	def modulus(self):
		result = float(self.e1.get()) % float(self.e2.get())
		self.ansLabel.configure(text= "Result: " + str(result))

root = tk.Tk()
root.title("Calculator")
root.geometry("165x180")
root.resizable(width=False, height=False)
app = Calculator(master= root)
app.mainloop()