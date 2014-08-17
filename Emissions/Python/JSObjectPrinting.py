import csv

def getKey(name):
    #this got out of hand fast. really need to clean this up
    return name.replace(' ', '').replace('&','').replace(',','').replace('.','').replace('-','').replace("'","").replace(")","").replace("(","")

def remDup(fname):

    infile = open(fname,"r")
    outfile = open(fname[:-4]+'2'+fname[-4:], "w", newline='', encoding='utf-8')

    myreader = csv.reader(infile, delimiter = "!")
    mywriter = csv.writer(outfile, delimiter = "!")

    prevRow = []
    for row in myreader:
        if row != prevRow:
            mywriter.writerow(row)
        else:
            print(row)
        prevRow = row
        

    infile.close()
    outfile.close()



def fillPopData():

    infile = open("C:/daryn/data/Emissions/popPrinting2.dat","r")
    outfile = open("C:/Users/darynr/Dropbox/web/emissions.data.js", "a", newline='', encoding='utf-8')

    myreader = csv.reader(infile, delimiter = "!")
    

    for row in myreader:
        break

    prevc = "blahblahblah"
    prevm = "etcetcetc"
    firstCountry = True
    firstm = True

    prevy = 0

    outfile.write('\n\n');
    for row in myreader:

        meas = row[2]

        if meas != prevm:
            if firstm == False:
                outfile.write(']}};\n\n')
            elif firstm == True:
                firstm = False
            outfile.write('var '+getKey(meas)+' = {')
            prevm = meas
            firstCountry = True


        country = row[0]

        if country==prevc:
           year = int(row[1])
           if year != prevy+1:
               print(country+' '+str(year)+' '+meas+'\n')
           prevy = year
           outfile.write(',')
           
        elif country != prevc:
            key = getKey(country)
            prevc = country
            prevy = int(row[1])
            if firstCountry == False:
                outfile.write(']},\n')
                
            elif firstCountry == True:
                firstCountry = False
            outfile.write(key+': { base: '+row[1]+', data : [')
        if meas == "Population":
            outfile.write(row[3])
        else:    
            outfile.write('"'+row[3]+'"')

    outfile.write(']}};\n\n')
    outfile.close()
    infile.close()


def fillGasData():

    infile = open("C:/daryn/data/Emissions/GHGsummaryData2.dat","r")
    outfile = open("C:/Users/darynr/Dropbox/web/emissions.data.js", "w", newline='', encoding='utf-8')

    myreader = csv.reader(infile, delimiter = "!")
    

    for row in myreader:
        break

    prevc = "blahblahblah"
    prevg = "etcetcetc"
    firstCountry = True
    firstGas = True

    prevy = 0
    
    for row in myreader:

        gas = row[4]

        if gas != prevg:
            if firstGas == False:
                outfile.write(']}};\n\n')
            elif firstGas == True:
                firstGas = False
            outfile.write('var '+getKey(gas)+' = {')
            prevg = gas
            firstCountry = True


        country = row[0]

        if country==prevc:
           year = int(row[1])
           if year != prevy+1:
               print(country+' '+str(year)+' '+gas+'\n')
           prevy = year
           outfile.write(',')
           
        elif country != prevc:
            key = getKey(country)
            prevc = country
            prevy = int(row[1])
            if firstCountry == False:
                outfile.write(']},\n')
                
            elif firstCountry == True:
                firstCountry = False
            outfile.write(key+': { base: '+row[1]+', data : [')
            #outfile.write('{'+'name: "'+country+'", id: "'+key+', base: '+row[1]+', data : [')
        outfile.write('['+row[5]+','+row[6]+']')

    outfile.write(']}};\n\n')
    outfile.close()
    infile.close()
            














