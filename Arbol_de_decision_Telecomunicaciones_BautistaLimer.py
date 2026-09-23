import math

#datos del conjunto original
total = 10

acept_total = 5
negar_total = 5

#entropia
psi = acept_total / total
pno = negar_total / total

hs = -(psi * math.log2(psi) + pno *math.log2(pno))

#_______________________________________________________________________________________________________________________________________

#Joven (≤30), Adulto (31–50), Mayor (>50)

#Joven id 1, 3, 8 : edades 24, 29, 27 : 3 personas : no tienen linea fija : Todas negaron
# id 1 : 2.5    no
# id 3 : 3.0    no
# id 8 : 2.0    no

#Adulto id 2, 4, 6, 7, 9, 10 : edades 38, 45, 33, 41, 36, 31 : 6 personas : 4 tienen linea fija, 2 no tienen : 4 aceptaron y 2 negaron
# id 2 : 6.0    si
# id 4 : 8.0    si
# id 6 : 4.0    no
# id 7 : 5.5    si
# id 9 : 6.5    si
# id 10: 3.5    no

#Mayor id 5 : edad 52 : 1 persona : tiene linea fija : aceptó
# id 5 : 7.5

#_______________________________________________________________________________________________________________________________________

#entropia en cada grupo

def entropy(p1, p2):
    total = p1 + p2
    if total == 0 or p1 == 0 or p2 == 0:
        return 0.0
    p1 /= total
    p2 /= total
    return - (p1 * math.log2(p1) + p2 * math.log2(p2))

#----------------------edad-------------------------
# Joven: 0 sí, 3 no
h_joven = entropy(0, 3)
# Adulto: 4 sí, 2 no
h_adulto = entropy(4, 2)
# Mayor: 1 sí, 0 no
h_mayor = entropy(1, 0)

h_div_edad = (3/10)*h_joven + (6/10)*h_adulto + (1/10)*h_mayor
ganancia_edad = hs - h_div_edad

#----------------------linea-------------------------
h_linea_si = entropy(4, 1) # con linea 4 si y 1 no
h_linea_no = entropy(1, 4) # sin linea 1 si y 4 no

h_div_linea = (5/10) * h_linea_si + (5/10) * h_linea_no
ganancia_linea = hs - h_div_linea 

#----------------------datos-------------------------  (agrupado: Bajo ≤3GB, Medio 3.1–6GB, Alto >6GB) 
h_datos_bajo = entropy(0,3)  
h_datos_medio = entropy(2,2)
h_datos_alto = entropy(3,0)

h_div_datos = (3/10) * h_datos_bajo + (4/10) * h_datos_medio + (3/10) * h_datos_alto
ganancia_datos = hs - h_div_datos

#----------------------output------------------------
print("entropia inicial: ", hs)
 
print("EDAD")
print("entropia ponderada: ", h_div_edad)
print("ganancia (edad): ", ganancia_edad)

print("LINEA")
print("entropia ponderada: ", h_div_linea)
print("ganancia (linea): ", ganancia_linea)

print("DATOS")
print("H(bajo): ", h_datos_bajo)
print("H(medio): ", h_datos_medio)
print("H(alto): ", h_datos_alto)
print("entropia ponderada: ", h_div_datos)
print("ganancia datos: ", ganancia_datos)

# Selección del mejor nodo raíz
ganancias = {
    "edad": ganancia_edad,
    "tiene linea": ganancia_linea,
    "uso d datos": ganancia_datos
    
}
mejor_atributo = max(ganancias, key=ganancias.get)
print(f"el mejor atributo para la raíz del árbol es: {mejor_atributo} (Gain = {ganancias[mejor_atributo]})")
