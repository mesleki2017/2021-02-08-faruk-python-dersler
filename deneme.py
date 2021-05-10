

liste1 = ["G", "L", "G", "L", "G", "L", "G"]
liste2 = ["G", "L", "L", "G"]

liste3 = ["G", "R", "G",    "L", "G", "R",
          "G", "R", "G",   "G", "R", "G",  "G"]


yon = 0
yonstep = 90
x = 0
y = 0

for komut in liste3:
    if komut == "R":
        yon = yon+yonstep
    if komut == "L":
        yon = yon-yonstep

    if komut == "G":
        if yon == 0:
            x = x+1
        if yon == 90 or yon == -270:
            y = y+1
        if yon == 180 or yon == -180:
            x = x-1
        if yon == 270 or yon == -90:
            y = y-1


print(x, y)

if x == 0 and y == 0:
    print("ok geri donduk")
else:
    print("geri donmedi")
