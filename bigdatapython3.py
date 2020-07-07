#// Fonction d'ajout d'un élément un certain nombre de fois dans une liste
def addXtimesYInList(X,Y,Liste):
	for i in range(X):
		Liste.append(Y)

#// Fonction de calcul du nb d'itérations d'un mot dans une phrase splitée
def nbIterationsMotdansPhrase(recherche,phrase):
    iterations=0
    for mot in phrase:
        if mot == recherche:
            iterations=iterations+1
    return iterations

#// Fonction qui renvoie si un mot est dans un set
def WordIsInSet(word,set):
    for item in set:
        if word==item :
            return True
    return False

#// Fonction qui vérifie s'il existe un pattern vérifié
def RespectPattern(phrase):
    size=len(phrase)
    if WordIsInSet(phrase[0],HFWords):                  #// Premier mot est un HFW
        if WordIsInSet(phrase[size-1],HFWords):         #// Dernier mot est un HFW
            for i in range(1,size-1):
                if WordIsInSet(phrase[i],CWords):       #// Contient un CW ou +
                    return True
    return False

#// Fonction de calcul du nb de ! dans une phrase splitée
def NbExclamat(phrase):
    i=0
    for s in phrase:
        i=i+s.count('!')
    return i

#// Fonction de calcul du nb de ? dans une phrase splitée
def NbQuest(phrase):
    i=0
    for s in phrase:
        i=i+s.count('?')
    return i

#// Fonction de calcul du nb de quotes dans une phrase splitée
def NbQuotes(phrase):
    i=0
    for s in phrase:
        i=i+s.count('`')
    return i

#// Fonction de calcul du nb de mot en maj dans une phrase splitée
def NbCapitalized(phrase):
    i=0
    for j in range(len(phrase)):
        if phrase[j].isupper():
            i=i+1
    return i

#// Lecture csv
import csv
import collections
f = open('./trng.csv', 'r')
render=csv.reader(f)

#// On met le contenu du csv dans un tableau sous la forme [[tweet1],[tweet2],...]
reader=[]
for row in render:
    lempty=[]
    lempty.append(row[1])
    reader.append(lempty)

NbNgramsInTweet=[]
NbWordsInTweet=[]
CountWords=[]
Frequencies=[]
PatternNumb=[]
PatternFreq=[]
FrequenciesInTweet=[]
PunctuationFeatureInTweet=[]
PunctuationFeature=[]
HFWords=[]
RWords=[]
CWords=[]
WordsInTweet=[]

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
    l[0] = " ".join(filter(lambda x:x[0]!='#' and x[0]!='@' and (not x.startswith('http')) and x!='RT' and x!="." and x!="," and x!="!" and x!="?" and x!=";" and x!=":", l[0].split()))
    l=l[0].split()

    #// Création des Ngrams
    ngrams1unite = [(l[i]) for i in range(len(l))]
    ngrams2unite = [(l[i],l[i+1]) for i in range(len(l)-1)]
    ngrams3unite = [(l[i],l[i+1],l[i+2]) for i in range(len(l)-2)]
    ngrams4unite = [(l[i],l[i+1],l[i+2],l[i+3]) for i in range(len(l)-3)]
    ngrams5unite = [(l[i],l[i+1],l[i+2],l[i+3],l[i+4]) for i in range(len(l)-4)]

    NbNgramsInTweet.append(len(ngrams1unite)+len(ngrams2unite)+len(ngrams3unite)+len(ngrams4unite)+len(ngrams5unite))

	#// Transformer en liste la structure de Counter
    comptagengrams1unite = collections.Counter(ngrams1unite).most_common()
    comptagengrams2unite = collections.Counter(ngrams2unite).most_common()
    comptagengrams3unite = collections.Counter(ngrams3unite).most_common()
    comptagengrams4unite = collections.Counter(ngrams4unite).most_common()
    comptagengrams5unite = collections.Counter(ngrams5unite).most_common()

    WordsInTweet.append(comptagengrams1unite)
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

#// Analyse de tous les tweets et création d'un tableau de tableau avec les mots et le nb d'apparition
#// Ex.:  CountWords=[ [(tweet1_mot1,freq_t1_m1),(tweet1_mot2,freq_t1_m2)] , [(tweet2_mot1,freq_t2_m1),(tweet2_mot2,freq_t2_m2)] ]
index=0
for l in reader :
    l=l[0].split()
    CountWords.append([])
    CountWords[index].append({l[i] : nbIterationsMotdansPhrase(l[i],l) for i in range(len(l))})
    NbWordsInTweet.append(len(l))
    index=index+1

#// Calcul des fréquences d'apparition des mots dans les tweets
#// Ex.:  FrequenciesInTweet=[ [tweet1 {mot_1 : freq_mot_1_t1},{mot_2 : freq_mot_2_t1}] , [tweet2 {mot_1 : freq_mot_1_t2},{mot_2 : freq_mot_2_t2}] ]
index=0
for l in reader :
    l=l[0].split()
    FrequenciesInTweet.append([])
    for i in range(len(l)):
        FrequenciesInTweet[index].append({l[i] : CountWords[index][0].get(l[i])/ngrams1[l[i]]})
    index=index+1

#// Calcul des fréquences d'apparition des mots dans les tweets par rapport au total
#// Ex.:  FrequenciesInTweet=[ [tweet1 {mot_1 : freq_mot_1},{mot_2 : freq_mot_2}] , [tweet2 {mot_1 : freq_mot_1},{mot_2 : freq_mot_2}] ]
index = 0
NbWords = len(ngrams1brut)
for l in reader :
    l=l[0].split()
    Frequencies.append([])
    for i in range(len(l)):
        Frequencies[index].append([l[i] , ngrams1[l[i]]/NbWords])
    index=index+1

#// Création des HFWords, des CWords et RWords
for tweet in Frequencies :
    for i in range(len(tweet)) :
        if tweet[i][1]>=0.00001 and tweet[i][1]<=0.000505:
            HFWords.append(tweet[i][0])
        elif tweet[i][1]>=0.000505 and tweet[i][1]<=0.001:
            CWords.append(tweet[i][0])
        else:
            RWords.append(tweet[i][0])

#// Calcul de la pattern feature
index=0
for l in reader :
    l=l[0].split()
    PatternNumb.append(0)
    PatternFreq.append(0)
    for i in range(len(l)):
        if RespectPattern(l):
            PatternNumb[index]=PatternNumb[index]+1
            PatternFreq[index]=PatternNumb[index]/sum(PatternNumb)
    index=index+1


#// Calculs intermédiaires : punctuation feature par tweet
for l in reader :
    l=l[0].split()
    PunctuationFeatureInTweet.append(len(l)+NbExclamat(l)+NbQuest(l)+NbQuotes(l)+NbCapitalized(l))

#// Calcul de la punctuation feature totale
#// Mw = max(NbWordsInTweet)
#// Mng = max(NbNgramsInTweet)
#// Mpa = max(PatternNumb)
#// Mp = max(PunctuationFeatureInTweet)
index=0
for i in range(len(reader)) :
    PunctuationFeature.append(PunctuationFeatureInTweet[i]/(max(PunctuationFeatureInTweet)*(max(NbWordsInTweet)+max(NbNgramsInTweet)+max(PatternNumb))/3))
    index=index+1

NbTotalNgram = sum(NbNgramsInTweet)

for i in range(len(NbNgramsInTweet)):
    NbNgramsInTweet[i]=NbNgramsInTweet[i]/NbTotalNgram

#print(NbNgramsInTweet)             #wNgrams
#print(NbWordsInTweet)              #wWords
#print(PatternFreq)                 #wPattern
#print(PunctuationFeature)          #wPunctuation

FeaturesVector = []
index=0
for l in reader :
    FeaturesVector.append([NbNgramsInTweet[index],NbWordsInTweet[index],PatternFreq[index],PunctuationFeature[index]])
    index=index+1

print(FeaturesVector)


#################################

#-print(CountWords)
#-print(Frequencies)
#-print(FrequenciesInTweet)
