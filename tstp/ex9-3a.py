import csv

movies = [["Top Gun", "Riskey Business", "Minority Report"], ["Titanic","The Revenant", "Inception"],["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)


with open("movies.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
