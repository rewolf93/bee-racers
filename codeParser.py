import bee

class CodeParser():

    lineNum = 0

    def __init__(self, path):

        #Open bee code file
        beeCode = open(path, "r")
        self.userCode = beeCode.readlines()
        beeCode.close()

        #Remove whitespace
        self.userCode = [self.userCode.replace(' ', '') for self.userCode in self.userCode]

    def perser(self):

        while self.lineNum < len(self.userCode):

            terms = self.userCode[self.lineNum].split()

            if terms[0] == "add":
                self.add(terms)

            elif terms[0] == "sub":
                self.sub(terms)

            elif terms[0] == "mlt":
                self.mlt(terms)

            elif terms[0] == "div":
                self.div(terms)

            elif terms[0] == "set":
                self.set(terms)

            elif terms[0] == "jmp":
                self.jmp(terms)

            elif terms[0] == "fly":
                self.fly()

            elif terms[0] == "lst":
                self.lst(terms)

            elif terms[0] == "lte":
                self.lte(terms)

            elif terms[0] == "grt":
                self.grt(terms)

            elif terms[0] == "gte":
                self.gte(terms)

            elif terms[0] == "eqt":
                self.eqt(terms)

            elif terms[0] == "nte":
                self.nte(terms)


            self.lineNum += 1

    def add(self, terms):
        
        if terms[1] == "SPEED":
            #ADD NUMBER TO SPEED OF BEE
        elif terms[1] == "ANGLE":
            #ADD NUMBER TO ANGLE OF BEE

    def sub(self, terms):

        if terms[1] == "SPEED":
            #SUBTRACT NUMBER FROM SPEED OF BEE
        elif terms[1] == "ANGLE":
            #SUBTRACT NUMBER FROM ANGLE OF BEE

    def mlt(self, terms):

        if terms[1] == "SPEED":
            #MULTIPLY SPEED BY NUMBER

        elif terms[1] == "ANGLE":
            #MULTIPLY ANGLE BY NUMBER

    def div(self, terms):

        if terms[1] == "SPEED":
            #DIVIDE SPEED BY NUMBER
        elif terms[1] == "ANGLE":
            #DIVIDE ANGLE BY NUMBER

    def set(self, terms):

        if terms[1] == "SPEED":
            #SET SPEED TO NUMBER
        elif terms[1] == "ANGLE":
            #SET ANGLE TO NUMBER

    def jmp(self, terms):

        for lineNum, line in enumerate(self.userCode):
            line = self.userCode[lineNum].split()
            if line[0] == terms[1]:
                self.lineNum = lineNum
                return
    def fly(self):

        #REMOVE COLLISION FROM BEE FOR SET TIME PERIOD
        #INCREASE SIZE OF BEE SPRITE AND DEPTH OF SHADOW THEN GO BACK TO NORMAL

    def portToNum(self, terms):
        for i, _ in enumerate(terms):
            if terms[i] == "SPEED":
                terms[i] = self.acceleration[0]
            if terms[i] == "ANGLE":
                terms[i] = self.acceleration[1]

    def lst(self, terms):
        self.portToNum(terms)
        if int(terms[1]) < int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.lineNum = lineNum
                    return

    def lte(self, terms):
        self.portToNum(terms)
        if int(terms[1]) <= int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.lineNum = lineNum
                    return
    def grt(self, terms):
        self.portToNum(terms)
        if int(terms[1]) > int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.lineNum = lineNum
                    return
    def gte(self, terms):
        self.portToNum(terms)
        if int(terms[1]) >= int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.lineNum = lineNum
                    return
    def eqt(self, terms):
        self.portToNum(terms)
        if int(terms[1]) == int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.lineNum = lineNum
                    return
                
    def nte(self, terms):
        self.portToNum(terms)
        if int(terms[1]) != int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.lineNum = lineNum
                    return
