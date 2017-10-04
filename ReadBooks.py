'''
Created on Apr 22, 2016

@author: Mickey
'''


def processData(booktitles, bookratings):
    '''
     Read data about books and raters and return the 
     information in a list of books being rated and a dictionary
     of raters and their ratings of the books.
    '''
    #combine the book and author names 
    f = open(booktitles)
    i = 0
    authors = []
    books = []
    itemlist = []
    for line in f:
        if i % 2 == 0:
            authors.append(line.strip())
        else:
            books.append(line.strip())
        i += 1
    for x in range(0, len(books)):
        new = books[x] + ","+ authors[x] 
        itemlist.append(new)
    
    #get dict of raters and thie ratings
    dictratings = {}
    p = open(bookratings)
    for line in p:
        line = line.split(":")
        name = line[0]
        restof = line[1:]
        dictratings[name]= [] #no repeated names so no need for "if name not in dictratings"
        for thing in restof:
            dictratings[name].append(int(thing))
    return itemlist, dictratings
                
#print processData("booksauthors.txt", "ratingsbooks.txt")