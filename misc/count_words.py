import re
text = ''.join(open('a.txt').readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
for s in sentences:
        if(len(s.split())>16):
           print("(*)"+s+" ["+str(len(s.split()))+ "words"+"]"+"\n")
        else:
           print(s)
