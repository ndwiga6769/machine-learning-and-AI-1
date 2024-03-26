from logic import *
# from termcolor import colored

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")
knowledge = And (
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid,dumbledore)),
    dumbledore
)
# knowledge = And(
#     Implication(Not(rain), hagrid),
#     Or(hagrid, dumbledore),
#     Not(And(hagrid, dumbledore)),
#     dumbledore
# )
# print(colored("hello world","green"))
# print(model_check(knowledge, rain))

# Sentence = And(rain,hagrid)

print(knowledge.formula())
