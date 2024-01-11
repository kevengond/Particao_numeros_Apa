import random


def two_way_number_partitioning(V):
 """
 Resolve o problema da partição de números usando um algoritmo guloso.

 Args:
  V: Um conjunto de números inteiros positivos.

 Returns:
  A solução para o problema, representada por um tuplo (V1, V2), onde V1 e V2
  são os subconjuntos resultantes.
 """

 V1 = []
 V2 = deque()

 # Adiciona o número mais pequeno de V a um dos subconjuntos.

 n = min(V)
 V1.append(n)
 V.remove(n)

 # Adiciona os números restantes a um dos subconjuntos, de modo a minimizar
 # a diferença das somas dos subconjuntos.

 while V:
  if sum(V1) > sum(V2):
   V2.append(V.pop())
  else:
   V1.append(V.pop())

 # Adiciona um mecanismo de corte

 if abs(sum(V1) - sum(V2)) <= 1:
  break

 return (V1, V2)


V = [i for i in range(1, 101)]

(V1, V2) = two_way_number_partitioning(V)
difference = len(V1) - len(V2)


print(V1, end="\n\n\n")
print(V2, end="\n\n\n")
print("|V1|-|V2| = {}".format(abs(difference)))
