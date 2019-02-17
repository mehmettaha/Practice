from collections import deque

def searchm(sentences, phrase, history = 2):
    memory = deque(maxlen = history)
    for sentence in sentences:
        if phrase in sentence:
            yield sentence, memory
            memory.append(sentence)

objects = ["sentence a x", "sentence b x", "sentence c y", "sentence d y", "sentence e x", "sentence f x"]

for i, t in searchm(objects, "x", 2):
    print(i,t)