# Árbol de Decisión: Predicción de Aceptación en Telecomunicaciones

Este repositorio contiene la implementación y el cálculo analítico de **Ganancia de Información (Information Gain)** y **Entropía de Shannon** para seleccionar el nodo raíz de un Árbol de Decisión en un conjunto de datos sobre clientes de telecomunicaciones.

---

## 📄 Contenido del Repositorio

* `Arbol_de_decision_Telecomunicaciones_BautistaLimer.py`: Script en Python que calcula la entropía inicial del sistema, las entropías ponderadas por atributo y las ganancias de información para determinar la raíz del árbol.

---

## 📊 Dataset de Trabajo

El conjunto de datos evalúa a **10 clientes** según tres atributos principales (`edad`, `linea_fija`, `uso_datos`), determinando la clase objetivo de **aceptación del servicio** (5 aceptaron / 5 negaron).

### Agrupación y Clasificación de Datos:

1. **Atributo `Edad`:**
   * **Joven ($\le 30$):** 3 personas (0 aceptan, 3 niegan)
   * **Adulto ($31 \text{ a } 50$):** 6 personas (4 aceptan, 2 niegan)
   * **Mayor ($> 50$):** 1 persona (1 acepta, 0 niegan)

2. **Atributo `Línea Fija`:**
   * **Con línea fija:** 5 personas (4 aceptan, 1 niega)
   * **Sin línea fija:** 5 personas (1 acepta, 4 niegan)

3. **Atributo `Uso de Datos`:**
   * **Bajo ($\le 3 \text{ GB}$):** 3 personas (0 aceptan, 3 niegan)
   * **Medio ($3.1 \text{ a } 6 \text{ GB}$):** 4 personas (2 aceptan, 2 niegan)
   * **Alto ($> 6 \text{ GB}$):** 3 personas (3 aceptan, 0 niegan)

---

## 📐 Marco Teórico y Fórmulas

### 1. Entropía de Shannon $H(S)$

$$H(S) = - \sum_{i=1}^{k} p_i \log_2(p_i)$$

Para la entropía inicial del dataset ($P = 5, N = 5$):

$$H(S) = -\left(\frac{5}{10} \log_2\left(\frac{5}{10}\right) + \frac{5}{10} \log_2\left(\frac{5}{10}\right)\right) = 1.000\text{ bit}$$

---

### 2. Ganancia de Información $Gain(S, A)$

$$\text{Gain}(S, A) = H(S) - \sum_{v \in \text{Valores}(A)} \frac{\vert{}S_v\vert{}}{\vert{}S\vert{}} H(S_v)$$

---

## 📊 Resultados de Ganancia por Atributo

| Atributo | Entropía Ponderada $H_A(S)$ | Ganancia de Información $Gain(S, A)$ |
| :--- | :---: | :---: |
| **Uso de Datos** | **0.4000** | **0.6000** 🏆 |
| **Edad** | **0.5510** | **0.4490** |
| **Línea F
