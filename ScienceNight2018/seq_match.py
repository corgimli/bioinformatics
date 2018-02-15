import pandas as pd
from stringdist import levenshtein_norm as levn

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
dna_lib.index.name = 'Species'
dna_lib.reset_index(inplace=True)

test = 'AGACAGAGGAGAGTGGAATTTCGTGTG'

def match(test,threshold=0.8):
	dna_lib['% Match'] = dna_lib['Sequence'].apply(lambda x: 1-levn(x,test))

	if dna_lib['% Match'].any()>threshold:
		result = dna_lib[dna_lib['% Match']>threshold].sort_values(by='% Match',ascending=False)
		result['% Match']*=100
		return result.loc[:,['Species','% Match']].round({'% Match': 1})
	else:
		return pd.DataFrame(columns=['Species','% Match'])
