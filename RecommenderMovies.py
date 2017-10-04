'''
Created on Apr 22, 2016

@author: Mickey
'''
from Recommender import averages
from Recommender import similarities
from Recommender import recommended
from ReadMovies import processData

if __name__ == '__main__':
    #process files and print data on top 30 average movie ratings in file
    bookauthorfile = "booksauthors.txt"
    moviefile = "ratingsmovies.txt"
    movieitems, moviedict = processData(moviefile)
    resultavg = averages(movieitems,moviedict)
    
    print "Movies and their average ratings"
    print "-------------------------------------"
    for tup in resultavg[:30]:
        print tup
    print
        
    #get top 30 similar ratings for specified people, print them 
    person1 = "student1103"
    resultsim = similarities(person1, moviedict)
    person2 = "student1016"
    resultsim2 = similarities(person2, moviedict)
    person3 = "student1153"
    resultsim3 = similarities(person3, moviedict)
    
    print "Ratings similar to student1103"
    print "-------------------------------------"
    for thing in resultsim[:30]:
        print thing
    print
    
    print "Ratings similar to student1016"
    print "-------------------------------------"
    for item in resultsim2[:30]:
        print item
    print
    
    print "Ratings similar to student1153"
    print "-------------------------------------"
    for item in resultsim3[:30]:
        print item
    print
    
    #get recommendations for specified people based on top 50 most similar raters
    #print 20 of them
    resultrec = recommended(resultsim, movieitems, moviedict,50)
    resultrec2 = recommended(resultsim2, movieitems, moviedict,50)
    resultrec3 = recommended(resultsim3, movieitems, moviedict,50)
    print "Recommendations for student1103 with 50 most similar raters"
    print "----------------------------------------------------"
    for item in resultrec[:20]:
        print item
    print 
    print "Recommendations for student1016 with 50 most similar raters"
    print "----------------------------------------------------"
    for item in resultrec2[:20]:
        print item
    print
    print "Recommendations for student1153 with 50 most similar raters"
    print "----------------------------------------------------"
    for item in resultrec3[:20]:
        print item
    print
