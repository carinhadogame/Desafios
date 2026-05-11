# ================================
# OPERAÇÕES COM LISTAS EM PYTHON
# ================================

# 1. Criando listas
frutas = ["maçã", "banana", "laranja"]
numeros = [5, 2, 8, 1, 9]

print("Lista inicial:", frutas)

# -------------------------------
# 2. Adicionar elementos
# -------------------------------

# append (final)
frutas.append("morango")
print("Após append:", frutas)

# insert (posição específica)
frutas.insert(1, "kiwi")
print("Após insert:", frutas)

# -------------------------------
# 3. Remover elementos
# -------------------------------

# remove (valor)
frutas.remove("banana")
print("Após remove:", frutas)

# pop (índice)
frutas.pop(2)
print("Após pop:", frutas)

# -------------------------------
# 4. Modificar elementos
# -------------------------------

frutas[0] = "abacaxi"
print("Após modificação:", frutas)

# -------------------------------
# 5. Concatenar listas
# -------------------------------

nova_lista = frutas + ["uva", "manga"]
print("Concatenação:", nova_lista)

# -------------------------------
# 6. Tamanho da lista
# -------------------------------

print("Tamanho:", len(frutas))

# -------------------------------
# 7. Verificar elemento
# -------------------------------

print("Tem 'uva'?", "uva" in frutas)

# -------------------------------
# 8. Ordenar lista
# -------------------------------

numeros.sort()
print("Ordenada:", numeros)

# -------------------------------
# 9. Inverter lista
# -------------------------------

numeros.reverse()
print("Invertida:", numeros)

# -------------------------------
# 10. Percorrer lista (for)
# -------------------------------

print("Loop for:")
for fruta in frutas:
    print(fruta)

# -------------------------------
# 11. Percorrer lista (while)
# -------------------------------

print("Loop while:")
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

# -------------------------------
# 12. Lista aninhada
# -------------------------------

matriz = [[1, 2], [3, 4]]
print("Elemento matriz[0][1]:", matriz[0][1])

# -------------------------------
# 13. Compreensão de listas
# -------------------------------

quadrados = [x**2 for x in range(1, 6)]
print("Quadrados:", quadrados)

# -------------------------------
# 14. Exemplo de pilha (extra)
# -------------------------------

pilha = []
pilha.append(1)
pilha.append(2)
pilha.append(3)

print("Pilha:", pilha)

pilha.pop()
print("Após desempilhar:", pilha)