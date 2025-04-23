# Analysis

## Layer 1, Head 4 - Used Text: "The capital of France is [MASK]."

Example Sentences:
- In layer 1 head 4, we can observe how the head fairly identifies the importance of "capital of France" as the pair of words to pay attention to.

## Layer 12, Head 11 - Used Text: "The capital of France is [MASK]."

- In layer 12 head 11, we can observe how there is a lot of noise around — all the words are paying attention to the separator point of the phrase, which is irrelevant to the result.

## Layer 1, Head 4 - Used Text: "The apple is on the table, where people usually go to [MASK]."

Now I chose "The apple is on the table, where people usually go to [MASK]." because I wanted to try to trick the model with prepositions, by masking out an action that people are supposed to do.

Example Sentences:
- At layer 1 head 4, we can see how the attention is doing a great job not being misled by irrelevant information. It starts to "suspect" around "is on the table" and around "usually go to", so we are achieving our little trick.

## Layer 3, Head 10 - Used Text: "The apple is on the table, where people usually go to [MASK]."

- At attention layer 3 and head 10, it is interesting how — similar to the "Understanding" section of the course — the model is strongly recognizing which words are consequential, which is correct in our language!