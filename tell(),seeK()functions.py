#talk ()fuction
f=open("talk.txt")
print(f.tell())
print(f.readline(16))
f.close
#seek()function
f=open("talk.txt")
print(f.readline())
f.seek(7)
print(f.readline())
f.close
