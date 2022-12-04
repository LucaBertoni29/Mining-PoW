import math

""" p rappresente la probabilità che un nodo onesto scopra il blocco successivo
    q è la probabilità che l'attaccante scopra il blocco successivo, ovvero la potenza totale di calcolo che controlla
    z è la probabilità che l'attaccante recuperi z blocchi di svantaggio """

def attackerSuccessProbability(q, z):
    p = 1.0 - q
    Lambda = z * (q / p)
    sum = 1.0

    for k in range(z+1):
        poisson = math.exp(-Lambda)
        for i in range(1, k+1):
            poisson *= (Lambda / i)
        sum -= poisson * (1 - math.pow(q / p, z - k))
    return sum


q = float(input("Inserire la probabilità che l'attaccante scopra il blocco successivo: "))
print ("\n")

print ("z |  P")
print ("---------------------------------------------------------------------------")

for i in range (10):
        print(f"{i} {attackerSuccessProbability(q, i):10f}")
