import Bee_Memory
import pickle
import sys
import MemoryMap

class CodeParser():

    #Jump to line
    def jmp(self, terms):
        for lineNum, line in enumerate(self.userCode):
            line = self.userCode[lineNum].split()
            if line[0] == terms[1]:
                self.pushFunction()
                self.lineNum = lineNum
                return
    #Bee flies    
    def fly(self):
        return
        #REMOVE COLLISION FROM BEE FOR SET TIME PERIOD
        #INCREASE SIZE OF BEE SPRITE AND DEPTH OF SHADOW THEN GO BACK TO NORMAL


    #Change port to memory location
    def portToLoc(self, terms):
        for i in range(1, len(terms)):
            if terms[i] in MemoryMap.ports:
                terms[i] = MemoryMap.ports[terms[i]]
                
    #Change port to an int
    def portToNum(self, terms):
        for i in range(1, len(terms)):
            if terms[i] in MemoryMap.ports:
                terms[i] = self.bee.opo(MemoryMap.ports[terms[i]])
            

    #Less than
    def lst(self, terms):
        if not terms[3] == "jmp":
            self.invalidSyntaxError(self.userCode[self.lineNum], terms)
            
        if int(terms[1]) < int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return
                
    #Less than or equal to
    def lte(self, terms):
        if not terms[3] == "jmp":
            self.invalidSyntaxError(self.userCode[self.lineNum], terms)
            
        if int(terms[1]) <= int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return

    #Greater than
    def grt(self, terms):
        if not terms[3] == "jmp":
            self.invalidSyntaxError(self.userCode[self.lineNum], terms)
            
        if int(terms[1]) > int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return

    #Greater than or equal to         
    def gte(self, terms):
        if not terms[3] == "jmp":
            self.invalidSyntaxError(self.userCode[self.lineNum], terms)
            
        if int(terms[1]) >= int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return

    #Equal to        
    def eqt(self, terms):
        if not terms[3] == "jmp":
            self.invalidSyntaxError(self.userCode[self.lineNum], terms)
            
        if int(terms[1]) == int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.lineNum = lineNum
                    return

    #Not equal to        
    def nte(self, terms):
        if not terms[3] == "jmp":
            self.invalidSyntaxError(self.userCode[self.lineNum], terms)
            
        if int(terms[1]) != int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                line = line[:-1]
                if line == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return

    #Error
    def err(self, terms):
        temp = ""
        for i in range(1, int(len(terms))): 
            temp += terms[i]
            temp += " "
        print("ERROR: " + temp)

    #Wait cycles
    def wait(self, cycles):
        if not isinstance(cycles, int):
            self.invalidInputError(self.userCode[self.lineNum])
            
        self.bee.nop(int(cycles))

    #Push function to stack for return
    def pushFunction(self):
        self.functionLine.append(self.lineNum)

    #Return to function or end code
    def popFunction(self):
        if len(self.functionLine) > 0:
            self.lineNum = self.functionLine[(len(self.functionLine)) - 1]
            self.functionLine.pop()
            
        elif len(self.functionLine) == 0:
            self.lineNum = len(self.userCode) + 1
    
    bee = Bee_Memory.VM()

    #Initialization                             
    def __init__(self, path):

        #Set line number to zero and initialize stack
        self.lineNum = 0
        self.functionLine = []

        #Check if path is a text file
        if not ".txt" in path:
            self.fileTypeError()
            
        #Open bee code file
        beeCode = open(path, "r")
        self.userCode = beeCode.readlines()
        beeCode.close()

        #Remove whitespace and comments and, set ports to memory locations 
        line = 0
        while line < len(self.userCode):
            terms = self.userCode[line].split()
            if len(terms) == 0 or "#" in terms[0]:
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

    #Parser  
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
                "or"  : self.bee.orr,  #Working
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
        }
        
        while self.lineNum < len(self.userCode):

            #Split line up into parts and change register name to register location
            terms = self.userCode[self.lineNum].split()       
                
            #Find function
            if terms[0] == "end":
                self.popFunction()

            elif terms[0] == "err":
                self.err(terms)

            elif terms[0] == "nop":
                self.wait(terms[1])
                
            elif len(terms) == 3:
                self.portToLoc(terms)
                math[terms[0]](int(terms[1]), int(terms[2]))

            elif len(terms) == 5 or len(terms) == 2:
                
                #Set memory location to what variable needs to be changed
                self.portToNum(terms)
                if math.get(terms[0]):    
                    math[terms[0]](terms[1], terms[2])
                else:
                    comparisons[terms[0]](terms)

            #Increment line number
            self.lineNum += 1

    #Wrong filetype when loading bee
    def fileTypeError(self):
        print("ERROR: Invalid filetype for bee. Please use a .txt file")
        sys.exit()

    #Wrong input type with function
    def invalidInputError(self, line):
        print("ERROR: Invalid input type on line", self.lineNum, ":", line)
        sys.exit()

    #Wrong syntax with function
    def invalidSyntaxError(self, line, terms):
        print("ERROR: Invalid syntax on line", self.lineNum, ":", line, "...'", terms[3], "' should be ' jmp '")
        sys.exit()
