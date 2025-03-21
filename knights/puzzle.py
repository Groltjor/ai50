from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")
Truth = Symbol("X dice verdad")
TruthB = Symbol("B dice la verdad")
TruthC = Symbol("C dice la verdad")
Said_A = Symbol("A dijo que es Knave")
# Puzzle 0
# A says "I am both a knight and a knave."

knowledge0 = And(

    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnight, Truth),
    Biconditional(Truth, And(AKnight, AKnave))

)
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnave, Not(BKnight)),
    
    Biconditional(AKnight, Truth),
    Biconditional(Truth, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnight, Truth),
    Biconditional(Truth, Biconditional(AKnight, BKnight)), ##
    
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(BKnight, TruthB),
    Biconditional(TruthB, Not(Biconditional(AKnight, BKnight))),
    
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(

    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnight, Truth),
    Biconditional(Truth, Or(AKnight, AKnave)),

    Biconditional(BKnight, Not(BKnave)),
    Biconditional(BKnight, TruthB),
    Biconditional(TruthB, Said_A),
    Biconditional(Said_A, AKnave),

    Biconditional(CKnight, Not(CKnave)),
    Biconditional(CKnight, TruthC),
    Biconditional(TruthC, AKnight)
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
