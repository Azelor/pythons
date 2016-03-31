

aadressid = ["Mustika 15-6, 23456, Mustvee",
 "Oja 12-34, 23456, Mustvee",
 "Jaama 34-56, 12345, Keila",
 "Tartu mnt. 67-89, 12456, Tallinn"]

aadr = aadressid[0].split(",")

print(aadr)

# teha for loop, mis käib läbi otsingusõna ja prindib kõik sobivad.
# probleem selles, et kui tänavanimi kattub linnanimega siis annab vale tulemi

a = "Mustika 15-6, 23456, Mustvee"

nugis = a.split(",")[-1].strip()

print(nugis)
