import csv

with open("movies.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["Top Gun", "Risky Business", "Minority Report"])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Training Day", "Man on Fire", "Flight"])

    
with open("movies.csv", "r") as g:
    r = csv.reader(g, delimiter=",")
    for row in r:
        print(",".join(row))
