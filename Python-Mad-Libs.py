"""
Description: How do you feel?
Author:  shreyas
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s ruled the world."

#start of the game as presented by CodeAcademy
print ("MadLibs has started")

#the hero's name ig, idk bro
name = input("What is your main Character's name? ")

#these are just to take up the adjectives for making up the story
ad1 = input("What is your choice for 1st adjective? ")
ad2 = input("What is your choice for 2nd adjective? ")
ad3 = input("What is your choice for 3rd adjective? ")

#GIVE A VERB
verb = input("What is your choice for a verb? ")

#now it prompts me for nouns
noun1 = input("What is your choice for 1st noun? ")
noun2 = input("What is your choice for 2nd noun? ")

#now for the random assortment of thing
animal = input("What is your favourite animal? ")
food = input("What is your favourite thing to eat? ")
fruit = input("What is your favourite fruit? ")
superhero = input("What is your favourite superhero? ")
country = input("What is your favourite country? ")
dessert = input("What is your favourite sweet treat? ")
year = input("Give me a random year: ")

#final output command
print(STORY % (name, ad1, ad2, animal, food, verb, noun1, fruit, ad3, name, superhero, name, country, name, dessert, name, year, noun2))

