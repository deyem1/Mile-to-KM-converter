from tkinter import *
window = Tk()
window.title = ("Mile to Kilometer Converter")
#window.minsize(width=500, height=500)
window.config(padx= 20, pady=20)

def action():

    new_text = entry.get()
    print("converted to miles")
    converted_text = float(new_text)*1.609349
    km_label.config(text = converted_text)

#Entries
entry = Entry(width=7)
# #Add some text to begin with
# entry.insert(END, string="Miles.")
#Gets text in entry
print(entry.get())
entry.grid(column= 2, row = 1)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(column= 3, row = 1)

#Labels
equal_to_label = Label(text="is equal to ")
equal_to_label.grid(column= 1, row = 2)

#Labels
km_label = Label(text=" 0 ")
#km_label.config(text= converted_text)
km_label.grid(column= 2, row = 2)

#Labels
unit_label = Label(text="km")
unit_label.grid(column= 3, row = 2)

#Buttons


#calls action() when pressed
button = Button(text="Convert", command=action)
button.grid(column= 2, row = 3)



#Labels
unit_label = Label(text="by AB")
unit_label.grid(column= 3, row = 5)
unit_label.config(pady=5, padx=5)


window.mainloop()