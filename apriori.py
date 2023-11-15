
def freqGreaterThanOrEqualTOMinSupport(db,newItemSet):
	cnt = 0
	for row in db:
		if set(newItemSet).issubset(set(row)):
			cnt = cnt + 1
	return cnt >= min_support

# based on downward closure property - for any frequent itemset, it's subset is also frequent 
def prune(L,k,newItemSet):
	for i in range(len(newItemSet)):
		smallItemset = newItemSet[0:i] + newItemSet[i+1:]
		if smallItemset not in L[k-1]:
			return False
	return True

def candidate_gen(L,C,k):
	n = len(L[k-1])
	for i in range(n-1):
		for j in range(i+1,n):
			if L[k-1][i][0:k-1] == L[k-1][j][0:k-1]:
				newItemSet = L[k-1][i] + [ L[k-1][j][k-1] ]
				if prune(L,k,newItemSet):
					C[k].append(newItemSet)
					if freqGreaterThanOrEqualTOMinSupport(db,newItemSet):
						L[k].append(newItemSet)
			else:
				break

def start(L,C,k,db):
	count = {}
	for line in db:
		for item in line:
			if item in count:
				count[item]+=  1
			else:
				count[item] = 1
				C[k].append([item])  

			if count[item] >= min_support and [item] not in L[k]:
				L[k].append([item])

	while len(L[k]) != 0:
		k = k + 1
		C.append([]) # to add itemsets to C[k]
		L.append([]) # to add itemsets to L[k]
		candidate_gen(L,C,k) # C[k] is filled



f = open('abc.txt')
db = f.readlines()
for i,line in enumerate(db):
	db[i] = line.split()
	db[i].sort()

print("DB: ",db)
min_support=int(input("Enter minimum support: ")) 
L = [[]]
C = [[]]
k = 0
start(L,C,k,db)


f=len(L)
print("ans=",L[f-2])

