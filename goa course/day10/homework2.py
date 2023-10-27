import random
from turtle import *
import turtle
colors = ["magenta","darkviolet","pink","blue","purple"]
color(random.choice(colors))
width(random.randint(6,12))
speed(198000)
for i in range(200):
    color("green")
    color(random.choice(colors))
    goto(0,200)
    forward(random.randint(1,800))
    left(random.randint(1,60))
    turtle.write("GOAL ORIENTED ACADEMY",font = ("Verdana",15,"normal")) 
for i in range(50):
    color(random.choice(colors))
    goto(-100,60)
    forward(random.randint(1,600))
    left(random.randint(1,60))
    turtle.write("GOAL ORIENTED ACADEMY",font = ("Verdana",15,"normal")) 
for i in range(50):
    color(random.choice(colors))
    goto(-200,100)
    forward(random.randint(1,630))
    left(random.randint(1,60))
    turtle.write("GOAL ORIENTED ACADEMY",font = ("Verdana",15,"normal"))   
for i in range(50):
    color(random.choice(colors))
    goto(-200,200)
    forward(random.randint(1,600))
    left(random.randint(1,60))  
    turtle.write("GOAL ORIENTED ACADEMY",font = ("Verdana",15,"normal"))    
for i in range(15):
    goto(150,-100)
    turtle.write("GOAL ORIENTED ACADEMY",font = ("Verdana",15,"normal"))        


