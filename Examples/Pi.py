from Hardware import Hardware, InstructionLibrary
import Instructions as inst
from Selection import tournament
from Mutation import mutate
from math import pi


#######################################
# Evolving a program to approximate pi
#######################################

def main():
    inst_lib = InstructionLibrary()
    inst_lib.add_inst("Add", inst.add, False)
    inst_lib.add_inst("Sub", inst.sub, False)
    inst_lib.add_inst("Mul", inst.mul, False)
    inst_lib.add_inst("Div", inst.div, False)
    inst_lib.add_inst("Assign", inst.assign, False)
    inst_lib.add_inst("Copy", inst.copy, False)
    hws = [Hardware(inst_lib, None, 4, 32) for _ in range(1000)]
    [hw.generate_program() for hw in hws]

    gen = 0
    best = -1000
    while 1:
        print(F"Generation: {gen}")
        for hw in hws:
            ticks = 0
            while not hw.EOP and ticks < 10:
                ticks += 1
                hw.tick()
            hw.cache_fitness(-abs(pi - hw.registers[0]))
            if hw.fitness > best:
                best = hw.fitness
                print(hw)
                print("Fin with Fit:", best)
        hws = tournament(hws)
        [mutate(hw) for hw in hws]
        gen += 1


if __name__ == '__main__':
    main()
