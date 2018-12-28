kyle = {'height': 67,
        'favorite color':'orange',
        'favorite author':'Scott Adams'}

#author = input("What is Kyle's favorite author?: ")

#if author == kyle['favorite author']:
#    print("Correct!", author, "is Kyle's favorite author!")
#else:
#    print("Sorry, that is not correct.")

answer = input("Type 'height', 'favorite color', or 'favorite author': ")
if answer in kyle:
    result = kyle[answer]
    print(result)
