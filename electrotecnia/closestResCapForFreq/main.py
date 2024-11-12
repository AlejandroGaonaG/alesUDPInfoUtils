import math
import itertools

def freqResult(resistance, capacitancy):
    frequency = 1/(2 * math.pi * resistance * capacitancy)
    return frequency

def readToList(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

resistanceStringList = readToList('resist.txt')
condensStringList = readToList('condens.txt')
resistanceList = []
condensList = []

for resString in resistanceStringList:
    if 'K' in resString:
        res = (float(resString.replace('K', ''))) * 1000
    elif 'M' in resString:
        res = (float(resString.replace('M', ''))) * 1000000
    else:
        res = float(resString)

    resistanceList.append(res)

for condensString in condensStringList:
    if 'u' in condensString:
        condens = (float(condensString.replace('u', ''))) * pow(10, -6)
    elif 'n' in condensString:
        condens = (float(condensString.replace('n', ''))) * pow(10, -9)
    elif 'p' in condensString:
        condens = (float(condensString.replace('p', ''))) * pow(10, -12)
    else:
        condens = float(condensString)

    condensList.append(condens)

def closestResCondens(resistances, condensators, targetFreq):
    pairs = list(itertools.product(resistances, condensators))

    freqs = [(a, b, freqResult(a, b)) for a, b in pairs]
    freqs.sort(key=lambda x: abs(x[2] - targetFreq))

    topFive = [(pair[0], pair[1]) for pair in freqs[:5]]

    return topFive

print('Frecuencia deseada (en Hz): ')
frequencyToGet = input()
freqConsUse = closestResCondens(resistanceList, condensList, float(frequencyToGet))
print('Ordenado de forma (Resistencia, Capacitancia), top 5 del menos al más cercano\n')
print(freqConsUse)