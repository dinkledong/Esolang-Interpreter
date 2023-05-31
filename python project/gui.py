from tkinter import *
import webbrowser
import fish
import brain



def main():
    window = Tk()
    window.title("Esolang Interpreter")
    window.geometry('1280x720')
    window.configure(bg="black")
    frame=Frame(window,bg="black")
    frame.pack(side="top", expand=True, fill="both")

    mainMenu(frame)

    window.mainloop()

def mainMenu(frame):
    clearFrame(frame)
    
    lbl = Label(frame, text="Esolang Interpreter", font=("MS Comic Sans", 40))  
    lbl.configure(bg="black",fg="white",justify=CENTER)
    lbl.grid(column=1, row=0,padx=100,pady=20)  

    txtvalue="Esoteric programming languages (Esolangs) are a type of proggraming languages designed to experiment\nwith weird ideas, to be hard to program in, or as a joke, rather than for practical use. \n\nBelow you can find interpreters for two proliphic esolangs (Fish and Brainf**k) written in python:"
    txt1 = Label(frame, text=txtvalue, font=("Arial Bold", 18),justify="left")  
    txt1.configure(bg="black",fg="white")
    txt1.grid(column=0, row=1,columnspan=3,padx=50,pady=20)  

    btn1 = Button(frame, text="><>",command= lambda: menuFish(frame),height=1,justify=CENTER,font=("Arial Bold", 22),borderwidth=5)  
    btn1.grid(column=0, row=2 ,padx=100,ipadx=20) 

    btn2 = Button(frame, text="Brainf**k",command=lambda: menuBrain(frame),height=1,justify=CENTER,font=("Arial Bold", 22),borderwidth=5)  
    btn2.grid(column=2, row=2 ,padx=50)

    img1 = PhotoImage(file='images/fish2.png')
    pic1 = Label(frame,image=img1)
    pic1.image=img1
    pic1.grid(column=0, row=3 ,padx=10,sticky="e",pady=10)

    img2 = PhotoImage(file='images/brain2.png')
    pic2 = Label(frame,image=img2)
    pic2.image=img2
    pic2.grid(column=2, row=3 ,padx=0,sticky="w",pady=10)
    
    txtvalue=""
    txt1 = Label(frame, text=txtvalue, )  
    txt1.configure(bg="black",fg="white")
    txt1.grid()  

    link1 = Label(frame, text="More info about esolangs can be found at : www.esolangs.org", cursor="hand2",font=("Arial Bold", 18),justify="center")
    link1.configure(bg="black",fg="white")
    link1.grid(column=0, row=4,columnspan=3,padx=50,pady=120)
    link1.bind("<Button-1>", lambda e: webbrowser.open_new("https://esolangs.org/wiki/Main_Page"))

    frame.pack(side="top", expand=True, fill="both")


def menuFish(frame):
    def resetFish():
        interpreter.stack=list()
        interpreter.map=list(list())
        interpreter.x=0
        interpreter.y=0
        interpreter.dir="right"
        interpreter.register=""
        interpreter.stringMode=False
        interpreter.output=""
        interpreter.end=False
        interpreter.skip=False

    def inputCodeFish():
        resetFish()
        interpreter.getMap(inputtxt.get(1.0, "end-1c"))

    def stepCodeFish():
        dummy = list(list())
        if interpreter.map !="" and interpreter.map!=dummy:
            interpreter.step()
            stacktxt.delete(0.0, "end-1c")
            stacktxt.insert(END, interpreter.stack.__str__())
            
            outputtxt.delete(0.0, "end-1c")
            outputtxt.insert(END, interpreter.output.__str__())

            frame.update()
            #print(interpreter.stack,"  ",interpreter.output)
        else:
            print("empty map")
    
    def runCodeFish():
        inputCodeFish()
        #stacktxt.delete(0.0, "end-1c")
        outputtxt.delete(0.0, "end-1c")
        c=0
        while interpreter.end!=True:
            if c>3000:
                break
            stepCodeFish()
            frame.update()
            c+=1
        if c>=3000:
            print ("program stalled ?")
        resetFish()
        

    clearFrame(frame)
    interpreter=fish.Fish()
    

    lbl = Label(frame, text="Fish (><>) Interpreter", font=("MS Comic Sans", 40))  
    lbl.configure(bg="black",fg="white",justify=CENTER)
    lbl.grid(column=0, row=0,padx=100,pady=20,columnspan=6)  

    txtvalue="><> (Fish) is a stack-based, reflective, two-dimensional esoteric programming language. In simple terms it is\na two-dimensional language, meaning the code is not necessarily executed in a linear manner. Using various\ninstructions, the direction the code is read can be changed to either up, down, left or right. It is also a stack-\n-based language, so all operations are performed on a stack. You can also store and retrieve values in the \ncodebox, so making a proper compiler is very hard, if not impossible. (Showcased version of the interpreter\ndoes not support '[]' and ']' operations)"
    txt1 = Label(frame, text=txtvalue, font=("Arial Bold", 16),justify="left")  
    txt1.configure(bg="black",fg="white")
    txt1.grid(column=0, row=1,columnspan=6,padx=50,pady=20)  

    txt2 = Label(frame, text="input:", font=("Arial Bold", 16),justify="left")  
    txt2.configure(bg="black",fg="white")
    txt2.grid(column=0, row=2)  

    inputtxt = Text(frame,height = 9,width = 40)
    inputtxt.configure(bg="white",fg="black")
    inputtxt.grid(column=0, row=3,columnspan=3,rowspan=2,pady=10,padx=20)
    
    txt3 = Label(frame, text="stack:", font=("Arial Bold", 16),justify="left")  
    txt3.configure(bg="black",fg="white")
    txt3.grid(column=5, row=2)  

    stacktxt = Text(frame,height = 3,width = 40)
    stacktxt.configure(bg="white",fg="black")
    stacktxt.grid(column=5, row=3,columnspan=2,pady=10)

    txt4 = Label(frame, text="output:", font=("Arial Bold", 16),justify="left")  
    txt4.configure(bg="black",fg="white")
    txt4.grid(column=5, row=4)  

    v2=Scrollbar(frame, orient='vertical')
    v2.grid(column=6, row=5,sticky=N+S+W)

    outputtxt = Text(frame,height = 6,width = 40,yscrollcommand=v2.set)
    outputtxt.configure(bg="white",fg="black")
    outputtxt.grid(column=5, row=5,columnspan=2,padx=20)

    v2.config(command=outputtxt.yview,background="black")

    inputButton = Button(frame,text = "Input Code",command=inputCodeFish,font=("Arial Bold", 16))
    inputButton.grid(column=0, row=5)

    stepButton = Button(frame,text = "Step",command=stepCodeFish,font=("Arial Bold", 16))
    stepButton.grid(column=1, row=5)

    runButton = Button(frame,text = "Run",command=runCodeFish,font=("Arial Bold", 16))
    runButton.grid(column=2, row=5)


    link1 = Label(frame, text="More info about ><> can be found at : www.esolangs.org", cursor="hand2",font=("Arial Bold", 18),justify="center")
    link1.configure(bg="black",fg="white")
    link1.grid(column=0, row=6,columnspan=6,padx=50,pady=120)
    link1.bind("<Button-1>", lambda e: webbrowser.open_new("https://esolangs.org/wiki/Fish"))

    frame.pack(side="top", expand=True, fill="both")

def menuBrain(frame):

    clearFrame(frame)
    interpreter=brain.Brainfunk()

    def resetBrain():
        interpreter.pointer=0
        interpreter.memory=[]
        interpreter.output=""
        interpreter.step==0

    def stepCodeBrain():
        interpreter.runStep(inputtxt.get(1.0, "end-1c"))

        list_of_the_values = list(interpreter.memory.values())
        stacktxt.delete(0.0, "end-1c")
        stacktxt.insert(END, list_of_the_values.__str__())
            
        outputtxt.delete(0.0, "end-1c")
        outputtxt.insert(END, interpreter.output.__str__())
        frame.update()
    
    def runCodeBrain():
        #stacktxt.delete(0.0, "end-1c")
        resetBrain()

        interpreter.run(inputtxt.get(1.0, "end-1c"))
        stacktxt.delete(0.0, "end-1c")
        list_of_the_values = list(interpreter.memory.values())
        stacktxt.insert(END, list_of_the_values.__str__())
            
        outputtxt.delete(0.0, "end-1c")
        outputtxt.insert(END, interpreter.output.__str__())
        frame.update()

    
    
    

    lbl = Label(frame, text="Brainf**k Interpreter", font=("MS Comic Sans", 40))  
    lbl.configure(bg="black",fg="white",justify=CENTER)
    lbl.grid(column=0, row=0,padx=100,pady=20,columnspan=6)  

    txtvalue="Brainf**k is one of the most famous esoteric programming languages, and has inspired the creation of a host of other languages.\nBrainfuck operates on an array of memory cells, each initially set to zero. (In the original implementation, the array was 30,000\ncells long, but this may not be part of the language specification; different sizes for the array length and cell size give different\nvariants of the language). There is a pointer, initially pointing to the first memory cell. The language contains only 8 commands:\n+(add)  -(remove)  >(pointer-right)  <(pointer-left)  [](loop)  .(input)  ,(output)"

    txt1 = Label(frame, text=txtvalue, font=("Arial Bold", 16),justify="left")  
    txt1.configure(bg="black",fg="white")
    txt1.grid(column=0, row=1,columnspan=6,padx=50,pady=20)  

    txt2 = Label(frame, text="input:", font=("Arial Bold", 16),justify="left")  
    txt2.configure(bg="black",fg="white")
    txt2.grid(column=0, row=2)  

    inputtxt = Text(frame,height = 9,width = 40)
    inputtxt.configure(bg="white",fg="black")
    inputtxt.grid(column=0, row=3,columnspan=3,rowspan=2,pady=10,padx=20)
    
    txt3 = Label(frame, text="memory:", font=("Arial Bold", 16),justify="left")  
    txt3.configure(bg="black",fg="white")
    txt3.grid(column=4, row=2)  

    stacktxt = Text(frame,height = 2,width = 40)
    stacktxt.configure(bg="white",fg="black")
    stacktxt.grid(column=4, row=3,columnspan=2,pady=10)

    txt4 = Label(frame, text="output:", font=("Arial Bold", 16),justify="left")  
    txt4.configure(bg="black",fg="white")
    txt4.grid(column=4, row=4)  

    v2=Scrollbar(frame, orient='vertical')
    v2.grid(column=5, row=5,sticky=N+S+W)

    outputtxt = Text(frame,height = 6,width = 40,yscrollcommand=v2.set)
    outputtxt.configure(bg="white",fg="black")
    outputtxt.grid(column=4, row=5,columnspan=2,padx=20)

    v2.config(command=outputtxt.yview,background="black")


    stepButton = Button(frame,text = "Step",command=stepCodeBrain,font=("Arial Bold", 16))
    stepButton.grid(column=0, row=5)

    runButton = Button(frame,text = "Run",command=runCodeBrain,font=("Arial Bold", 16))
    runButton.grid(column=2, row=5)


    link1 = Label(frame, text="More info about Brainf**k can be found at : www.esolangs.org", cursor="hand2",font=("Arial Bold", 18),justify="center")
    link1.configure(bg="black",fg="white")
    link1.grid(column=0, row=6,columnspan=6,padx=50,pady=120)
    link1.bind("<Button-1>", lambda e: webbrowser.open_new("https://esolangs.org/wiki/Brainfuck"))

    frame.pack(side="top", expand=True, fill="both")



def clearFrame(frame):
    for widget in frame.winfo_children():
       widget.destroy()
    frame.pack()






################################################
main()

