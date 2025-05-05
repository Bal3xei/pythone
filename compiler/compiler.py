import datetime, re
with open ("compiler/input.txt", "r") as f:
    content = f.readlines()

with open ("compiler/output.txt", "a") as f:
    data = str(datetime.datetime.now())[:-7]+ "\n" 
    f.write(data)
    for line in content: 
        data = str(datetime.datetime.now())
        info = " "*20 + line
        f.write(info)

    f.write("\n")
