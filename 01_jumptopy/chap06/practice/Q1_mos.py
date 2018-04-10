# 모스 부호를 dictionary 자료형으로 정의할것
alphabet_list={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z',}
original=input()
word_list=original.split('  ')
alphabet=[]
for word in word_list:
    for mos in word.split():
        alphabet.append(alphabet_list[mos])
    alphabet.append(' ')

for alpha in alphabet:
    print(alpha, end="")