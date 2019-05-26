import csv
import argparse

class analyser:

    def __init__(self):
        pass

    def cli(self):

        file = 'Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv'
        
        parser = argparse.ArgumentParser()
        parser.add_argument('mode', help='mode select: median, percentage, best, regression, comparison')
        parser.add_argument('-y', '--year')
        parser.add_argument('-v', '--voivodeship')
        parser.add_argument('-v2', '--voivodeship2')
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-m', '--male', action='store_true')
        group.add_argument('-f', '--female', action='store_true')
        args = parser.parse_args()
        
        mode = args.mode
        mode = mode.replace('mode=','')
        year = args.year
        voivodeship = args.voivodeship
        voivodeship2 = args.voivodeship2
        voivodeshipcomparison = [voivodeship, voivodeship2]
        voivodeshiplist = [
            'Dolnośląskie',
            'Kujawsko-pomorskie',
            'Lubelskie',
            'Lubuskie',
            'Łódzkie',
            'Małopolskie',
            'Mazowieckie',
            'Opolskie',
            'Podkarpackie',
            'Podlaskie',
            'Pomorskie',
            'Śląskie',
            'Świętokrzyskie',
            'Warmińsko-Mazurskie',
            'Wielkopolskie',
            'Zachodniopomorskie'
        ]
        yearslist = [ '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
        modeslist = [ 'median', 'percentage', 'best', 'regression', 'comparison']
        male = args.male
        female = args.female
        result=0
        highestratio=0
        highestratioindex=0
        tooktest=[0]*16
        tooktestallyears=[[0] * 16 for i in range(9)]
        passedtest=[0]*16
        passedtestallyears=[[0] * 16 for i in range(9)]
        percentages=[0]*16
        percentagesallyears=[[0] * 16 for i in range(9)]
        gender = ''
        genderstring = ' (males and females)'
        if male:
            genderstring=' (males)'
            gender='mężczyźni'
        if female:
            genderstring=' (females)'
            gender='kobiety'
        redFlags = None

        ########################
        # arguments validation #
        ########################
        
        if mode not in modeslist:
            print("Select a valid mode")
            redFlags = 1

        if voivodeship != None:
            if mode == 'best' or mode == 'regression':
                print("You can't select a voivodeship in this mode")
                redFlags = 1

        if voivodeship2 != None:
            if mode != 'comparison':
                print("You can't select second voivodeship in this mode!")
                redFlags = 1

        if year != None:
            if mode != 'median' and mode != 'best':
                print("You can't select a year in this mode")
                redFlags = 1

        if mode == 'median' or mode == 'best':
            if year not in yearslist :
                print("The data is for years 2010-2018. Enter a valid year")
                redFlags = 1
        
        if voivodeship not in voivodeshiplist:
            if mode in modeslist and mode != 'best' and mode != 'regression':
                print("Select a valid voivodeship")
                redFlags = 1
        
        if voivodeship2 not in voivodeshiplist:
            if mode == 'comparison':
                print("Select a valid second voivodeship")
                redFlags = 1            


        ########################
        #      modes logic     #
        ########################

        if redFlags == None: 
            # 1
            if mode == 'median':
                with open(file, newline='') as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=';')
                    for row in csvreader:
                        if male or female:
                            if voivodeship == row[0] and gender == row[2] and year >= row[3] and 'przystąpiło' == row[1]:
                                result+=int(row[4])
                        else:
                            if voivodeship == row[0] and year >= row[3] and 'przystąpiło' == row[1]:
                                result+=int(row[4])
                print('Median for years 2010-', year, ', for ', voivodeship, ' voivodeship is ', round(result/(int(year)-2009)), genderstring, sep='')

            # 2
            if mode == 'percentage':
                with open(file, newline='') as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=';')
                    for row in csvreader:
                        if male or female:
                            year=2010
                            for x in range(9):
                                if voivodeship == row[0] and gender == row[2] and year == int(row[3]) and 'przystąpiło' == row[1]:
                                    tooktest[x] = int(row[4])
                                if voivodeship == row[0] and gender == row[2] and year == int(row[3]) and 'zdało' == row[1]:
                                    passedtest[x] = int(row[4])
                                year+=1
                        else:
                            year=2010
                            for x in range(9):
                                if voivodeship == row[0] and year == int(row[3]) and 'przystąpiło' == row[1]:
                                    tooktest[x] += int(row[4])
                                if voivodeship == row[0] and year == int(row[3]) and 'zdało' == row[1]:
                                    passedtest[x] += int(row[4])
                                year+=1
                    for x in range(9): 
                        percentages[x] = round((passedtest[x] / tooktest[x])*100,1)
                print('Passing percentage', genderstring, ' for ', voivodeship, ' is as follows:', sep='')
                year = 2010
                for x in range(9):
                    print(year, ' - ', percentages[x], '%', sep='')
                    year+=1

            # 3
            if mode == 'best':
                with open(file, newline='') as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=';')
                    for row in csvreader:
                        if male or female:
                            for x, v in enumerate(voivodeshiplist):
                                if v == row[0] and gender == row[2] and year == row[3] and 'przystąpiło' == row[1]:
                                    tooktest[x] = int(row[4])
                                if v == row[0] and gender == row[2] and year == row[3] and 'zdało' == row[1]:
                                    passedtest[x] = int(row[4])
                        else:
                            for x, v in enumerate(voivodeshiplist):
                                if v == row[0] and year == row[3] and 'przystąpiło' == row[1]:
                                    tooktest[x] += int(row[4])
                                if v == row[0] and year == row[3] and 'zdało' == row[1]:
                                    passedtest[x] += int(row[4])
                    for x in range(16): 
                        percentages[x] = round((passedtest[x] / tooktest[x])*100, 1)
                        if highestratio < percentages[x]:
                            highestratio = percentages[x]
                            highestratioindex = x
                print('In year ', year, ' ', voivodeshiplist[highestratioindex], ' got the highest passing ratio (', highestratio, '%)' ,  genderstring, sep='')   

            # 4
            if mode == 'regression':
                with open(file, newline='') as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=';')
                    for row in csvreader:
                        if male or female:
                            year = 2010
                            for x in range(9):
                                for y, v in enumerate(voivodeshiplist):
                                        if v == row[0] and gender == row[2] and year == int(row[3]) and 'przystąpiło' == row[1]:
                                            tooktestallyears[x][y] = int(row[4])
                                        if v == row[0] and gender == row[2] and year == int(row[3]) and 'zdało' == row[1]:
                                            passedtestallyears[x][y] = int(row[4])
                                year+=1

                        else:
                            year=2010
                            for x in range(9):
                                for y, v in enumerate(voivodeshiplist):
                                    if v == row[0] and year == int(row[3]) and 'przystąpiło' == row[1]:
                                        tooktestallyears[x][y] += int(row[4])
                                    if v == row[0] and year == int(row[3]) and 'zdało' == row[1]:
                                        passedtestallyears[x][y] += int(row[4])
                                year+=1
                for x in range(9):
                    for y, v in enumerate(voivodeshiplist):
                        percentagesallyears[x][y] = (passedtestallyears[x][y] / tooktestallyears[x][y])*100
                        if x > 0:
                            if percentagesallyears[x][y] < percentagesallyears[x-1][y]:
                                print('Voivodeship ', voivodeshiplist[y], ' got a lower score (', round(percentagesallyears[x][y], 1),
                                    '%) in year ', 2010+x, ' than in year ', 2009+x, ' (', round(percentagesallyears[x-1][y],1), '%)', genderstring, sep='')
                                
            # 5
            if mode == 'comparison':
                with open(file, newline='') as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=';')
                    for row in csvreader:
                        if male or female:
                            year = 2010
                            for x in range(9):                    
                                for y, v in enumerate(voivodeshipcomparison):
                                    if v == row[0] and gender == row[2] and year == int(row[3]) and 'przystąpiło' == row[1]:
                                        tooktestallyears[x][y] = int(row[4])
                                    if v == row[0] and gender == row[2] and year == int(row[3]) and 'zdało' == row[1]:
                                        passedtestallyears[x][y] = int(row[4])
                                year+=1
                        else:
                            year=2010
                            for x in range(9):
                                for y, v in enumerate(voivodeshipcomparison):
                                    if v == row[0] and year == int(row[3]) and 'przystąpiło' == row[1]:
                                        tooktestallyears[x][y] += int(row[4])
                                    if v == row[0] and year == int(row[3]) and 'zdało' == row[1]:
                                        passedtestallyears[x][y] += int(row[4])
                                year+=1

                print('Comparing passing percentages for ', voivodeship, ' and ', voivodeship2, sep='')
                for x in range(9):
                    percentagesallyears[x][0] = (passedtestallyears[x][0] / tooktestallyears[x][0])*100
                    percentagesallyears[x][1] = (passedtestallyears[x][1] / tooktestallyears[x][1])*100
                    if percentagesallyears[x][0] > percentagesallyears[x][1]:
                        print(2010+x, ' ', voivodeship, ' wins with score ', round(percentagesallyears[x][0],1), ', ', voivodeship2, ' got ',
                            round(percentagesallyears[x][1],1), genderstring, sep='')
                    elif percentagesallyears[x][0] < percentagesallyears[x][1]:
                        print(2010+x, ' ', voivodeship2, ' wins with score ', round(percentagesallyears[x][1],1), ', ', voivodeship, ' got ',
                            round(percentagesallyears[x][0],1), genderstring, sep='')
            
    if __name__ == '__main__':
        cli('')
