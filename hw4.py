# 1) 
from functools import reduce
def count_simba(data):
    return reduce(lambda a, b: a + b, map(lambda s: s.count("Simba"), data))

data = ["Simba and Nala are lions.", "I laugh in the face of danger.",
           "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

result = count_simba(data)
print(result) 
