a = {"a" : 1, "b" : 2, "c" : 2}

def fill(a):
    b = {}
    for key, value in a.items():
        if value not in b.values():
            yield key, value
            b.update({key :value})

print(list(fill(a)))