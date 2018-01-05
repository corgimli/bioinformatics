

from bs4 import BeautifulSoup
import csv
import re
import requests

# URL for metabolic pathway table
table_URL = 'http://www.bmrb.wisc.edu/data_library/Genes/Metabolic_Pathway_table.html'

# Retrieve html for metabolic pathway table (webpage)
r  = requests.get(table_URL)
soup = BeautifulSoup(r.text,'lxml')

# Find all metabolism types on the page
metabolisms = soup.find_all('h1',id=True)

# Create csv for output
with open('metabolic_pathways.csv', 'w') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['parent','sub','gene'])

    # for each metabolism from the list found...
    for met in metabolisms:
        ##print(met['id'])

        # find all sub-pathways on the page
        paths = met.find_next('ul').select('li > a')
        for path in paths:
            ##print('-',re.split('\/|\.',path['href'])[1])

            # Retrieve url for the sub-pathway
            pathway = re.split('\/|\.',path['href'])[1]
            pathref = path['href']
            URL = 'http://www.bmrb.wisc.edu/data_library/Genes/'+pathref
            # Retrieve html for sub-pathway 
            s  = requests.get(URL)
            soup2 = BeautifulSoup(s.text,'lxml')

            # Search for the table with genes...
            rows = soup2.find('table',class_='sortable alternating')

            # For each row in gene table...
            for row in rows.select('tr')[1:]:
                ##print(row.select('td')[0].text)
                # Retrieve the gene
                gene = row.select('td')[0].text
                ##print([met['id'],pathway,gene])
                # Write out parent metabolism, sub-pathway, and gene to csv
                writer.writerow([met['id'],pathway,gene])

