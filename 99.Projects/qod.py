# coding=utf-8
import random as r
quotes={}
def quoteplease():
    print(quotes)
    return 

def addquote():
    noquotes=[]
    quotedby=input("Enter the name of person quoted it")
    quoteslist=quotes.get(quotedby,noquotes)
    quote=input("enter the quote")
    quoteslist.append(quote)
    quotes[quotedby]=quoteslist

def searchbyperson():
    person=input("enter person name")
    if(person in quotes.keys()):
        print("Quotes of ",person)
        for quote in quotes.get(person):
            print(quote)
    else:
        print("No Quotes. Please add if you know one")

def randomquote():
    quote=r.choice(quotes.get(r.choice(quotes.keys())))
    print(quote)
    
functions={
    1:addquote,
    2:searchbyperson,
    3:quoteplease,
    4:randomquote
}
while 1:
    print("Welcome to the Skillverse Quote of the Day")
    print("1. Submit a Quote")
    print("2. Browse Quotes by Person")
    print("3. Display all quotes")
    print("4. Show a random Quote")
    choice=int(input())
    task=functions.get(choice,"Cannot Do that!")
    task()

