file__read = open('Codingal.txt','r')
print("File in Read Mode -")
print(file__read.read())
file__read.close()

file__write = open('Codingal.txt','w')
print(file__write.write("File in Write Mode"))
print(file__write.write("Hi! I am a Penguin. I am 1 yr. old"))
file__write.close()

file__append = open('Codingal.txt','a')
file__append.write("\n File in Append Mode -")
file__append.write("Hi! I am a Penguin. I am 1 yr. old")
file__append.close()