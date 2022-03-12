#shortest route
import math

hos = {'A':[[2, 1], 20],
            'B':[[8, 7], 12],
            'C':[[-5,-7],34],
            'D':[[5.5,-6],56],
            'E':[[5,5],23],
            'F':[[7,0.5],12],
            'G':[[-6,-5],43],
            'H':[[-3,-5],62],
            'I':[[-2,1.5],15],
            'J':[[3,-2],21],
            'K':[[-4,2],19],
            'L':[[1,9],3],
            'M':[[1.5,-8],15],
            'N':[[6,3],27],
            'O':[[-8,-2],25]
            }


here = input("Your Hospital: ")



p = hos[here][0]

route={}

for h, i in hos.items():
    cap = i[1]
    if h==here or cap<=0:
        continue
    q=i[0]
    dis = float("{:.2f}".format(math.dist(p, q)))
    route[h] = dis


sort_route = sorted(route.items(), key=lambda x: x[1])
print("Referral Hospitals and distances: ")
for i in sort_route:
	print(f'{i[0]}, {i[1]}')

print(f'total: {len(sort_route)} from {len(origi_hos)}')

#selection (in case just 1 choice)
s = input("choose: ")
for m, n in hos.items():
    if s == m:
        n[1]-=1
        hos[here][1]+=1

'''check capacity apdate
print(hos)'''