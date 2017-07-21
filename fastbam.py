import re
import sys

# Use this for testing
bamFile = 'fakebam.bam'
fastqFile = 'fake_R2.fastq'

# # Use this for command line input
# bamFile = sys.argv[1]
# fastqFile = sys.argv[2]


with open(bamFile,'r') as f:
	# creates a library of unique crz tags with corresponding STS
    crzlib2 = {}
    # processes bam file one line at a time
    for line in f:
        st = re.search('(ST-[^\s]+)',line).group(0)
        crz = re.search('(CR:Z[^\s]+)',line).group(0)
        # print(crz,st)
        if not(crz in crzlib2):
            crzlib2[crz]=[st]
        elif st in crzlib2[crz]:
            pass
        else:
            crzlib2[crz].append(st)

### Possibly broken
## Output was incorrect on my machine, but correct on aislyn's
with open(fastqFile,'r') as f2:
    valid = 0
    for i, row in enumerate(f2):
        if i%4==0:
            fastq_sts = re.findall('(ST-[^\s]+)',row)
            for key in crzlib2.keys():
                if fastq_sts[0] in crzlib2[key]:
                    currentkey = key
                    valid=1
                    with open(currentkey.replace(':','_')+'.txt','a') as w:
                        w.write(row)
        else:
            if valid:
                with open(currentkey.replace(':','_')+'.txt','a') as w:
                        w.write(row)
            if i%4==3:
                valid=0
	