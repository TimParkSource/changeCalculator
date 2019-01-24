from decimal import *

denominations = [Decimal('100'),Decimal('50'),Decimal('20'),Decimal('10'),Decimal('5'),Decimal('1'),Decimal('.25'),Decimal('.10'),Decimal('.05'),Decimal('.01')]
changeDenominations = [0,0,0,0,0,0,0,0,0,0]

change = input('Enter change amount: ')
#change = 288.44
change = Decimal(change)

def greedy(fnum):
    if fnum != Decimal('0'):
        # greedy algorithm
        for x in range(0,10):
            i = 0
            while fnum >= denominations[x]:
                fnum -= denominations[x]
                i += 1
                changeDenominations[x] = i
                #print(str(denominations[x]) + ':' + str(changeDenominations[x]))

greedy(change)

dash = '-' * 12
print(dash)
print(' {:>2s}  {:<4s}'.format('Amt','Den',))
print(dash)

for x in range(0,10):
    if changeDenominations[x] != 0:
        print(' {:>2s}   ${:<4s}'.format(str(changeDenominations[x]), str(denominations[x])))
        
