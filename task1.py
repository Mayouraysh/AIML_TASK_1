cricket_file = open("cricket.txt","r")
result = cricket_file.read()
cricket_file.close()


wordlist = result.split()
wordcount = {}
for word in wordlist:
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1
for key, value in wordcount.items():
    print(f"{key} : {value}")

   
analysisfile = open("analysis.txt", "w")
for key, value in wordcount.items():
    analysisfile.write(f"{key} : {value}\n")
analysisfile.close()
