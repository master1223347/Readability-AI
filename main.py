text = input("text")

def letters(text):
    x = 0
    for i in range(len(text)):
        if text[i].isalpha() == True:
            x = x+1
    return x
L = letters(text)

def sentences(text):
    x = 0
    for i in range(len(text)):
        if text[i] == "!" or text[i] == "." or text[i] == "?":
            x = x +1
    return x
S = sentences(text)

def WPH(text):
    x = 0
    for i in range(len(text)):
        if text[i] == " ":
            x = x+1
    x = x+1
    return x
words = WPH(text)

S = S/words * 100
L = L/words * 100

index = 0.0588 * L - 0.296 * S - 15.8
grade = round(index)

if grade >= 16:
    print("Grade 16+")
elif grade <=1:
    print("Before Grade 1")
else:
    print("Grade " + str(grade))



#get number of letters -
#get number of sentences -
#get words per hundred -
#multiply with words per hundred -
#enter into equation -
#round - DONE
#if it is 16+ enter 16+ -
#if it is under 1 enter under 1 -
#print -
# 0.0588 * L - 0.296 * S - 15.8

