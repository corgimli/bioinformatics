import pandas as pd
from stringdist import levenshtein_norm as levn
# from fuzzywuzzy import fuzz
from Levenshtein import ratio 

filename = 'samples_data_1.txt'

animals = []
seqs = []

with open(filename,'r') as f:
	for line in f:
		# line.strip('\n')
		if line[0]=='>':
			animal = line.rstrip()
			animals.append(animal[1:])
		else:
			seqs.append(line.rstrip())

dna_lib = pd.DataFrame.from_dict(dict(zip(animals,seqs)),orient='index').rename(columns={0:'Sequence'})
dna_lib.index.name = 'Source'
dna_lib.reset_index(inplace=True)
# dna_lib = pd.DataFrame(dict(zip(animals,seqs)).items(), columns = ['Animal','Sequence'])
# print(dna_lib)

test = 'AGACAGAGGAGAGTGGAATTTCGTGTG'

def match(test,threshold=0.8):
	dna_lib['match_lev'] = dna_lib['Sequence'].apply(lambda x: 1-levn(x,test))
# dna_lib['match_lev'] = dna_lib['Sequence'].apply(lambda x: 1-levn(x,test))
# dna_lib['match+fuzz'] = dna_lib['Sequence'].apply(lambda x: fuzz.ratio(x,test))
# print(dna_lib['match_lev'].sort_values(ascending=False)>0.8)

	if dna_lib['match_lev'].any()>threshold:
		return dna_lib[dna_lib['match_lev']>threshold].sort_values(by='match_lev',ascending=False)#.to_frame()
	else:
		return('ERROR: No match found. Please re-enter DNA sequence')
