'''
Created on Apr 22, 2016

@author: Mickey
'''

def processData( filename ):
    '''
    Read data about movies and raters and return the info in a list of
    movies being rated and a dictionary of raters and their ratings
    '''
    #get the list of movies
    itemset = set()
    raterset = set()
    dictratings = {}
    f = open(filename)
    for line in f:
        line = line.strip().split()
        rating = int(line[0])
        rater = line[1]
        movie = line[2:]
        movie = " ".join(movie)
        itemset.add(movie)
        raterset.add(rater)
            
    itemlist = list(itemset)
    
    #make the dict of raters and their ratings
    #initialize values as list of zeroes
    raterlist = list(raterset)
    for name in raterlist:
        if name not in dictratings:
            dictratings[name] = [0]*len(itemlist)
    
    f = open(filename)
    for line in f:
        line = line.strip().split()
        rating = int(line[0])
        rater = line[1]
        movie = line[2:]
        movie = " ".join(movie)
        x = itemlist.index(movie)
        dictratings[rater][x] = rating

    return itemlist, dictratings
    

#print processData("ratingsmovies.txt")
        
        
        
        