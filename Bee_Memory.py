class VM:

    ram = [0] * 65536

    #Function for writing our the contents of the bee ram object to the file
    def print_ram(self):
        self.file = open("memory.txt", "w+")
        for x in self.ram:
            self.file.write("%s\n" % x)
        self.file.close()
            
    #Functions for instructions

    #NOP - Waste a clock cycle
    def nop(bee, cycles):
        while(cycles > 0):
            pass
            cycles -= 1

    #ADD - Add X+Y, result stored in X    
    def add(bee, mem_loc, y):
        bee.ram[mem_loc] = (bee.ram[mem_loc] + y)
        bee.print_ram()

    #SUB - Subtract X-Y, result stored in X

    def sub(bee, mem_loc, y):
        bee.ram[mem_loc] = (bee.ram[mem_loc] - y)
        bee.print_ram()

    #INC - Increments by 1
    def inc(bee, mem_loc):
        bee.ram[mem_loc] = bee.ram[mem_loc] + 1
        bee.print_ram()

    #DEC - Decrement by 1 
    def dec(bee, mem_loc):
        bee.ram[mem_loc] = bee.ram[mem_loc] - 1
        bee.print_ram()

    #NEG - Negate 
    def neg(bee, mem_loc):
        bee.ram[mem_loc] = bee.ram[mem_loc] * -1
        bee.print_ram()

    #OR - Bitwise OR
    def orr(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] | y
        bee.print_ram()

    #AND - Bitwise AND
    def andd(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] & y
        bee.print_ram()

    #XOR - Bitwise XOR
    def xorr(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] ^ y
        bee.print_ram()

    #NOT - Bitwise NOT
    def nott(bee, mem_loc):
        bee.ram[mem_loc] = ~ bee.ram[mem_loc]
        bee.print_ram()

    #MPY - Multiply X*Y, result stored in X
    def mpy(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] * y
        bee.print_ram()

    #DIV - Divide X/Y, result stored in X
    def div(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] / y
        bee.print_ram()

    #MOD - Modulus X%Y, result stored in X
    def mod(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] % y
        bee.print_ram()
    
    #CMP - Compare X to Y, result stored in flags register
    #1 = Zero
    #2 = Equal
    #3 = Greater
    #4 = Less

    def cmp(bee, mem_loc, y):
        if bee.ram[mem_loc] == y and y == 0:
            x = 1
        elif bee.ram[mem_loc] == y:
            x = 2
        elif bee.ram[mem_loc] < y:
            x = 3
        elif bee.ram[mem_loc] > y:
            x = 4

        ram[mem_loc] = x    

    #MOV - Moves value into memory

    def mov(bee, mem_loc, y):
        bee.ram[mem_loc] = y
        bee.print_ram()

    #LOC - set memory address x equal to memory address y
    def loc(bee, mem_loc, mem_loc2):
        bee.ram[mem_loc] = bee.ram[mem_loc2]

    #IPO - Inputs number from port into memory loc
    def ipo(bee, mem_loc, y):
        #need code for getting port values, ask nathan 
        bee.ram[mem_loc] = y

    #OPO - Output number from memory loc into port
    def opo(bee, mem_loc):
        return bee.ram[mem_loc]
