class Brainfunk():
    pointer=0
    memory=[]
    output=""
    step=0

    def parse(this,code):
            return True
    
    def loop(this,code):
        opened = []
        loops = {}
        for i in range(len(code)):
            if code[i] == '[':
                opened.append(i)
            elif code[i] == ']':
                loops[i] = opened[-1]
                loops[opened.pop()] = i
        return loops

    def run(this,code):
        if this.parse(code):
            this.pointer = i = 0
            this.memory = {0: 0}
            loops = this.loop(code)
            while i < len(code):
                command = code[i]
                if command == '>':
                    this.pointer += 1
                    this.memory.setdefault(this.pointer, 0)
                elif command == '<':
                    this.pointer -= 1
                elif command == '+':
                    this.memory[this.pointer] += 1
                elif command == '-':
                    this.memory[this.pointer] -= 1
                elif command == '.':
                    this.output+=chr(this.memory[this.pointer])
                elif command == ',':
                    this.memory[this.pointer] = int(input('Input: '))
                elif command == '[':
                    if not this.memory[this.pointer]: 
                        i = loops[i]
                elif command == ']':
                    if this.memory[this.pointer]: 
                        i = loops[i]
                
                i += 1
  

    def runStep(this,code):
        if this.parse(code):
            loops = this.loop(code)
            if  (this.step==0):
                this.pointer = 0
                this.memory = {0: 0}
            if this.step < len(code):
                command = code[this.step]
                if command == '>':
                    this.pointer += 1
                    this.memory.setdefault(this.pointer, 0)
                elif command == '<':
                    this.pointer -= 1
                elif command == '+':
                    this.memory[this.pointer] += 1
                elif command == '-':
                    this.memory[this.pointer] -= 1
                elif command == '.':
                    this.output+=chr(this.memory[this.pointer])
                elif command == ',':
                    this.memory[this.pointer] = int(input('Input: '))
                elif command == '[':
                    if not this.memory[this.pointer]: 
                        this.step = loops[this.step]
                elif command == ']':
                    if this.memory[this.pointer]: 
                        this.step = loops[this.step]
                
                this.step += 1
            if (this.step>=len(code) or this.step<0):
                return -1


