import xlrd
path = "Foosball Game (Responses).xlsx"
inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)
# print(inputWorksheet.nrows)
# print(inputWorksheet.ncols)
# print(inputWorksheet.cell_value(1, 1))   #(x,y)
names = ('Abdullah', 'Akhtar', 'Arjun', 'Daniel', 'Dmytro', 'Fadi', 'Flavio', 'Frederik', 'Jaiden','John C', 'John Vu', 'Marc Flores', 'Michael (Apple)', 'Nathan', 'Nav', 'PK', 'Razel', 'Reem', 'Reggy Loisy', 'Ricardo', 'Shourya', 'Shray', 'Siraj', 'Tome', 'Tyler', 'Victor (Beats)', 'Vini', 'William', '')
wins = [0 for i in range(len(names))]
loss = [0 for j in range(len(names))]
total_games_played = [0 for k in range(len(names))]
winloss = [0 for l in range(len(names))]
winpercent = [0 for i in range(len(names))]
points = [0 for i in range(len(names))]
losspoints = [0 for i in range(len(names))]
ranks = [0 for i in range(len(names))]


def game_results(player1, player2, points1, points2):
    temp = 0
    points1 = int(points1)
    points2 = int(points2)
    if points1 > points2:
        winindex = names.index(player1)
        lossindex = names.index(player2)
    else:
        winindex = names.index(player2)
        lossindex = names.index(player1)
    temp = wins[winindex]+1
    wins.pop(winindex)
    wins.insert(winindex, temp)
    temp = loss[lossindex] + 1
    loss.pop(lossindex)
    loss.insert(lossindex, temp)
    temp = total_games_played[winindex]+1
    total_games_played.pop(winindex)
    total_games_played.insert(winindex, temp)
    temp = total_games_played[lossindex]+1
    total_games_played.pop(lossindex)
    total_games_played.insert(lossindex, temp)


def rankings():
    newpoints = points.copy()
    biggest = 0
    maxindex = 0
    for i in range(1, len(points)):
        biggest = max(newpoints)
        for j in range(len(newpoints)):
            if newpoints[j] == biggest:
                maxindex = j

        ranks.pop(maxindex)
        ranks.insert(maxindex, i)
        #print(ranks)
        newpoints.pop(maxindex)
        newpoints.insert(maxindex, 0)
        #print(newpoints)

# rankings()
# print(ranks)


def last_three_games():
    totallines = inputWorksheet.nrows
    for j in range(len(names)):
        for k in range(len(names)):
            count = 0
            gameresult = []
            for i in range(1, totallines):
                if count != 3 and inputWorksheet.cell_value(totallines - i, 1) == names[j] and inputWorksheet.cell_value(totallines - i, 2) == names[k]:
                    count += 1
                    if inputWorksheet.cell_value(totallines - i, 3) > inputWorksheet.cell_value(totallines - i, 4):
                        gameresult.append("W")
                    else:
                        gameresult.append("L")
                if count != 3 and inputWorksheet.cell_value(totallines - i, 2) == names[j] and inputWorksheet.cell_value(totallines - i, 1) == names[k]:
                    count += 1
                    if inputWorksheet.cell_value(totallines - i, 4) > inputWorksheet.cell_value(totallines - i, 3):
                        gameresult.append("W")
                    else:
                        gameresult.append("L")
            if gameresult.count("W") >= 2:
                temp = points[j] + 1
                points.pop(j)
                points.insert(j, temp)
            elif gameresult.count("L") >= 2:
                temp = losspoints[j] + 1
                losspoints.pop(j)
                losspoints.insert(j,temp)


def print_rankstable():
    newlist = []
    for i in range(1, len(names)):
        for j in range(len(names) - 1):
            if ranks[j] == i:
                newlist.append([names[j], ranks[j], points[j], losspoints[j]])


    print("Ranking Table")
    print(": Name             : Rank   : Record W-L :")
    print("---------------------------------------")

    for item in newlist:
        print(':', item[0], " "*(15-len(item[0])), ":", item[1], " "*(5-len(str(item[1]))), ":", item[2],'-',item[3], " "*(9-(len(str(item[2])))-len(str(item[3]))-3), ":")


def print_standingstable():
    nestedlist = []
    for i in range(len(names)-1):
        nestedlist.append([names[i], ranks[i], wins[i], loss[i], winloss[i], winpercent[i],total_games_played[i], points[i], losspoints[i]])


    print("Current Stats")
    print(': Name             : Rank   : Wins   : Loss   : Win/Loss Ratio   : Win Percent    : Games Played   : '
          'Record W-L :')
    print('---------------------------------------------------------------------------------------------------------------')

    for item in nestedlist:
        print(':', item[0], " "*(15-len(item[0])), ":", item[1], " "*(5-len(str(item[1]))), ":", item[2], " "*(5-len(str(item[2]))), ":", item[3], " "*(5-len(str(item[3]))), ":", item[4], " "*(15-len(str(item[4]))), ":", str(item[5])+'%', " "*(12-len(str(item[5]))), ":", item[6], " "*(13-len(str(item[6]))), ":", item[7],'-',item[8], ' '*(9-(len(str(item[7])))-(len(str(item[8])))-3), ':')


def printGames():
    print('')
    day = input('Enter the Date in format YYYY-MM-DD ')
    list = []
    print('')
    print(day, "Games")
    print(": Name             : Opponent         : Score    :")
    print("--------------------------------------------------")
    
    for i in range(1, inputWorksheet.nrows):
        if str(xlrd.xldate.xldate_as_datetime(inputWorksheet.cell_value(i, 0),inputWorkbook.datemode))[:10] == day:
            list.append([inputWorksheet.cell_value(i,1),inputWorksheet.cell_value(i,2),int(inputWorksheet.cell_value(i,3)),int(inputWorksheet.cell_value(i,4))])
            
    for item in list:
        print(':', item[0], " "*(15-len(item[0])), ":", item[1], " "*(15-len(str(item[1]))), ":", item[2], "-", item[3], " "*(7-3-(len(str(item[2])))-len(str(item[3]))),':')


for x in range(1, inputWorksheet.nrows):
    l = []
    for y in range(1, 5):
        l.append(inputWorksheet.cell_value(x, y))
    game_results(l[0], l[1], l[2], l[3])
    # print(l[0], l[1], l[2], l[3])
    l = []


for i in range(len(names)):
    if loss[i] != 0:
        wl = round(wins[i] / loss[i],2)
    else:
        wl = wins[i]
    if total_games_played[i] != 0:
        wp = round((wins[i] / total_games_played[i]) * 100,2)
    else:
        wp = 0
    winloss.pop(i)
    winloss.insert(i, wl)
    winpercent.pop(i)
    winpercent.insert(i, wp)


def betting():
    p1found, p2found = False, False
    while not p1found:
        p1 = str(input("Enter the name of the first player: "))
        for i in range(len(names)):
            if names[i].upper() == p1.upper():
                p1found = True
        if not p1found:
            print("PLAYER IS NOT IN TABLE. TRY AGAIN")
    while not p2found:
        p2 = str(input("Enter the name of the second player: "))
        for i in range(len(names)):
            if names[i].upper() == p2.upper():
                p2found = True
        if not p2found:
            print("PLAYER IS NOT IN TABLE. TRY AGAIN")

    p1 = p1[0].upper() + p1[1:]
    p2 = p2[0].upper() + p2[1:]
    totallines = inputWorksheet.nrows
    wins = 0
    totalgames = 0
    for i in range(1, totallines):
        if totalgames < 10 and inputWorksheet.cell_value(totallines - i, 1).upper() == p1.upper() and inputWorksheet.cell_value(
                totallines - i, 2).upper() == p2.upper():
            if inputWorksheet.cell_value(totallines - i, 3) > inputWorksheet.cell_value(totallines - i, 4):
                wins += 1
                totalgames += 1
            else:
                totalgames += 1
        if totalgames < 10 and inputWorksheet.cell_value(totallines - i, 2).upper() == p1.upper() and inputWorksheet.cell_value(
                totallines - i, 1).upper() == p2.upper():
            if inputWorksheet.cell_value(totallines - i, 4) > inputWorksheet.cell_value(totallines - i, 3):
                wins += 1
                totalgames += 1
            else:
                totalgames += 1
    oddsp1 = round(10 * (wins/totalgames), 0)
    oddsp2 = 10 - oddsp1

    if oddsp1 == 10:
        oddsp1 = 9
        oddsp2 = 1
    elif oddsp2 == 10:
        oddsp2 = 9
        oddsp1 = 1

    unit1 = oddsp1
    unit2 = oddsp2

    bets =[]
    templist = []
    temp = 0
    choice = 0
    totalunits = 0
    p1pot = 0
    p2pot = 0
    quit = False
    while not quit:
        print('')
        print('')
        print("THE UNIT PRICE for ", p1.upper(), ' is $'+ str(unit1), ''*10, "THE UNIT PRICE for ", p2.upper(), ' is $'+ str(unit2))
        print("THE ODDS FOR ", p1.upper(), ' VS ', p2.upper(), 'is', oddsp1, 'to', oddsp2)
        if len(bets)>0:
            print("The winnings for ", p1.upper(), ' are $'+ str(round((p2pot - (p2pot * 0.05))/totalunits, 2)), ' '* 5, " The winnings for ", p2.upper(), ' are $'+ str(round((p1pot - (p1pot * 0.05))/totalunits, 2)))
        else:
            temp = int(input('IS BOOKIE SATISFIED WITH CURRENT ODDS? 1 FOR YES 111 FOR NO:'))
            while temp != 1 and temp != 111:
                print("INVALID INPUT")
                temp = int(input('1 or 111'))
            if temp == 1:
                pass
            elif temp == 111:
                while temp != "done":
                    print('')
                    print('ENTER THE ODDS FOR ', p1.upper()+'. MAKE SURE IT IS LESS THAN 10.')
                    temp = int(input('ODDS:'))
                    while temp > 10 or temp <= 0:
                        print("INVALID INPUT. ODDS MUST BE LESS THAN 10 AND GREATER THEN 0")
                        temp = int(input('ODDS:'))
                    print("Are you satisfied with THE ODDS FOR ", p1.upper(), ' VS ', p2.upper(), 'is', temp, 'to', 10-temp)
                    choice = int(input("IF YES ENTER 111 FOR YES OR 123 FOR NO"))
                    while choice != 111 and choice != 123:
                        print("INVALID INPUT")
                        choice = int(input('111 or 123'))
                    if choice == 111:
                        oddsp1 = temp
                        oddsp2 = 10 - oddsp1
                        unit1 = oddsp1
                        unit2 = oddsp2
                        break
                continue


        print("")
        print("ENTER WHO THE BET IS FOR: 1 FOR ", p1.upper(), ', OR 2 FOR ', p2.upper())
        temp = int(input('1 or 2'))
        while temp != 1 and temp != 2:
            print("INVALID INPUT")
            temp = int(input('1 or 2'))
        templist.append(temp)
        templist.append(str(input("NAME OF BETTOR: ")))
        templist.append(int(input("NUMBER OF UNITS: ")))
        totalunits += templist[2]
        if templist[0] == 1:
            print("PAY BOOKIE: ", round(templist[2] * unit1, 2))
            p1pot += templist[2] * unit1
        elif templist[0] == 2:
            print("PAY BOOKIE: ", round(templist[2] * unit2, 2))
            p2pot += templist[2] * unit2
        temp = str(input("HAS BOOKIE RECIEVED PAYMENT? (YES/NO)"))
        print("")
        print("GIVE BETTOR TICKET!!!")
        bets.append(templist)
        templist = []
        print('')
        temp = int(input("CONTINUE BETTING? ENTER 1 FOR YES OR 123 FOR NO: "))
        while temp != 1 and temp != 123:
            print("INVALID INPUT")
            temp = int(input("CONTINUE BETTING? ENTER 1 FOR YES OR 123 FOR NO: "))
        if temp == 123:
          quit = True
        print('-'*150)
    print("BETTING HAS ENDED")
    print('-' * 150)

    print("ENTER WHO WON THE ROUND: 1 FOR ", p1.upper(), ', OR 2 FOR ', p2.upper())
    temp = int(input('1 or 2'))
    while temp != 1 and temp != 2:
        print("INVALID INPUT")
        temp = int(input('1 or 2'))
    print("")
    if temp == 1:
        winnings = (p1pot - (p1pot * 0.05))/totalunits
        print('winnings == ', winnings)
        print('WINNERS: UNITS BOUGHT: DOLLARS WON')
        for i in range(len(bets)):
            if bets[i][0] == 1:
                print(bets[i][1].upper(), ' '*4, bets[i][2], ' '*4, '$', round((bets[i][2]*unit1) + (bets[i][2]*winnings),2))
    else:
        winnings = (p2pot - (p2pot * 0.05))/totalunits
        print('winnings == ', winnings)
        print('WINNERS: UNITS BOUGHT: DOLLARS WON')
        for i in range(len(bets)):
            if bets[i][0] == 2:
                print(bets[i][1].upper(), ' '*4, bets[i][2], ' '*4, '$', round((bets[i][2]*unit2) + (bets[i][2]*winnings), 2))


def menu():
    choice = 100
    last_three_games()
    rankings()
    while choice != 0:
        print("")
        print("")
        print("WELCOME TO THE BB FOOSBALL LEAGUE TABLE SYSTEM")
        print("1. PRINT TABLES")
        print("2. CHECK ALL THE GAMES FROM A SPECIFIC DATE")
        print("3. LAUNCH BETTING SYSTEM")
        print("0. TO EXIT THE CODE ENTER 0")

        choice = input("ENTER YOUR CHOICE: ")
        while not choice.isdigit():
            print("ERROR. CHOICE MUST BE AN INTEGER VALUE")
            choice = input("ENTER YOUR CHOICE: ")
        choice = int(choice)
        while choice > 3 or choice < 0:
            print("ERROR. CHOICE MUST BE BETWEEN 1 and 3")
            choice = int(input("ENTER YOUR CHOICE: "))
        if choice == 1:
            print_rankstable()
            print('')
            print_standingstable()
        elif choice == 2:
            printGames()
        elif choice == 3:
            betting()


menu()
