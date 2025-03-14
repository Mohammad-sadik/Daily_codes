n = ["Ganesh", "Raj", "Mahi"]
h = [180,165,170]

new = {j : i for i, j in zip(n,h)}
op ={k :new.get(k) for k in sorted(h)}
print(op)