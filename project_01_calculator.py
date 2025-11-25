from tkinter import *
import math
from pygame import mixer                                             # mixer module helps playing any audio sound
import speech_recognition



mixer.init()

def click(value):
    ex = entryField.get()
    answer = ''
    try:
        if value == 'C' :                                           
            ex = ex[0:len(ex)-1]                                      # splitting the entred numbers and deleting from the end
            entryField.delete(0,END)
            entryField.insert(0,ex)
            return

        elif value == 'CE' :                                          # deleting everything
            entryField.delete(0,END)
        
        elif value == '√' :
            answer = math.sqrt(eval(ex))                               # eval() works for both int() and float()
        
        elif value == 'π' :
            answer = math.pi
        
        elif value == "cosθ" :                                       
            answer = math.cos(math.radians(eval(ex)))                        
                                    
        elif value == "tanθ" :                                       
            answer = math.tan(math.radians(eval(ex))) 
            
        elif value == "sinθ" :                                     
            answer = math.sin(math.radians(eval(ex))) 
        
        elif value == '2π' :
            answer = 2 * math.pi
        
        elif value == "cosh" :
            answer = math.cosh(eval(ex))
        
        elif value == "tanh" :
            answer = math.tanh(eval(ex))
        
        elif value == "sinh" :
            answer = math.sinh(eval(ex))
        
        elif value == chr(8731) :
            answer = round(eval(ex)**(1/3), 2)
        
        elif value == 'x\u02b8' :                       # x**y =7**2=49
            entryField.insert(END,'**')
            return
        
        elif value == 'x\u00b3' :                        # x³
            answer = eval(ex)**3
        
        elif value == 'x\u00b2' :                        # x²
            answer = eval(ex)**2
        
        elif value == 'ln' :
            answer = math.log2(eval(ex))
        
        elif value == 'deg' :
            answer = math.degrees(eval(ex))
        
        elif value == 'rad' :
            answer = math.radians(eval(ex))
        
        elif value == 'e' :
            answer = math.e 
        
        elif value == 'log₁₀' :
            answer = math.log10(eval(ex))
        
        elif value == chr(247) :
            entryField.insert(END, "/")
            return
        
        elif value == '=' :
            answer = eval(ex)
            
        elif value == "x!":
            answer = math.factorial(int(eval(ex)))
        
        else:
            entryField.insert(END,value)
            return
                
        entryField.delete(0,END)
        entryField.insert(0,answer)
        
    except SyntaxError:
        pass

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    l=math.lcm(a,b)
    return l

def hcf(a,b):
    h=math.gcd(a,b)
    return h

operations = {'ADD' : add, 'ADDITION' : add, 'SUM' : add, 'PLUS' : add,
              'SUBTRUCTION' : sub, 'DIFFERENCE' : sub, 'MINUS' : sub, 'SUBSTRACT' : sub,
              'PRODUCT' : mul, 'MULTIPLICATION' : mul, 'MULTIPLY' : mul,
              'DIVISION': div, 'DIV' : div, 'DIVIDE' : div,
              'LCM' : lcm, 'HCF' : hcf,
              'MOD' : mod, 'REMAINDER' : mod, 'MODULUS' : mod} 

def findNumbers(t):
    l = []
    for num in t:
        try:
            l.append(float(num))
        except ValueError:
            pass
    return l
    

def audio():
    mixer.music.load('project_01_start.mp3')
    mixer.music.play()
    
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        #print("Say something:")
        #audio = sr.listen(m)
        try:
            sr.adjust_for_ambient_noise(m, duration=1)
            voice = sr.listen(m)
            text = sr.recognize_google(voice)
            print("You said:", text)
            #print(text)
            mixer.music.load('project_01_end.mp3')
            mixer.music.play()
            text_list = text.split(' ')
            #print(text_list)
            
            for word in text_list:
                if word.upper() in operations.keys():
                    l = findNumbers(text_list)
                    print(l)
                    result = operations[word.upper()](l[0], l[1]) # a and b
                    entryField.delete(0, END)
                    entryField.insert(END, result)
                
                else:                                       # unnecessary line that has nor numbers will be passed
                    pass
                
        #     for word in text_list:
        #         key = word.upper()
        #         if key in operations.keys():
        #             l = findNumbers(text_list)
        #             print("Numbers found:", l)
        #             if len(l) >= 2:
        #                 result = operations[key](l[0], l[1])
        #                 entryField.delete(0, END)
        #                 entryField.insert(END, result)
        #             else:
        #                 print("Not enough numbers found to perform operation.")
        #             break  # stop after first operation word found
            
        except:
            pass    
    

        
root = Tk()                                                   # window creat korar jonno
root.config(bg= "#000000")
root.geometry('675x499+100+100')
root.title("My first GUI project: Scientific Calculator")
root.resizable(False, False)

#label = Label(root, text = "Scientific Calculator", font=('Arial', 15), fg="#D8BABA")
#label.grid(pady=20)

logoimage= PhotoImage(file="project_01_logo3.png")
logolabel = Label(root, image=logoimage, bg= "#000000")
logolabel.grid(row=0, column=0)

entryField = Entry(root, font=('arial', 25, 'bold'),
                   bg = "#000000", fg = 'orange',
                   bd=7, relief=SUNKEN, width=27)
entryField.grid(row=0, column=0, columnspan=8, pady=(15,10), ipady=10)                               # row and column are 0 because this is the first thing will be added in our window


micimage= PhotoImage(file="project_01_mic.png")
micbutton = Button(root, image=micimage, bd=0, bg = "#000000", activebackground="#212323",
                   command=audio)
micbutton.grid(row=0, column=7)



orange_buttons = {"π","2π", "cosθ", "tanθ", "sinθ", "cosh", "tanh", "sinh", "ln", "log₁₀", "deg", "rad", "e",
                  chr(8731), "x\u02b8", "x\u00b3", "x\u00b2","(", ")", "x!"}

button_text_list = [
    "C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00b3", "x\u00b2",
    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"
]                                                                               # chr(8731) → cube root symbol (∛)
                                                                                # chr(247) → division symbol (÷)
                                                                                # x\u02b8 → xˈ (modifier letter prime)
                                                                                # x\u00b3 → x³
                                                                                # x\u00b2 → x²

rowvalue = 1
columnvalue = 0

for i in button_text_list:
    color = "orange" if i in orange_buttons else "white"                # Color selection for scientific functions

    button = Button(
        root,
        width=5,
        height=2,
        relief='raise',
        text=i,
        bg="#191717",
        fg=color,
        font=('arial', 18),
        activebackground="#212323",
        command=lambda button=i: click(button)
    )

    button.grid(row=rowvalue, column=columnvalue, padx=2, pady=2)

    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0


root.mainloop()                                     # window contineously stable rakhar jonno