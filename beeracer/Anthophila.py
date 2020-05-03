#bee-racers Virtual Machine for storing information in memory, and delivering instructions to the physics engine
import beeracer.codeParserLambda as codeParserLambda

bee = codeParserLambda.CodeParser("bee.txt")
bee.parse()
