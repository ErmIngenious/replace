#variable with a long string 
sentence = 'The!quick!brown!fox!jumps!over!the!lazy!dog.'

#covert sentence to uppercase, replace puntuation mark with space and print output.

 
print  (sentence.upper().replace('!', ' '))

#covert sentence to uppercase, replace puntuation mark with space and print output in reverse.
print(sentence.upper().replace('!', ' ')
[::-1])

