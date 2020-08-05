words=['apple','orange','banana','ankle']
words_1=[]
for i in words:
    words_1.append([str(j) for j in str(i)])
inp=str(input(">"))
inp_list=[str(i) for i in inp]
count=0
for i in words_1:
    count+=1
    for j in range(len(i)):
        if inp_list[0:]==i[0:j]:
            print(words[count-1])
