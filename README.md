# Parciales — Análisis de Algoritmos (193502)

Universidad Francisco de Paula Santander Ocaña  
Programa: Ingeniería de Sistemas  
Semestre: V  
Créditos: 3  
Asignatura: **Análisis de Algoritmos** 

---

## Instrucciones generales

- Tiempo máximo: **60 minutos**  
- Cada parcial tiene **4 puntos (25 pts c/u)**  
- Usa Python o Java.  
- Para comparar funciones, basta con un **`for` + `if`** y reportar el menor `n` que verifica la desigualdad.  
- Justifica con fórmulas y razonamiento.  

---

# Parcial — Versión A

### Punto 1 (25 pts) — Ordena por complejidad
Ordena de menor a mayor las siguientes funciones (asintóticamente).  
Si dos son del mismo orden, indícalo.


![Logo](https://lh3.googleusercontent.com/pw/AP1GczOgpGBrm2bFBeJEo7b9KpmVW1WB0J7_4xhzREWWmsjd8ejMOn5_QmXnv9ji2z7BlyVAVmYl0jOEs01Vmf9-wEbyuZo7S5DK2xYmuN-cOR2my9LOms5kM5FlcbG3I19k3Xc8nwGVtFKco2O2QXg4DLUn=w128-h290-s-no?authuser=0)

---

### Punto 2 (25 pts) — Identifica y confronta
Asocia cada \(T(n)\) con un algoritmo plausible. Luego compara **dos pares** y encuentra el umbral de `n` con un `for` + `if`.

- T1(n) = 3n^2 + 50n  
- T2(n) = 8nlog2(n) + 200 
- T3(n) = 0.2n^3
- T4(n) = 2^n

///  respuesta
  -import math

def compare():
    variable = 0
    for n in range(1, 100):
        if (3 * n ** 2 + 50 * n):
            variable = n
            return n

print(compare())
n=9
print(3 * n ** 2 + 50 * n) insertion 
-def compares():
    
    for n in range(1, 100):
        if (8 * n * math.log2(n)):
            
         return n
compare = compares()
print(f"El cruce ocurre cerca de n ≈ {compares}")
print(f"Conclusión: Para n ≥ {compares}")

-def compare2():
    variable = 0
    for n in range(1, 100):
        if (n**2 + 2**n):
            variable = n
            return n
print(compare2())
n=9
print(n + 2 ** n) 

Algoritmos posibles:  
- Insertion/Bubble (peor caso)  
- Merge/Heapsort  
- Floyd–Warshall (triple bucle)  
- Backtracking/Fuerza bruta  

---

### Punto 3 (25 pts) — Ejercicio lógico
#### Isaac y los intervalos mágicos

Isaac, convencido de que tiene un talento especial para los números, asegura que puede contar al instante cuántos primos existen en cualquier rango que le propongan sus amigos. Para comprobarlo, ellos le entregan una lista con N pares de números (a,b), y él debe responder de inmediato cuántos números primos hay en cada intervalo. A partir de esta historia, elabora el análisis necesario para resolver el problema y define claramente qué se recibe como entrada, qué se debe producir como salida y qué lógica se requiere para verificar la afirmación de Isaac. 
Respuesta 
entradas 
una variable para capturar el 1 intervalo 
segunda variable para capturar el segundo intervalo 
contador que me vaya contando los numeros primos que vaya encontrando
salida 
mensaje diciendo si es primo o no 
---

### Punto 4 (25 pts) — Cuestionario

[![Click here!!](https://cf.quizizz.com/img/wayground/brand/plans/logo-basic.png)](https://wayground.com/join?gc=846438)
