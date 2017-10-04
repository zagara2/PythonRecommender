'''
Created on Apr 22, 2016

@author: Mickey
'''
def processData( filename):
    '''
    Read data about food and raters and return the 
    information in a list of restaurants being rated and dictionary
    of raters and their ratings of the restaurants.
    '''
    
    #get the list of unique restaurants
    f = open(filename)
    restaurantset = set()
    raterset = set()
    dictratings = {}
    for line in f:
        if "," in line:
            linesplit = line.split(",")
            for x in range(0, len(linesplit), 2):
                restaurantset.add(linesplit[x])
        else:
            linestrip = line.strip()
            raterset.add(linestrip)
            
    itemlist = list(restaurantset)
    
    #make the dict of raters and their ratings of the restaurants
    #initialize keys as list of 0s 
    numrest = len(itemlist)
    for name in raterset:
        dictratings[name] = [0] * numrest
        
    namelist = []
    ratinglist = []
    p = open(filename)
    for line in p:
        if "," not in line:
            namelist.append(line.strip())
        else:
            ratinglist.append(line.strip())

    combolist = []
    for x in range(0, len(namelist)):
        full = namelist[x] + "," + ratinglist[x]
        combolist.append(full)

    for thing in combolist:
        mysplit = thing.split(",")
        name = mysplit[0]
        restof = mysplit[1:]
        for x in range(0, len(restof), 2):
            rname = restof[x]
            rate = int(restof[x+1])
            myindex = itemlist.index(rname)
            dictratings[name][myindex] += rate
    return itemlist, dictratings
        
        
#print processData("foods.txt")
    
        

    