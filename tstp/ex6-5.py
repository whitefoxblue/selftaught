wordlist= ["The", "fox", "jumped", "over", "the", "fence", "."]
sentence = " ".join(wordlist)
#sentence = sentence.replace(" .",".")
sentence = sentence[0:-2] + "."
print(sentence)
