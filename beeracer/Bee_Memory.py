class VM:

    def __init__(self):
        self.ram = [0] * 65536

    #Function for writing our the contents of the bee ram object to the file
    def print_ram(self):
        self.file = open("memory.txt", "w+")
        for x in self.ram:
            self.file.write("%s\n" % x)
        self.file.close()
    
    def check_ram(self, loc):
        return self.ram[loc]
    
    def set_ram(self, loc, val):
        self.ram[loc] = val
            
    #Functions for instructions

    #NOP - Waste a clock cycle
    def nop(bee, cycles):
        return cycles - 1

    #ADD - Add X+Y, result stored in X    
    def add(bee, mem_loc, y):
        bee.ram[mem_loc] = (bee.ram[mem_loc] + y)
        

    #SUB - Subtract X-Y, result stored in X

    def sub(bee, mem_loc, y):
        bee.ram[mem_loc] = (bee.ram[mem_loc] - y)
        

    #INC - Increments by 1
    def inc(bee, mem_loc):
        bee.ram[mem_loc] = bee.ram[mem_loc] + 1
        

    #DEC - Decrement by 1 
    def dec(bee, mem_loc):
        bee.ram[mem_loc] = bee.ram[mem_loc] - 1
        

    #NEG - Negate 
    def neg(bee, mem_loc):
        bee.ram[mem_loc] = bee.ram[mem_loc] * -1
        

    #OR - Bitwise OR
    def orr(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] | y
        

    #AND - Bitwise AND
    def andd(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] & y
        

    #XOR - Bitwise XOR
    def xorr(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] ^ y
        

    #NOT - Bitwise NOT
    def nott(bee, mem_loc):
        bee.ram[mem_loc] = ~ bee.ram[mem_loc]
        

    #MPY - Multiply X*Y, result stored in X
    def mpy(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] * y
        

    #DIV - Divide X/Y, result stored in X
    def div(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] / y
        

    #MOD - Modulus X%Y, result stored in X
    def mod(bee, mem_loc, y):
        bee.ram[mem_loc] = bee.ram[mem_loc] % y
        
    
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
        

    #LOC - set memory address x equal to memory address y
    def loc(bee, mem_loc, mem_loc2):
        bee.ram[mem_loc] = bee.ram[mem_loc2]

    #IPO - Inputs number from port into memory loc
    def ipo(bee, port, mem_loc):
        #need code for getting port values, ask nathan 
        bee.ram[mem_loc] = bee.ram[port]

    #OPO - Output number from memory loc into port
    def opo(bee, mem_loc):
        return bee.ram[mem_loc]

#Input Functions

    #P_ZOOM Set Speed of Bee
    def p_zoom(bee, y):
        bee.ram[512] = y
    #P_Steer Set angle to turn
    def p_steer(bee, y):
        bee.ram[513] = y
    #P_SCANARC Set arc width to scan
    def p_scanarc(bee, y):
        bee.ram[514] = y

    #Output Functions

    #P_COMPASS Current Heading of Bee
    def p_compass(bee, value):
        bee.ram[514] = value
    #P_TESLA Current Distance to closest Bee
    def p_tesla(bee, value):
        bee.ram[516] = value
    #P_WALLDIST Current Distance to closest wall
    def p_walldist(bee, value):
        bee.ram[517] = value
    #P_HOMEDIST Current distance to home
    def p_homedist(bee, value):
        bee.ram[518] = value
    #P_POLLENDIST Current distance to pollen
    def p_pollendist(bee, value):
        bee.ram[519] = value




    #PORTS

    #Get current speed from Game
    def setCurSpeed(bee, value):
        bee.ram[2] = value

    #Get current X axis of bee homefrom Game
    def setXAxisBeeHome(bee, value):
        bee.ram[3] = value

    # Get current Y axis of bee home from Game
    def setYAxisBeeHome(bee, value):
        bee.ram[4] = value

    # Get current X axis of bee  from Game
    def setXAxisBee(bee, value):
        bee.ram[5] = value
    # Get current X axis of bee  from Game
    def setYAxisBee(bee, value):
        bee.ram[6] = value

    #Set the pollen count
    def setPollenCount(bee, value):
        bee.ram[7] = value
    #Set X axis of pollen
    def setPollenLocX(bee, value):
        bee.ram[8] = value
    #Set Y axis of pollen
    def setPollenLocY(bee, value):
        bee.ram[9] = value

    # How much pollen is the bee holding?
    def invCount(bee, value):
        bee.ram[10] = value