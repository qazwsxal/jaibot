pronun = open("mpron.txt",'r')
jaipun = open("puns.txt",'w')
puns = 0
for line in pronun:
    if '/eI/' in line:
        puns = puns +1
        jaipun.write(line.split()[0])
        jaipun.write('\n')
jaipun.close()
print "run complete"
print "%d puns found" % puns
