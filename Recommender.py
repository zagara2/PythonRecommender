'''
Created on Apr 22, 2016

@author: Mickey
'''

def averages(itemlist,dictratings):
    '''
    For each item in (books, movies or restaurants) computes its 
    average rating. Return list of tuples where each tuple includes 
    an item being rated and the average rating for all those who've 
    rated the item. Sorted so that the highest rated item is first
    '''
    ratedict = {}
    ratelists = [v for (k, v) in dictratings.items()] #list of lists of ratings
    for item in itemlist:
        ratedict[item] = []
    for x in range(0, len(itemlist)):
        for lst in ratelists:
            ratedict[itemlist[x]].append(float(lst[x]))#get corresponding rating list for appropriate item
    avgdict = {}
    #compute averages of nonzero ratings/filter out 0s
    for (k, v) in ratedict.items():
        nozero = [x for x in v if x != 0.0]
        if nozero != []:
            avgdict[k] = sum(nozero)/len(nozero)
        else:
            avgdict[k] = 0.0
    #sort final list so highest first
    averageList = sorted((v, k) for (k,v) in avgdict.items())
    averageList.reverse()
    averageList = [(k, v) for (v, k) in averageList]
    return averageList
    

#print averages(['WaDuke', 'DivinityCafe', 'GreatHall', 'ABP', 'Panda', 'Loop', 'Alpine'], {'Will': [0, 0, 0, 1, 5, 1, 0], 'Samantha': [-3, 3, 0, 3, 3, 5, 1], 'Tracy': [-3, 3, 0, 5, 3, 3, -3], 'Xiaobai': [-1, 5, 0, 1, -1, 0, 0], 'George': [5, 5, -3, 1, 1, -3, 0]})
#print averages(['WaDuke', 'DivinityCafe', 'GreatHall'], {'Will': [0, 0, 0], 'Samantha': [-3, 3, 0]})
    
def similarities(name, dictratings):
    '''
    for each rater, computes how similar they are to other 
    raters based on ratings for books, movies or restaurants.
    returns a list of two-tuples where each tuple contains a rater-name (string) and a similarity-index (float). 
    The list is sorted with the most-similar rater first.
    '''
    target = dictratings[name] #rating list for specified person
    retlist = []
    #make list of rater names and corresponding similarity scores
    for (k, v) in dictratings.items():
        if k != name: #person not evaluated compared to self
            dotprod = sum([i*j for (i, j) in zip(target, v)])
            mytup = (k, float(dotprod))
            retlist.append(mytup)
    #sort final list so highest first
    similarList = sorted([(y, x) for (x, y) in retlist])
    similarList.reverse()
    similarList = [(x, y) for (y, x) in similarList]
    return similarList
    
#print similarities("Tracy", {'Will': [0, 0, 0, 1, 5, 1, 0], 'Samantha': [-3, 3, 0, 3, 3, 5, 1], 'Tracy': [-3, 3, 0, 5, 3, 3, -3], 'Xiaobai': [-1, 5, 0, 1, -1, 0, 0], 'George': [5, 5, -3, 1, 1, -3, 0]})
    
def recommended(simlist,itemlist,dictratings,n):
    '''
    given a rater, get recommendations for 
    books, movies or restaurants based on raters who are similar.
    Returns list sorted from most-recommended to least recommended and is a list of 
    tuples where the first element is the name of an item and the second 
    element is the score for that item.
    '''
    #get simlist in order
    simlist = sorted([(y,x) for (x,y) in simlist])
    simlist.reverse()
    simlist = simlist[:n]
    simlist = [(y,x) for (x, y) in simlist]

    #make dict of list of weighted ratings corresponding to each item
    sumdict = {}    
    for thing in itemlist:
        sumdict[thing] = []
    for item in simlist:
        name = item[0]
        simrating = item[1]
        ratlist = dictratings[name]
        myproduct = [simrating*p for p in ratlist]
        for x in range(0, len(ratlist)):
            toberated = itemlist[x]
            weightedrating = myproduct[x]
            sumdict[toberated].append(weightedrating)
    
    #compute averages of nonzero ratings/filter out 0s
    avgdict = {}
    for (k, v) in sumdict.items():
        nozero = [x for x in v if x != 0]
        if nozero != []:
            avgdict[k] = sum(nozero)/len(nozero)
        else:
            avgdict[k] = 0.0
    
    #sort the list so highest is first
    mylist = sorted((v, k) for (k,v) in avgdict.items())
    mylist.reverse()
    mylist = [(k, v) for (v, k) in mylist]
    recommendList = mylist
    return recommendList

#print recommended([('Samantha', 54.0), ('Will', 23.0), ('Xiaobai', 20.0), ('George', -1.0)], ['WaDuke', 'DivinityCafe', 'GreatHall', 'ABP', 'Panda', 'Loop', 'Alpine'], {'Will': [0, 0, 0, 1, 5, 1, 0], 'Samantha': [-3, 3, 0, 3, 3, 5, 1], 'Tracy': [-3, 3, 0, 5, 3, 3, -3], 'Xiaobai': [-1, 5, 0, 1, -1, 0, 0], 'George': [5, 5, -3, 1, 1, -3, 0]}, 4)

        
    
    
    
    
    
    