#modules
from tkinter import *
import pickle

#root window
root=Tk()

#to clear the entry box
def clear():
    c_var.set("")
    d_var.set("")
    h_var.set("")
    w_var.set("")
    a_var.set("")
    m_var.set("")

#to predict mpg
def calculate_mpg():
    c=c_var.get()
    d=d_var.get()
    h=h_var.get()
    w=w_var.get()
    a=a_var.get()
    m=m_var.get()
    clear()
    fp=open("model.pkl","rb")
    model=pickle.load(fp)
    mpg=model.predict(np.array([c,d,h,w,a,m]).reshape(1,-1))
    t=Toplevel()
    label=Label(t,text=f"Your Car's \n Predicted Mileage is \n{mpg[0]:.2f} Miles Per Gallon.")
    label.config(bg='#123456', fg='wheat', font=('monospace', 35, 'bold'),height=5,width=21)
    label.pack()
    button=Button(t,text="Quit",command=t.destroy)
    button.config(bg='wheat', fg='red', font=('monospace', 35, 'bold'),height=1,width=21)
    button.pack()
    t.resizable(0,0)
    
    
#variables   
c_var=DoubleVar()
d_var=DoubleVar()
h_var=DoubleVar()
w_var=DoubleVar()
a_var=DoubleVar()
m_var=DoubleVar()

clear()

#labels
c_label=Label(root,text="Cylinders:")
d_label=Label(root,text="Displacement:")
h_label=Label(root,text="Horsepower:")
w_label=Label(root,text="Weight:")
a_label=Label(root,text="Accleration:")
m_label=Label(root,text="Model Year:")

# entry boxes
c_entry=Entry(root,textvariable=c_var)
d_entry=Entry(root,textvariable=d_var)
h_entry=Entry(root,textvariable=h_var)
w_entry=Entry(root,textvariable=w_var)
a_entry=Entry(root,textvariable=a_var)
m_entry=Entry(root,textvariable=m_var)

#buttons
button_1=Button(root,text="Calculate MPG",command=calculate_mpg)
button_2=Button(root,text="Quit",command=root.destroy)

#packing all widgets
c_label.grid(row=1,column=1,)
c_entry.grid(row=1,column=2,)
d_label.grid(row=2,column=1,)
d_entry.grid(row=2,column=2,)
h_label.grid(row=3,column=1,)
h_entry.grid(row=3,column=2,)
w_label.grid(row=4,column=1,)
w_entry.grid(row=4,column=2,)
a_label.grid(row=5,column=1,)
a_entry.grid(row=5,column=2,)
m_label.grid(row=6,column=1,)
m_entry.grid(row=6,column=2,)
button_1.grid(row=7,column=1,columnspan=2,sticky=W+E+N+S)
button_2.grid(row=8,column=1,columnspan=2,sticky=W+E+N+S)

c_entry.focus()

#configurations
c_label.config(bg="wheat",fg='#123456', font=('monospace', 25, 'bold'))
d_label.config(bg="wheat",fg='#123456', font=('monospace', 25, 'bold'))
h_label.config(bg="wheat",fg='#123456', font=('monospace', 25, 'bold'))
w_label.config(bg="wheat",fg='#123456', font=('monospace', 25, 'bold'))
a_label.config(bg="wheat",fg='#123456', font=('monospace', 25, 'bold'))
m_label.config(bg="wheat",fg='#123456', font=('monospace', 25, 'bold'))
c_entry.config(bg='#123456', fg='wheat', font=('monospace', 25, 'bold'))
d_entry.config(bg='#123456', fg='wheat', font=('monospace', 25, 'bold'))
h_entry.config(bg='#123456', fg='wheat', font=('monospace', 25, 'bold'))
w_entry.config(bg='#123456', fg='wheat', font=('monospace', 25, 'bold'))
a_entry.config(bg='#123456', fg='wheat', font=('monospace', 25, 'bold'))
m_entry.config(bg='#123456', fg='wheat', font=('monospace', 25, 'bold'))
button_1.config(bg='wheat', fg='green', font=('monospace', 25, 'bold'),relief="raised")
button_2.config(bg='wheat', fg='red', font=('monospace', 25, 'bold'),relief="raised")
root.config(bg="wheat")
root.title("MPG Prediction")
root.resizable(0,0)

root.mainloop()
