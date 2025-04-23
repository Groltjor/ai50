import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> N V
S -> N V P N
NP -> N | Det N | Det Adj N | Det Adj Adj Adj N | Det N P Det N | P N | Adj N | Det Adj N | Adj N | Det Adj
PP -> P NP
S -> N V NP P NP P NP
S -> N V NP PP
S -> N V NP
S -> N V PP Conj N V
S -> NP V NP
S -> N Adv V NP Conj N V PP 
S -> N V Adv Conj V NP
S -> N V NP NP PP Conj V N P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    import string
    import re
    
    punctDict = list(string.punctuation)
    alphabeticDict = list(string.ascii_lowercase)
    clean = []
    if sentence:
        chainer = sentence.lower()
        chainer = chainer.split(sep = " ")
        for palabra in chainer:

            evalPalabra = list(palabra)
            for caracter in evalPalabra:
                if caracter in alphabeticDict:
                    clean.append(palabra.strip())
                    break
            
    for index in range(0, len(clean)):
        clean[index] = re.sub(r"\.$", "", clean[index])
    
    if clean:
        return clean
    else:
        return None
        


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks = []

    for rama in tree.subtrees():
        if rama.label() == "NP":
            if not any(child.label() == "NP" and child != rama for child in rama.subtrees()):
                chunks.append(rama)
            
    return chunks


if __name__ == "__main__":
    main()
