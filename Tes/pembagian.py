a_file = open("input.in", "r")

data = []
for line in a_file:
  stripped_line = line.strip()
  data.append(stripped_line)

a_file.close()
def tes(x):
    if 1<=int(x[0])<=100:      
        case=[]
        if (len(x)-1)%3!=0:
            print("input tidak valid")
        else:
            iter=0
            for i in range(int(x[0])):
                bwh=int(x[1+3*iter])
                atas=int(x[2+3*iter])
                pbg=int(x[3+3*iter])
                if 1<=bwh<=atas<10000:
                    if 1<=pbg<10000:
                        hsl=pembagian(bwh,atas+1,pbg)
                        case.append(hsl)
                        iter=iter+1
                    else:
                        print("input tidak valid")
                else:
                    print("input tidak valid")
        for i in range(len(case)):
            print(f"Case {i+1}: {case[i]}")
    else:
        print("input tidak valid")
def pembagian(bwh,atas,pbg):
    counter=0
    for i in range(bwh,atas+1):
        if i%pbg==0:
            counter=counter+1
    return counter

tes(data)
