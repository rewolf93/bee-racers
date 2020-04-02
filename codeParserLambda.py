from Bee_Memory import VM
import pickle
import MemoryMap

class CodeParser():

    def jmp(self, terms):

        for lineNum, line in enumerate(self.userCode):
            line = self.userCode[lineNum].split()
            if line[0] == terms[1]:
                self.pushFunction()
                self.lineNum = lineNum
                return
            
    def fly(self):
        return
        #REMOVE COLLISION FROM BEE FOR SET TIME PERIOD
        #INCREASE SIZE OF BEE SPRITE AND DEPTH OF SHADOW THEN GO BACK TO NORMAL

    def portToNum(self, terms):
        for i, _ in enumerate(terms):
            if terms[i] == "SPEED":
                terms[i] = self.bee.opo(MemoryMap.Speed)
            if terms[i] == "ANGLE":
                terms[i] = self.bee.opo(MemoryMap.Angle)

    def lst(self, terms):
        self.portToNum(terms)
        if int(terms[1]) < int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return

    def lte(self, terms):
        self.portToNum(terms)
        if int(terms[1]) <= int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return
                
    def grt(self, terms):
        self.portToNum(terms)
        if int(terms[1]) > int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return
                
    def gte(self, terms):
        self.portToNum(terms)
        if int(terms[1]) >= int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return
                
    def eqt(self, terms):
        self.portToNum(terms)
        if int(terms[1]) == int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.lineNum = lineNum
                    return
                
    def nte(self, terms):
        self.portToNum(terms)
        if int(terms[1]) != int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return

    def err(self, terms):
        temp = ""
        for i in range(1, int(len(terms))): 
            temp += terms[i]
            temp += " "
        print("ERROR: " + temp)

    def wait(self, cycles):
        self.bee.nop(int(cycles))

    def pushFunction(self):
        self.functionLine.append(self.lineNum)

    def popFunction(self):
        if(len(self.functionLine) > 0):
            self.lineNum = self.functionLine[(len(self.functionLine)) - 1]
            self.functionLine.pop()
            
        elif(len(self.functionLine) == 0):
            self.lineNum = len(self.userCode) + 1
    
    bee = VM()
                                      
    def __init__(self, path):

        #Set line number to zero and initialize stack
        self.lineNum = 0
        self.functionLine = []
        
        #Open bee code file
        beeCode = open(path, "r")
        self.userCode = beeCode.readlines()
        beeCode.close()

        #Remove whitespace
        line = 0
        while line < len(self.userCode):
            terms = self.userCode[line].split()
            if len(terms) == 0:
                self.userCode.pop(line)
            else:
                line += 1
        
        #Save bee code as binary
        binPath = path.replace(".txt", ".bin")
        binFile = open(binPath, "wb")
        pickle.dump(self.userCode, binFile)
        binFile.close()

        #Create bee VM
        self.bee.print_ram()
        
    def parse(self):

        #Function dictionary
        math = {"add" : self.bee.add,  #Working
                "sub" : self.bee.sub,  #Working
                "mpy" : self.bee.mpy,  #Working
                "div" : self.bee.div,  #Working
                "set" : self.bee.mov,  #Working
                "mod" : self.bee.mod,  #Working
                "inc" : self.bee.inc,  #Working
                "dec" : self.bee.dec,  #Working
                "neg" : self.bee.neg,  #Working
                "or" : self.bee.orr,   #Working
                "and" : self.bee.andd, #Working
                "xor" : self.bee.xorr, #Working
                "not" : self.bee.nott  #Working
        }

        comparisons = { "jmp" : self.jmp, #Working
                        "fly" : self.fly, #Not working
                        "lst" : self.lst, #Working
                        "lte" : self.lte, #Working
                        "grt" : self.grt, #Working
                        "gte" : self.gte, #Working
                        "eqt" : self.eqt, #Working
                        "nte" : self.nte, #Working
                        "nop" : self.wait #Working
        }
        
        while self.lineNum < len(self.userCode):

            #Split line up into parts
            terms = self.userCode[self.lineNum].split()
            ##print(self.lineNum, terms)           
                
            #Find function
            if terms[0] == "end":
                self.popFunction()

            elif terms[0] == "err":
                self.err(terms)

            elif terms[0] == "nop":
                self.wait(terms[1])
                
            elif len(terms) == 3:
                
                #Set memory location to what variable needs to be changed
                if terms[1] == "SPEED":
                    self.memloc = MemoryMap.Speed
                elif terms[1] == "ANGLE":
                    self.memloc = MemoryMap.Angle
                    
                math[terms[0]](self.memloc, int(terms[2]))

            elif len(terms) == 5 or len(terms) == 2:
                
                #Set memory location to what variable needs to be changed
                if terms[1] == "SPEED":
                    self.memloc = MemoryMap.Speed
                elif terms[1] == "ANGLE":
                    self.memloc = MemoryMap.Angle
                    
                if math.get(terms[0]):    
                    math[terms[0]](self.memloc)
                else:
                    comparisons[terms[0]](terms)

            #Increment line number
            self.lineNum += 1

        
