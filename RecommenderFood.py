'''
Created on Apr 22, 2016

@author: Mickey
'''
from Recommender import averages
from Recommender import similarities
from Recommender import recommended
from ReadFood import processData

if __name__ == '__main__':
    #process files and print data on average food ratings in file
    foodfile = "foods.txt"
    fooditems, fooddict = processData(foodfile)
    resultavg = averages(fooditems,fooddict)
    
    print "Restaurants and their average ratings"
    print "-------------------------------------"
    for tup in resultavg:
        print tup
    print
    
    #get similar ratings for specified people, print them     
    person1 = "Tracy"
    resultsim = similarities(person1, fooddict)
    person2 = "George"
    resultsim2 = similarities(person2, fooddict)
    
    print "Ratings similar to Tracy"
    print "-------------------------------------"
    for thing in resultsim:
        print thing
    print
    
    print "Ratings similar to George"
    print "-------------------------------------"
    for item in resultsim2:
        print item
    print
    
    #get recommendations for specified people based on top 3 most similar raters
    #print 3 of them
    resultrec = recommended(resultsim, fooditems, fooddict,3)
    resultrec2 = recommended(resultsim2, fooditems, fooddict,3)
    print "Recommendations for Tracy with 3 most similar raters"
    print "----------------------------------------------------"
    for item in resultrec[:3]:
        print item
    print 
    print "Recommendations for George with 3 most similar raters"
    print "----------------------------------------------------"
    for item in resultrec2[:3]:
        print item
    print
    
    
