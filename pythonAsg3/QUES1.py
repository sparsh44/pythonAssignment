enteredString=str(input("Enter The String : "))

#if space " " is present 
if " " in enteredString:
    #we will check frequency of words
    freq1=dict()
    words=enteredString.split() 
    #traversing list of words
    for word in words:
        if word in freq1:
            freq1[word]=freq1[word]+1
        else:
            freq1[word]=1
    for freq in freq1:
        print(freq,freq1[freq])

# if no space means singal word
else:
    #we will check frequency of alphabets
    freq2=dict()
    
    for letter in enteredString:
        if letter in freq2:
            freq2[letter]=freq2[letter]+1
        else:
            freq2[letter]=1
    for freq in freq2:
        print(freq,freq2[freq])