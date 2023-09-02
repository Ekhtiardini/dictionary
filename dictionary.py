import os
import csv

print('--------------------------------')
print('-----welcome to my dictunary----')
print('--------------------------------')

lan = dict()
menu = int(input ('1. Add 2.Edie 3.Delete 4.Search 5.Read 6.Save 7.Exit : ' ))

while (menu != 7):
    os.system('cls')
    print(lan)
    if menu == 1 :
        internalUp_key=input('your English word :')
        internalUp={internalUp_key:input('your Kurdish word :')}
        if (internalUp_key in lan.keys()):
            print('you shoud update this word  !!!')
        else:
            lan.update(internalUp)
            print('Success !!!')
    elif menu == 2 :
        lankey = input('your English word :')
        if (lankey in lan.keys()):
            lan[lankey] = input('your Kurdish word :')
            print('Success !!!')
    elif menu == 3 :
        lankey = input('your English word :')
        if (lankey in lan.keys()):
            del lan[lankey] 
            print('you deleted this word' + lankey + '   ')
    elif menu == 4 :
        lankey = input('your English word :')
        if (lankey in lan.keys()):
            input('Its :' + lan[lankey] + '! ')
        else:
            input('We dont have your word')
    elif menu == 5 :
        with open('Dic.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                lan.update({row[0]:row[1]})
            
            input('Succes you load all dict')
    elif menu == 6 :
        
        with open('Dic.csv', 'w',newline='') as f:
            writer = csv.writer(f)
            for row in lan:
                writer.writerow([row,lan[row]])
            
            input('Succes you save all dict')
    
    
    menu = int(input ('1. Add 2.Edie 3.Delete 4.Search 5.Read 6.Save 7.Exit : ' ))