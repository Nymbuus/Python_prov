#Author: Marcus Nilsson
#Date: 2023-10-12
print("Hejsan, nu har programmet startat!")
print("Ei22 - praktiskt prov ht23")
res = []
serie_sum = 0
parallellsum = 0

res = input("Ange resistorer: ").split()

for i in range(0,len(res)):
    serie_sum += int(res[i])
    parallellsum += pow(int(res[i]), -1)

parallellsum = pow(parallellsum, -1)

print(f"Serieresistans: {serie_sum}")
print(f"Parallellresistans: {parallellsum}")