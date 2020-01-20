import xlrd

path = "Foosball Game (Responses).xlsx"
inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)
# print(inputWorksheet.nrows)
# print(inputWorksheet.ncols)
# print(inputWorksheet.cell_value(1, 1))   #(x,y)

names = ('Akhtar', 'Arjun', 'Daniel', 'Dmytro', 'Fadi', 'Flavio', 'Frederik', 'Jaiden', 'John Vu', 'Marc Flores', 'Michael (Apple)', 'PK', 'Razel', 'Reem', 'Reggy Loisy', 'Ricardo', 'Shourya', 'Shray', 'Siraj', 'Tyler', 'Victor (Beats)', 'Vini', 'William', '')
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


last_three_games()
rankings()
print_rankstable()
print('')
print_standingstable()
printGames()