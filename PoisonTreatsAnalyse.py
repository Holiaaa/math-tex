import json

# Code qui a servi pour l'analyse des données recueilli grace a la page web
# Par Téo JAUFFRET (holiaaa.github.io/math-tex)

numbers_with_one = []
first_number = []
i = 1
while i <= 20:
    with open(f"pick_a_treat_stats ({i}).json", 'r') as f:
        data = json.loads(f.read())
        f.close()

    for key, value in data["resultats"].items():
        if value == 1:
            num = int(key)
            numbers_with_one.append(num)
    
    first_number.append(int(data["first_button"]))
    
    i += 1

from collections import Counter
import matplotlib.pyplot as plt 

counts = Counter(number_with_one)

x = sorted(counts.keys())
y = [counts[i] for i in x]

plt.figure(figsize=(12, 5))
plt.bar(x, y)

plt.xlabel("Nombre")
plt.ylabel("Fréquence")
plt.title("Fréquence des nombres")

plt.xticks(x)
plt.savefig("frequence_des_nombres.png", dpi=300, bbox_inches="tight")
plt.show()
