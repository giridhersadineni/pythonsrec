import random as r
quotes=[]
quotes.append('“The Way Get Started Is To Quit Talking And Begin Doing.” – Walt Disney')
quotes.append('“The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.” – Winston Churchill')

def quoteplease():
    quote=r.choice(quotes)
    print(quote)
    return 

def addquote():
    quote=input("Enter a Quote")
    quotes.append(quote)


functions={
    1:addquote,
    2:quoteplease
}
while 1:
    print("Welcome to the Skillverse Quote of the Day")
    print("Enter 1 to Submit a Quote")
    print("Enter 2 to view a random Quote")
    choice=int(input())
    task=functions.get(choice,"Cannot Do that!")
    task()

