#// TESTS
#// l1=['hello','how','are','you','doing','today','are','you','okay']
#// l2=['hi','bro','how','are','you','this','morning']
#// l3=['hello','how','you','doing','what','are','you','doing','today']
#//
#//reader=[l1,l2,l3]

def addXtimesYInList(X,Y,Liste):
	for i in range(X):
		Liste.append(Y)

#// Lecture csv
import csv
f = open('./Desktop/trng.csv', 'r')
render=csv.reader(f)

#// On met le contenu du csv dans un tableau sous la forme [[tweet1],[tweet2],...]
reader=[]
for row in render:
    lempty=[]
    lempty.append(row[1])
    reader.append(lempty)

ngrams1=[]
ngrams2=[]
ngrams3=[]
ngrams4=[]
ngrams5=[]

ngrams1brut=[]
ngrams2brut=[]
ngrams3brut=[]
ngrams4brut=[]
ngrams5brut=[]

ngrams1unite=[]
ngrams2unite=[]
ngrams3unite=[]
ngrams4unite=[]
ngrams5unite=[]

for l in reader :
    #// Suppression des #,@,RT, et liens
    l[0]=" ".join(filter(lambda x:x[0]!='#' and x[0]!='@' and (not x.startswith('http')) and x!='RT', l[0].split()))
	l[0]=l[0].split()
	#// Création des Ngrams
	ngrams1unite = [(l[i]) for i in range(len(l))]
	ngrams2unite = [(l[i],l[i+1]) for i in range(len(l)-1)]
	ngrams3unite = [(l[i],l[i+1],l[i+2]) for i in range(len(l)-2)]
	ngrams4unite = [(l[i],l[i+1],l[i+2],l[i+3]) for i in range(len(l)-3)]
	ngrams5unite = [(l[i],l[i+1],l[i+2],l[i+3],l[i+4]) for i in range(len(l)-4)]

	#// Transformer en liste la structure de Counter
    comptagengrams1unite = Counter(ngrams1unite).most_common()
	comptagengrams2unite = Counter(ngrams2unite).most_common()
	comptagengrams3unite = Counter(ngrams3unite).most_common()
	comptagengrams4unite = Counter(ngrams4unite).most_common()
	comptagengrams5unite = Counter(ngrams5unite).most_common()

	#// Mettre à jour le compteur de ngrams totaux
	for i in range(len(comptagengrams1unite)):
		addXtimesYInList(comptagengrams1unite[i][1],comptagengrams1unite[i][0],ngrams1brut)
	for i in range(len(comptagengrams2unite)):
		addXtimesYInList(comptagengrams2unite[i][1],comptagengrams2unite[i][0],ngrams2brut)
	for i in range(len(comptagengrams3unite)):
		addXtimesYInList(comptagengrams3unite[i][1],comptagengrams3unite[i][0],ngrams3brut)
	for i in range(len(comptagengrams4unite)):
		addXtimesYInList(comptagengrams4unite[i][1],comptagengrams4unite[i][0],ngrams4brut)
	for i in range(len(comptagengrams5unite)):
		addXtimesYInList(comptagengrams5unite[i][1],comptagengrams5unite[i][0],ngrams5brut)

#// Création du recap des Ngrams de tous les tweets sous forme de tables de hash
ngrams1 = { i : ngrams1brut.count(i) for i in ngrams1brut }
ngrams2 = { i : ngrams2brut.count(i) for i in ngrams2brut }
ngrams3 = { i : ngrams3brut.count(i) for i in ngrams3brut }
ngrams4 = { i : ngrams4brut.count(i) for i in ngrams4brut }
ngrams5 = { i : ngrams5brut.count(i) for i in ngrams5brut }
