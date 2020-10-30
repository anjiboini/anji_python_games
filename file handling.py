obj=open("D:/anji_python software/python/python projects2/thanu1.txt","w")
obj.write("welcome to india thanusrinbhvnhvb yeshu")
obj.close()


obj.close()
obj=open("D:/anji_python software/python/python projects2/thanu1.txt","a")
obj.write("  thanu sri")

obj=open("D:/anji_python software/python/python projects2/thanu1.txt","r")
a = obj.read()
print(a)
obj.close()
