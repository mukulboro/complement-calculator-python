from ones_complement import OnesComplement
from nines_complement import NinesComplement
from twos_complement import TwosComplement
from tens_complement import TensComplement
from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Complement Calculator by Mukul Aryal")
window.config(padx="40", pady="40")
window.iconbitmap("icon.ico")


def ones_button():

    ones = OnesComplement(number1.get(), number2.get())
    output_box.delete(1.0, END)
    initial_string = f"""
STEP 1: Making both bits equal in length
{ones.num1}
{ones.num2}

STEP 2: Taking one's complement of second number
{ones.num2}------>{ones.complement}

STEP 3: Adding complement of second number to first number
{ones.num1}
+{ones.complement}
_________________
{ones.sum}

STEP 4: Checking for overflow
"""

    if ones.check_overflow():
        result_string = f"""
Since carry occurs(i.e. {ones.carry_over}), add carry with remaining bits(i.e. {ones.to_be_added})

{ones.to_be_added}
+{ones.carry_over}
________________
{ones.final_result}

The required answer is: {ones.final_result}
"""

    else:
        result_string = f"""
    Since there is no overflow, negative of one's complement is answer.
    The required answer is: {ones.final_result}
    """

    final_string = initial_string + result_string
    output_box.insert(INSERT, final_string)


def nines_button():
    nines = NinesComplement(number1.get(), number2.get())
    output_box.delete(1.0, END)
    initial_string = f"""
STEP 1: Making both bits equal in length
{nines.num1}
{nines.num2}

STEP 2: Taking nine's complement of second number
{nines.num2}------>{nines.complement}

STEP 3: Adding complement of second number to first number
{nines.num1}
+{nines.complement}
_________________
{nines.sum}

STEP 4: Checking for overflow
"""

    if nines.check_overflow():
        result_string = f"""
Since carry occurs(i.e. {nines.carry_over}), add carry with remaining bits(i.e. {nines.to_be_added})

{nines.to_be_added}
+{nines.carry_over}
________________
{nines.final_result}

The required answer is: {nines.final_result}
"""

    else:
        result_string = f"""
    Since there is no overflow, negative of one's complement is answer.
    The required answer is: {nines.final_result}
    """

    final_string = initial_string + result_string
    output_box.insert(INSERT, final_string)


def twos_button():
    twos = TwosComplement(number1.get(), number2.get())
    output_box.delete(1.0, END)
    initial_string = f"""                                           
STEP 1: Making both bits equal in length                        
{twos.num1}                                                     
{twos.num2}                                                     
                                                                    
STEP 2: Taking two's complement of second number                
{twos.ones}                                                    
+ 1                                                             
___________                                                     
{twos.complement}                                              
                                                                    
STEP 3: Adding complement of second number to first number      
{twos.num1}                                                    
+{twos.complement}                                              
__________                                                      
{twos.sum}                                                     
                                                                    
STEP 4: Checking for overflow                                   
    """

    if twos.check_overflow():
        result_string = f"""                                        
Overflow occurs. So ignoring overflown digit                    
The required answer is: {twos.final_result}                     
    """
    else:
        result_string = f"""                                        
No overflow occurs. So, taking negative of 2's complement       
The required answer is -{twos.final_result}                     
    """
    final_string = initial_string + result_string
    output_box.insert(INSERT, final_string)


def tens_button():
    tens = TensComplement(number1.get(), number2.get())
    output_box.delete(1.0, END)
    initial_string = f"""                                           
STEP 1: Making both bits equal in length                        
{tens.num1}                                                     
{tens.num2}                                                     

STEP 2: Taking ten's complement of second number                
{tens.ones}                                                    
+ 1                                                             
___________                                                     
{tens.complement}                                              

STEP 3: Adding complement of second number to first number      
{tens.num1}                                                    
+{tens.complement}                                              
__________                                                      
{tens.sum}                                                     

STEP 4: Checking for overflow                                   
    """

    if tens.check_overflow():
        result_string = f"""                                        
Overflow occurs. So ignoring overflown digit                    
The required answer is: {tens.final_result}                     
    """
    else:
        result_string = f"""                                        
No overflow occurs. So, taking negative of 2's complement       
The required answer is -{tens.final_result}                     
    """
    final_string = initial_string + result_string
    output_box.insert(INSERT, final_string)


number1 = Entry(width=30)
number1.grid(column=1, row= 1)
number1.focus()

minus_label = Label(text="-", padx=40, font=("Arial", 20, "bold"))
minus_label.grid(column=2, row=1)

number2 = Entry(width=30)
number2.grid(column=3, row=1)

button1 = Button(text="1's complement", width=20, command=ones_button)
button1.grid(column=1, row=2)

button2 = Button(text="2's complement", width=20, command=twos_button)
button2.grid(column=3, row=2)

button9 = Button(text="9's complement", width=20, command=nines_button)
button9.grid(column=1, row=3)

button10 = Button(text="10's complement", width=20, command=tens_button)
button10.grid(column=3, row=3)

empty_label = Label(pady=10)
empty_label.grid(column=0, row=4)

output_box = scrolledtext.ScrolledText(window, height=20, width=60)
output_box.grid(column=0, row=5, columnspan=4)

window.mainloop()





