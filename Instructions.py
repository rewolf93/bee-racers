#Functions for instructions

#NOP - Waste a clock cycle
def bee_nop():
    pass

#ADD - Adds x + y, reesult stored in X

#Assume the assembly code was
#add    ax,     10
#The memory location (mem_loc) would be 65 (as stated in the memory map)
#So we need the parser to interpret ax as 65, bx as 66, cx 67 ... etc
#Or if they use an @ sign, check if its writable space, then interpret it as that memory location
def bee_add(bee, mem_loc, y):
    x = (bee.bee_ram[mem_loc]+y)
    bee.bee_ram[mem_loc] = x

#SUB - Subtract X-Y, result stored in X

def bee_sub(mem_loc, y):
    x = (bee_ram[mem_loc] - y)
    bee_ram[mem_loc] = x

#INC - Increments by 1
def bee_inc(mem_loc):
    bee_ram[mem_loc] = bee_ram[mem_loc] + 1

#DEC - Decrement by 1 
def bee_dec(mem_loc):
    bee_ram[mem_loc] = bee_ram[mem_loc] - 1

#NEG - Negate 
def bee_neg(mem_loc):
    bee_ram[mem_loc] = bee_ram[mem_loc] * -1

#OR - Bitwise OR

def bee_or(mem_loc, y):
    x = bee_ram[mem_loc] | y
    bee_ram[mem_loc] = x

#AND - Bitwise AND

def bee_and(mem_loc, y):
    x = bee_ram[mem_loc] & y
    bee_ram[mem_loc] = x   

#XOR - Bitwise XOR

def bee_xor(mem_loc, y):
    x = bee_ram[mem_loc] ^ y
    bee_ram[mem_loc] = x

#NOT - Bitwise NOT

def bee_not(mem_loc):
    x = ~ bee_ram[mem_loc] 
    bee_ram[mem_loc] = x 


#MPY - Multiply X*Y, result stored in X

def bee_mpy(mem_loc, y):
    x = (bee_ram[mem_loc] * y)
    bee_ram[mem_loc] = x       

#DIV - Divide X/Y, result stored in X

def bee_div(mem_loc, y):
    x = (bee_ram[mem_loc] / y)
    bee_ram[mem_loc] = x     

#MOD - Modulus X%Y, result stored in X

def bee_mod(mem_loc, y):
    x = (bee_ram[mem_loc] % y)
    bee_ram[mem_loc] = x     

#CMP - Compare X to Y, result stored in flags register
#1 = Zero
#2 = Equal
#3 = Greater
#4 = Less

def bee_cmp(mem_loc, y):
    if bee_ram[mem_loc] == y and y == 0:
        x = 1
    elif bee_ram[mem_loc] == y:
        x = 2
    elif bee_ram[mem_loc] < y:
        x = 3
    elif bee_ram[mem_loc] > y:
        x = 4

    bee_ram[mem_loc] = x        

#All the jump functions, establishing a place for them, but need to figure out how to actually code these in
#def bee_jmp():
#def bee_jls():    
#def bee_jgr():
#def bee_jne():
#def bee_jeq():
#def bee_jge():
#def bee_jle():
#def bee_jz():    
#def bee_jnz():    
     

#MOV - Moves value into memory

def bee_mov(bee, mem_loc, y):
    bee.bee_ram[mem_loc] = y

#LOC - set memory address x equal to memory address y
def bee_loc(mem_loc, mem_loc2):
    bee_ram[mem_loc] = bee_ram[mem_loc2]

#IPO - Inputs number from port into memory loc
def bee_ipo(mem_loc, y):
    #need code for getting port values, ask nathan 
    bee_ram[mem_loc] = y

#OPO - Output number from memory loc into port
def bee_opo(mem_loc, y):
    #need code for inputing port values, ask nathan 
    y = bee_ram[mem_loc]


#ERR - Generate error code
def bee_err():
    print("error")
