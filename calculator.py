import tkinter as tk

calc=""

def add_to_calc(x):
    global calc
    calc+=str(x)
    tf.delete(1.0,"end")
    tf.insert(1.0,calc)

def real_calc():
    global calc
    try:
        res = str(eval(calc))
        calc=""
        tf.delete(1.0,"end")
        tf.insert(1.0,res)
    except:
        clear()
        tf.insert(1.0,"ERROR")

def clear():
    global calc
    calc=""
    tf.delete(1.0,"end")

root=tk.Tk()
root.geometry("300x275")
tf=tk.Text(root, height=2,width=16, font=("Arial",24))
tf.grid(columnspan=5)

bt1=tk.Button(root, text="1", command= lambda: add_to_calc(1), width=5, font=("Arial",14))
bt1.grid(row=2,column=1)

bt2=tk.Button(root, text="2", command= lambda: add_to_calc(2), width=5, font=("Arial",14))
bt2.grid(row=2,column=2)

bt3=tk.Button(root, text="3", command= lambda: add_to_calc(3), width=5, font=("Arial",14))
bt3.grid(row=2,column=3)

bt4=tk.Button(root, text="4", command= lambda: add_to_calc(4), width=5, font=("Arial",14))
bt4.grid(row=3,column=1)

bt5=tk.Button(root, text="5", command= lambda: add_to_calc(5), width=5, font=("Arial",14))
bt5.grid(row=3,column=2)

bt6=tk.Button(root, text="6", command= lambda: add_to_calc(6), width=5, font=("Arial",14))
bt6.grid(row=3,column=3)

bt7=tk.Button(root, text="7", command= lambda: add_to_calc(7), width=5, font=("Arial",14))
bt7.grid(row=4,column=1)

bt8=tk.Button(root, text="8", command= lambda: add_to_calc(8), width=5, font=("Arial",14))
bt8.grid(row=4,column=2)

bt9=tk.Button(root, text="9", command= lambda: add_to_calc(9), width=5, font=("Arial",14))
bt9.grid(row=4,column=3)

bt0=tk.Button(root, text="0", command= lambda: add_to_calc(0), width=5, font=("Arial",14))
bt0.grid(row=5,column=2)

bt_plus=tk.Button(root, text="+", command= lambda: add_to_calc("+"), width=5, font=("Arial",14))
bt_plus.grid(row=2,column=4)

bt_minus=tk.Button(root, text="-", command= lambda: add_to_calc("-"), width=5, font=("Arial",14))
bt_minus.grid(row=3,column=4)

bt_mul=tk.Button(root, text="*", command= lambda: add_to_calc("*"), width=5, font=("Arial",14))
bt_mul.grid(row=4,column=4)

bt_div=tk.Button(root, text="/", command= lambda: add_to_calc("/"), width=5, font=("Arial",14))
bt_div.grid(row=5,column=4)

bt_op=tk.Button(root, text="(", command= lambda: add_to_calc("("), width=5, font=("Arial",14))
bt_op.grid(row=5,column=1)

bt_cl=tk.Button(root, text=")", command= lambda: add_to_calc(")"), width=5, font=("Arial",14))
bt_cl.grid(row=5,column=3)

bt_eq=tk.Button(root, text="=", command= lambda:real_calc(), width=11, font=("Arial",14))
bt_eq.grid(row=6,column=3, columnspan=2)

bt_clear=tk.Button(root, text="C", command=clear, width=11, font=("Arial",14))
bt_clear.grid(row=6,column=1,columnspan=2)

root.mainloop()
