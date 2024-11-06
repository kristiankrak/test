import random
N = int(input("Číslo od 1 až 10: "))
A = []
for i in range(N):
    A.append(random.randint(1, 15))
print("Původní pole náhodných čísel:")
print(A)
for i in range(N-1):
    for j in range(i+1, N):
        if A[i] < A[j]:
           
            P = A[i]
            A[i] = A[j]
            A[j] = P

            
print("Seřazené pole (sestupně):")
print(A)