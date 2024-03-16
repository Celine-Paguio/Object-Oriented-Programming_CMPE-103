# Object-Oriented Programming_Program Number 2
# Paguio, Celine Rose S.
# BSCPE 1-2
# March 16, 2024

# to import art module
from art import text2art

# to ask for the input of name and dream job
name = input("\033[1;33;40mPlease enter your name: ")
dream_job = input("\033[1;33;40mPlease enter your dream job: ")

# to print name and dream job with art and color
print("\033[1;31;40m" + text2art("Name: ", font='block', chr_ignore=True))
art_name = text2art(name, font='block', chr_ignore=True)
print("\033[1;34;40m" + art_name)
print("\033[1;31;40m" + text2art("Dream Job: ", font='block', chr_ignore=True))
art_dream_job = text2art(dream_job, font='block', chr_ignore=True)
print("\033[1;34;40m" + art_dream_job)

# end of program
