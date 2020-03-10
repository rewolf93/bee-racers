#bee-racers Virtual Machine for storing information in memory, and delivering instructions to the physics engine
import Bee_Memory
import Instructions

bee1 = Bee_Memory.memoryList()
bee_file = bee1.bee_create_file()


print("test")
Instructions.bee_mov(bee1, 10, 5)
Instructions.bee_add(bee1, 12, 10)
bee1.bee_print_ram()
