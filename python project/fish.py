## [ and ] operands are not supported (ну не хочу я ещё дебажить под несколько стеков)

class Fish:
    def __init__(self) -> None:
        self.stack=list()
        self.map=list(list())
        self.x=0
        self.y=0
        self.dir="right"
        self.register=""
        self.stringMode=False
        self.output=""
        self.end=False
        self.skip=False

    def getMap(this,newmap):
        if type(newmap)==str:
            tmp=newmap.split("\n")
        this.map=tmp
    

    def push(this,val):
        if type(this.stack)==None:
            this.stack=list()
        this.stack.append(val)
    
    def Pop(this):
        if len(this.stack)>0:
            tmp=this.stack.pop()
            return tmp
        else: return -1

    def operator(this,op):
        if this.skip:
                this.skip=False
        elif not this.skip:

            if not this.stringMode:
                if op==" ":
                    tmp=0
                elif op==">":  ####### pointer movement
                    this.dir="right"
                elif op=="<":  
                    this.dir="left"
                elif op=="^":  
                    this.dir="up"
                elif op=="v":  
                    this.dir="down"
                elif op=="/":  
                    if this.dir =="right":
                        this.dir="up"
                    elif this.dir =="left":
                        this.dir="down"
                    elif this.dir =="up":
                        this.dir="right"
                    elif this.dir =="down":
                        this.dir="left"
                elif op=="\\":  
                    if this.dir =="right":
                        this.dir="down"
                    elif this.dir =="left":
                        this.dir="up"
                    elif this.dir =="up":
                        this.dir="left"
                    elif this.dir =="down":
                        this.dir="right"
                elif op=="|":
                    if this.dir =="right":
                        this.dir="left"
                    elif this.dir =="left":
                        this.dir="right"
                elif op=="_":
                    if this.dir =="down":
                        this.dir="up"
                    elif this.dir =="up":
                        this.dir="down"
                elif op=="#":
                    if this.dir =="down":
                        this.dir="up"
                    elif this.dir =="up":
                        this.dir="down"
                    if this.dir =="right":
                        this.dir="left"
                    elif this.dir =="left":
                        this.dir="right"
                elif op=="!":
                    this.skip=True
                elif op=="?":
                    tmp=this.Pop()
                    if tmp==0:
                        this.skip=True
                elif op==".":
                    tmp=this.Pop()
                    tmp2=this.Pop()
                    this.x=tmp2
                    this.y=tmp

                elif op in "0123456789abcdf": ########basic stack manip
                    this.push(int(op,base=16))
                elif op=="+":
                    tmp=0
                    tmp=float(this.Pop())
                    tmp+=float(this.Pop())
                    this.push(tmp)
                elif op=="-":
                    tmp=0
                    tmp+=float(this.Pop())
                    tmp2=0
                    tmp2=float(this.Pop())
                    this.push(tmp2-tmp)
                elif op=="*":
                    tmp=0
                    tmp=float(this.Pop())
                    tmp2=0
                    tmp2=float(this.Pop())
                    this.push(tmp2*tmp)
                elif op==",":
                    tmp=0
                    tmp=float(this.Pop())
                    tmp2=0
                    tmp2=float(this.Pop())
                    this.push(tmp2/tmp)
                elif op=="%":
                    tmp=0
                    tmp=float(this.Pop())
                    tmp2=0
                    tmp2=float(this.Pop())
                    this.push(tmp2%tmp)
                elif op=="=":
                    tmp=0
                    tmp=this.Pop()
                    tmp2=0
                    tmp2=this.Pop()
                    if  tmp==tmp2:
                        this.push(1)
                    else: this.push(0)
                elif op==")":
                    tmp=0
                    tmp=this.Pop()
                    tmp2=0
                    tmp2=this.Pop()
                    if  tmp<tmp2:
                        this.push(1)
                    else: this.push(0)
                elif op=="(":
                    tmp=0
                    tmp=this.Pop()
                    tmp2=0
                    tmp2=this.Pop()
                    if  tmp>tmp2:
                        this.push(1)
                    else: this.push(0)
                elif (op=="\'" or op == '\"'):

                    this.stringMode=True
                elif op==":":   #wacky stack manipulations
                    tmp=this.Pop()
                    this.push(tmp)
                    this.push(tmp)
                elif op=="~":
                    this.Pop()
                elif op=="$":
                    tmp=0
                    tmp=this.Pop()
                    tmp2=0
                    tmp2=this.Pop()
                    this.push(tmp)
                    this.push(tmp2)
                elif op=="@":
                    tmp=0
                    tmp=this.Pop()
                    tmp2=0
                    tmp2=this.Pop()
                    tmp3=0
                    tmp3=this.Pop()
                    this.push(tmp)
                    this.push(tmp3)
                    this.push(tmp2)
                elif op=="}":
                    tmp=this.Pop()
                    this.stack=tmp+this.stack
                elif op=="{":
                    tmp=this.stack[1:]
                    tmp.append(this.stack[0])
                    this.stack=tmp
                elif op=="r":
                    this.stack.reverse()
                elif op=="l":
                    this.stack.append(len(this.stack))
                elif op=="o": ###########   input/output
                    tmp=this.Pop()
                    try:
                        this.output+=chr(tmp).__str__()
                    except:
                        this.output+=tmp.__str__()
                elif op=="n":
                    this.output+=this.Pop().__str__()
                elif op=="i":
                    this.stack.push(input("Input one character:"))
                elif op=="&":  ########### map manipulation
                    if this.register=="":
                        this.register=this.Pop()
                    else: 
                        this.stack.append(this.register)
                        this.register=""
                elif op=="g":
                    tmp1=this.Pop()
                    tmp2=this.Pop()
                    this.stack.append(this.map[tmp2][tmp1])
                elif op=="p":
                    tmp1=this.Pop() #y
                    tmp2=this.Pop() #x
                    tmp3=this.Pop() #v
                    map[tmp2,tmp]=tmp3
                elif op==";":
                    this.end=True
            elif ((op=="'"or op == '"')):
                this.stringMode=False
            else:
                this.push(op)
        

    def step(this):
        if not this.end:
            this.operator(this.map[this.y][this.x])
            if this.dir=="right":
                if this.x>=len(this.map[0])-1:
                    this.x=0
                else: this.x+=1
            elif this.dir=="up":
                if this.y<=0:
                    this.y=len(this.map)-1
                else: this.y-=1
            elif this.dir=="down":
                if this.y>=len(this.map)-1:
                    this.y=0
                else: this.y+=1
            elif this.dir=="left":
                if this.x<=0:
                    this.x=len(this.map[0])-1
                else: this.x-=1
            
    
    def run(this):
        while not this.end:
            this.step()
