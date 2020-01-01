from LGPy.Hardware import Hardware, InstructionLibrary
from LGPy import Instructions as inst
from LGPy.Selection import tournament
from LGPy.Mutation import mutate
from random import seed


#############################################
# Evolving a program to determine even / odd
#############################################
def set_int(hardware, args):
    hardware.registers[args[0]] = hardware.traits
    return 0

def main():
    seed(1)

    inst_lib = InstructionLibrary()
    inst_lib.add_inst("Add", inst.add, False)
    inst_lib.add_inst("Sub", inst.sub, False)
    inst_lib.add_inst("Mul", inst.mul, False)
    inst_lib.add_inst("Div", inst.div, False)
    inst_lib.add_inst("Mod", inst.mod, False)
    inst_lib.add_inst("Assign", inst.assign, False)

    #  Custom instruction to give the integer to the hardware
    inst_lib.add_inst("SetInt", lambda hardware, args: set_int(hardware, args), False)

    min_insts = 2
    max_insts = 16
    hws = [Hardware(inst_lib, -1, min_insts, max_insts) for _ in range(1000)]
    [hw.generate_program() for hw in hws]

    gen = 0
    best = -1
    nums = list(range(10))

    while 1:
        print(F"Generation: {gen}")

        for hw in hws:
            correct = 0
            for num in nums:
                hw.traits = num
                ticks = 0
                while not hw.EOP and ticks < 16:
                    ticks += 1
                    hw.tick()
                correct += num % 2 == hw.registers[0]
                hw.reset()

            if correct == len(nums):
                correct += 1 - len(hw)/(max_insts+1)
            hw.cache_fitness(correct)

            if hw.fitness > best:
                best = hw.fitness
                print(hw)
                print("Fin with Fit:", best)
        hws = tournament(hws)

        [mutate(hw) for hw in hws]
        gen += 1


if __name__ == '__main__':
    main()
