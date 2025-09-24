import math

def compare():
    variable = 0
    for n in range(1, 100):
        if (3 * n ** 2 + 50 * n):
            variable = n
            return n

print(compare())
n=9
print(3 * n ** 2 + 50 * n)




def compares():
    
    for n in range(1, 100):
        if (8 * n * math.log2(n)):
            
         return n
compare = compares()
print(f"El cruce ocurre cerca de n ≈ {compares}")
print(f"Conclusión: Para n ≥ {compares}")


def compare2():
    variable = 0
    for n in range(1, 100):
        if (n**2 + 2**n):
            variable = n
            return n
print(compare2())
n=9
print(n + 2 ** n) 
