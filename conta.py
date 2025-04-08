saluto = 'File "<frozen importlib._bootstrap_external>", line 1059, in source_to_codeFile "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed File "./prog.py", line 9'
lista = list(saluto)
insieme = set(lista)


def conta(stringa):
    for x in insieme:
        count=0
        i=0
        for y in saluto:
            if x==saluto[i]:
                count+=1
            i+=1

        print(x,count)


conta(saluto)