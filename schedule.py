import random

def generate_schedule(seed):
    max =29
    random.seed(seed)
    print("      1     2     3     4     5     6     7     8     9     10")
    resultPo = ""
    for _ in range(8):
        resultPo = random.choices(subjects) 
        pass
    print("PO" + resultPo)
    print("UT")
    print("ST")
    print("CT")
    print("PA")
    pass

subjects = ["INF   ","VAP   ","MIT   ","MSW   ","PRG   ","MAT   ","ANJ   ","CJL   ","ASW   ","OBN   ","POS   "]

generate_schedule(80)
