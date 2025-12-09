# 1
matritsa = [[1, 2], [3, 4], [5, 6]]
tekis = [son for qator in matritsa for son in qator]
print(tekis)

# 2
sozlar = ["dog", "cat", "mouse"]
bosh_harflar = [soz[0] for soz in sozlar]
print(bosh_harflar)

# 3
sonlar = [-5, 3, -1, 0, 7, -2]
musbatlar = [i for i in sonlar if i > 0]
print(musbatlar)

# 4
juft_toq = ["juft" if i % 2 == 0 else "toq" for i in range(1, 11)]
print(juft_toq)

# 5
import math
sonlar = [4, 9, 16, 25]
ildizlar = [math.sqrt(i) for i in sonlar]
print(ildizlar)

# 6
bolinadiganlar = [i for i in range(0, 51) if i % 5 == 0]
print(bolinadiganlar)
