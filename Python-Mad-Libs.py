"""
Description: How do you feel?
Author:  shreyas
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s ruled the world."

#start of the game as presented by CodeAcademy
print ("MadLibs has started")

#the hero's name ig, idk bro
name = raw_input("What is your main Character's name? ")

#these are just to take up the adjectives for making up the story
ad1 = raw_input("What is your choice for 1st adjective? ")
ad2 = raw_input("What is your choice for 2nd adjective? ")
ad3 = raw_input("What is your choice for 3rd adjective? ")

#GIVE A VERB
verb = raw_input("What is your choice for a verb? ")

#now it prompts me for nouns
noun1 = raw_input("What is your choice for 1st noun? ")
noun2 = raw_input("What is your choice for 2nd noun? ")

#now for the random assortment of thing
animal = raw_input("What is your favourite animal? ")
food = raw_input("What is your favourite thing to eat? ")
fruit = raw_input("What is your favourite fruit? ")
superhero = raw_input("What is your favourite superhero? ")
country = raw_input("What is your favourite country? ")
dessert = raw_input("What is your favourite sweet treat? ")
year = raw_input("Give me a random year: ")

#final output command
print(STORY % (name, ad1, ad2, animal, food, verb, noun1, fruit, ad3, name, superhero, name, country, name, dessert, name, year, noun2))

