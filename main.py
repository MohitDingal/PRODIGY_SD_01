import tkinter as tk

def conversion():
    ans1 = ""
    ans2 = ""
    value = float(temp.get())
    value1 = 0
    value2 = 0
    u = unit.get()
    u = u.upper()
    if u == 'K':
        value1 = 1.8 * (value - 273) + 32
        value2 = value - 273.15
        unit1 = 'F'
        unit2 = 'C'
    elif u == 'F':
        value1 = ((value-32)*5)/9
        value2 =  ((value - 32)*5/9) + 273.15
        unit1 = 'C'
        unit2 = 'K'
    else:
        value1 = value*(9/5)+32
        value2 = value + 273.15
        unit1 = 'F'
        unit2 = 'K'
    text1.config(text = "The temperature is {:0.2f} {}".format(value1,unit1))
    text2.config(text = "The temperature is {:0.2f} {}".format(value2,unit2))


root = tk.Tk()
root.geometry("400x400")
temp_value = tk.Label(root,text ="Temperature: ", font=("Arial","13"))
temp_value.pack()
temp = tk.Entry(root,width = 25,font=("Arial","13"))
temp.pack(padx=5,pady=10)

temp_type= tk.Label(root,text = "Enter the unit of measurement: ",font=("Arial","13"))
temp_type.pack()
unit = tk.Entry(root, width = 25,font=("Arial","13"))
unit.pack(padx=5,pady=10)

convert = tk.Button(root,text = "Convert", height=1,width = 8, command = conversion ,font=("Arial bold","13"), bg='red')
convert.pack(pady = 5)
textlabel = tk.Label(root,text ="The converted temperatures are: ", font = ("Arial","13"))
textlabel.pack()
text1 = tk.Label(root,font = ("Arial","12"))
text1.pack(padx=5,pady=10)
text2 = tk.Label(root,font = ("Arial","12"))
text2.pack(padx=5,pady=10)
root.mainloop()
