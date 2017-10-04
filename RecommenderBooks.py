'''
Created on Apr 22, 2016

@author: Mickey
'''
from Recommender import averages
from Recommender import similarities
from Recommender import recommended
from ReadBooks import processData

if __name__ == '__main__':
    
    #process files and print data on top 20 average book ratings in file
    bookauthorfile = "booksauthors.txt"
    bookratingfile = "ratingsbooks.txt"
    bookitems, bookdict = processData(bookauthorfile, bookratingfile)
    resultavg = averages(bookitems,bookdict)
    resultavgslice = resultavg[:20]
    
    print "Books and their average ratings"
    print "-------------------------------------"
    for tup in resultavgslice:
        print tup
    print
     
    #get top 20 similar ratings for specified people, print them   
    person1 = "Reuven"
    resultsim = similarities(person1, bookdict)
    person2 = "Priscilla"
    resultsim2 = similarities(person2, bookdict)
    person3 = "Cust6"
    resultsim3 = similarities(person3, bookdict)
    
    print "Ratings similar to Reuven"
    print "-------------------------------------"
    for thing in resultsim[:20]:
        print thing
    print
    
    print "Ratings similar to Priscilla"
    print "-------------------------------------"
    for item in resultsim2[:20]:
        print item
    print
    
    print "Ratings similar to Cust6"
    print "-------------------------------------"
    for item in resultsim3[:20]:
        print item
    print
    
    #get recommendations for specified people based on top 20 most similar raters
    #print 10 of them
    resultrec = recommended(resultsim, bookitems, bookdict,20)
    resultrec2 = recommended(resultsim2, bookitems, bookdict,20)
    resultrec3 = recommended(resultsim3, bookitems, bookdict,20)
    print "Recommendations for Reuven with 20 most similar raters"
    print "----------------------------------------------------"
    for item in resultrec[:10]:
        print item
    print 
    print "Recommendations for Priscilla with 20 most similar raters"
    print "----------------------------------------------------"
    for item in resultrec2[:10]:
        print item
    print
    print "Recommendations for Cust6 with 20 most similar raters"
    print "----------------------------------------------------"
    for item in resultrec3[:10]:
        print item