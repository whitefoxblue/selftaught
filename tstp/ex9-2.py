answer = input("What is your name? ")

with open("answer.txt", "w") as f:
    f.write(answer)


with open("answer.txt", "r") as g:
    print(g.read())
