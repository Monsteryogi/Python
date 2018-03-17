# code for converting String

pyg ='ay'                                            #piglatin

original = input('Enter a word:')

print ("Original word to piglatin:")

if len(original) > 0 and original.isalpha():         #checking string is not empty and it contain only characters
  word=original.lower()                              #converting characters to lower case
  first=word[0]                                      #removing first character
  new_word=word+first + pyg                          #concating the strings
  new_word=new_word[1:len(new_word)]                 #generating piglatin word
  print (new_word)                                   #print word
elif len(original)<=0:
  print ('String is Empty.')
else:
  print ("Enter only Characters")


print ("piglatin to Original")
if len(original) > 0 and original.isalpha():
    word=new_word.lower()
    first=new_word[len(original)-1]
    redrive=first+new_word[0:len(original)-1]
    print (redrive)
else:
    print ("Empty")