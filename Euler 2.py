            # Question 2 // Soru 2

#            By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. fib:(1,2,3,5,8,...)

#            Fibonacci dizisindeki değerleri dört milyonu geçmeyen terimleri dikkate alarak çift değerli terimlerin toplamını bulun. fib:(1,2,3,5,8,...)

flag1 = 1
flag2 = 2
total = 0
liste = [1,2]
liste2 = list()
while total < 4000000:
    total = flag1 + flag2
    flag1 = flag2
    flag2 = total
    liste.append(total)

for i in liste:
    if i % 2 == 0:
        liste2.append(i)
    i += 1



print(liste)

print(sum(liste2))

