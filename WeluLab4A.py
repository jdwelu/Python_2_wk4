#!/usr/bin/env python3

import tkinter

class MKWindow:
        def __init__(self):
                # Create the main window and adjust the size.
                self.mainWindow = tkinter.Tk()
                self.mainWindow.geometry("200x175")

                # Create the first entry field "Length" and lebel it.
                self.label0 = tkinter.Label(self.mainWindow, text="Length  (ft.)")
                self.lengthEntry = tkinter.Entry(self.mainWindow)

                # Create the second entry field "Width" and lebel it.
                self.label1 = tkinter.Label(self.mainWindow, text="Width  (ft.)")
                self.widthEntry = tkinter.Entry(self.mainWindow)

                # Create the third entry field "Price" and label it.
                self.label2 = tkinter.Label(self.mainWindow, text="Price  (per sqft.)")
                self.priceEntry = tkinter.Entry(self.mainWindow)

                # Create the button. I labelled it "Calculate" instead of "price."
                self.convertButton = tkinter.Button(self.mainWindow, text="Calculate", command=self.doConversion)
                self.labelValue = tkinter.StringVar()
                self.labelValue.set("0")
                self.outputLabel = tkinter.Label(self.mainWindow, textvariable=self.labelValue)

                # Display the fields and button.
                self.label0.pack()
                self.lengthEntry.pack()

                self.label1.pack()
                self.widthEntry.pack()

                self.label2.pack()
                self.priceEntry.pack()
                
                self.convertButton.pack()
                self.outputLabel.pack()

                # Start and display main window.
                tkinter.mainloop()

        def doConversion(self):
                # Check the float values entered.
                try:
                    length = float(self.lengthEntry.get())
                    width = float(self.widthEntry.get())
                    price = float(self.priceEntry.get())
                
                    priceTotal = length * width * price
                    self.labelValue.set("Total Price: $" + str(format(priceTotal, ".2f")))
                # Just used an except to handle all exceptions.
                except:
                    self.labelValue.set("Invalid Data Entry")
                    

myWindow = MKWindow()





