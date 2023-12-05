f = open("access.log", "r")
for line in f:
    line = line.strip()
    if ('Firefox/112.0' and '/adm') in line:
        print(line)