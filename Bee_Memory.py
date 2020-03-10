class memoryList:

    def __init__(self):
        self.bee_ram = [0] * 65536 #list of 65536 zeroes

    #file that will print out the contents of ram, used for error checking
    def bee_create_file(self):
        self.file = open("memory.txt", 'w+')
        return self.file

    #Function for writing our the contents of the bee ram object to the file
    def bee_print_ram(self):
        
        for x in self.bee_ram:
            self.file.write("%s\n" % x)
