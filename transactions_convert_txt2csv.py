import csv
from dateutil.parser import parse

def process_transaction_txt():
    filename = 'transaction.txt'
    header = 'DATE,DESCRIPTION,TYPE,AMOUNT'.split(',')
    outcsv = []
    outcsv.append(header)
    
    with open(filename) as fh:
         csvr = csv.reader(fh)
         for row in csvr:
             rowlist = row[0].split(' ')
             rowlist = [x for x in rowlist if x]
             if is_date(rowlist[0]) and \
                is_number(rowlist[-1]):
                transactonName = ' '.join(rowlist[1:-2])
                transactionDate = rowlist[0]
                trasactionAmount = rowlist[-1]
                transactionType = rowlist[-2]
                if transactionType in 'Credit':
                   trasactionAmount = '-{}'.format(trasactionAmount)
                if '.' in trasactionAmount:
                   entry = [transactionDate, transactonName, transactionType, trasactionAmount] 
                   outcsv.append(entry)
    return(outcsv)
    

def is_date(string):
    try: 
        parse(string)
        return True
    except ValueError:
        return False

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def write_to_csv(outfile, outcsv, mode='w'):
    with open(outfile, mode) as fh:
         csvw = csv.writer(fh)
         csvw.writerows(outcsv)
    print('Output file: {}'.format(outfile))

outcsv = process_transaction_txt()
outfile = 'transaction.csv'
write_to_csv(outfile, outcsv)
