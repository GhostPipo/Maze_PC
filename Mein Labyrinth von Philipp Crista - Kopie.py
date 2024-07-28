import turtle
import math
import random
from tkinter import messagebox
import tkinter as tk



current_level = 1


fenster= turtle.Screen()
fenster.bgcolor("black")
fenster.title("Mein Labyrinth von Philipp Crista")
fenster.setup(700,700)







class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue3")
        self.penup()
        self.speed(0)
        fenster.tracer(0)


    def destroy_walls():
        pen.goto(2000,2000)
        pen.clear()





class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
        self.direction = ""
    

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False


    def destroy(self):
         self.goto(2000, 2000)
         self.hideturtle()

    def stop(self):
        self.direction = ""




class Enemy(turtle.Turtle):
    def __init__(self, x, y, speed=1):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])
        self.enemy_speed = speed
        self.move()

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])


        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 50:
            return True
        else:
            return False


    
            




class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class Finishline(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_finishline(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Finishline2(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_finishline2(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Finishline3(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("purple")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_finishline3(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Finishline4(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("orange")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_finishline4(self):
        self.goto(2000, 2000)
        self.hideturtle()




class Finishline5(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("navy")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_finishline5(self):
        self.goto(2000, 2000)
        self.hideturtle()





class Finishline6(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("Orange")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_finishline6(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Finishline7(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("skyblue")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_finishline7(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Finishline8(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("cyan")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_finishline8(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Finishline9(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_finishline9(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Fakeline1(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_fakeline1(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Fakeline2(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_fakeline2(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Fakeline3(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_fakeline3(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Finishline10(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.hideturtle()



    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False


    def destroy_finishline10(self):
        self.goto(2000, 2000)
        self.hideturtle()



level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",       
"XP                      X",
"XX XXX  XXXX   XXX  XXX X",
"X  XX                   X",
"X  XXXXXXXXXXX XXXXXXXX X",
"XX           X X        X",
"X  XXXXXXXXXXX X XXX  XXX",
"X  XXXXXXXXXXX X XXX  XXX",
"XX XE          X XXX  XXX",
"X  XXXXXXXXXXX X X    E X",
"X  XXXXXXXXXXXXX XX XXX X",
"XX XX          X XX XXX X",
"X  XX XXXXXXXX X XX XXX X",
"X  XX XXXXXXXX X XX XXX X",
"XX XX XXXXXXXX X XX  TX X",
"X  XX    XXXXX XXXXXXXX X",
"X  XXXXX XXXXX        X X",
"XX XXXXX     XXXXXXXX X X",
"X  XXXXX X  XXXXXXXXX X X",
"X  XXXXX X          X X X",
"XX XXXXX XX XXXXXXX X XXX",
"X  XXXXX XX XXXXXXX X   X",
"X  XXXXX XX        TX   X",
"XX       XXXXXXXXXXXX  FX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]



level_2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP            XXXXXXXXXXX",
"XX   XXXXXXXX          XX",
"XX XXXXXXXXXX  XXXXXXX XX",
"XX XXXXXXXXXX        X XX",
"XX XXXXE      XXXXXXXX XX",
"XX   XX XXXXX XXXX   X XX",
"XX XXXX XXXXX XXXX X X XX",
"XX XXXX XXXXX XXXX X X XX",
"XX XXXX XXXXX XXXX X X XX",
"XX   XX XXXXX XXXX X X XX",
"XX XXXX    XX XXXX X   XX",
"XX XXXXX X XX XXXX XXXXXX",
"XX   XXX X XX XXXX X  EXX",
"XX XXXXX XEXX XXXX     XX",
"XX XXXXX X XX XXXXXXXX XX",
"XX       X XX       XX XX",
"XXXXXXXXX  X  XXXXX XX XX",
"XXXXX   X XX  X  TX XX XX",
"XXXXX XTX XX  X XXX XX  X",
"XXXXX XXX XX  X     XX  X",
"XXXXX     XXE XXXXXXXX  X",
"XXXXXXXXXXXX  XXXXXXXX  X",
"XXXXXXXXXXXX         X GX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]


level_3 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                XXXXXXX",
"XX  XXXXX  XXXXXX      XX",
"XX  XXXXX  XXXXXXXXXXX XX",
"XX  XXXXX  X     EXT   XX",
"XX  XXXXX     XXX XX X XX",
"XX  XXXXXXXXX XXX XX X XX",
"XX  XXXXXXXXX XXX    X XX",
"X   XXXXXXXXX XXXXXXXX XX",
"X XXXXXXXXXXX XXXXXXXX XX",
"X XX               E    X",
"X XX XXXXXXXX XXXXXXXXX X",
"X XX XT    XX XXXXXXXXX X",
"X XX XXXX  XX XXXXXXXXX X",
"X XX       XX XXXXXXXXX X",
"X XXXXXXXXXXX XXXXXXXXX X",
"X    XX       XXXXXXXXXTX",
"X XX XX XXXXXXXXXXXXXXXXX",
"X XXXXX XXXXXXXXXT     XX",
"X XXXXX XXXXXXXXXXX X XXX",
"X XXXXX X             EXX",
"X XXXXX    XXXXXXXXXXX  X",
"X XXXXXXXXXXXXXXXXXXXX  X",
"XE          TX         QX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]


level_4 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP         X   XX      TX",
"XX XXX  XXXX   XXX  XXX X",
"X  XXE                  X",
"X  XXXXXXXXXXX XXXXXXXX X",
"XX          EX X        X",
"X  XXXXXXXXXXX X XXX  XXX",
"X  XXXXXXXXXXX X XXX  XXX",
"XX X           X XXX  XXX",
"X  XXXXXXXXXXX X XE     X",
"X  XXXXXXXXXXXXX XX XXX X",
"XX XX         TX XX XXX X",
"X  XX XXXXXXXXXX XX XXX X",
"X  XX          X XX XXX X",
"XX XX XXXXXX   X XX  TX X",
"X  XX    XXX   XXXXXXXX X",
"X  XXXXX XXX  E       X X",
"XX XXXXX   EXXXXXXXXX X X",
"X  XXXXX X  XXXXXXXXX X X",
"X  XXXXX X         EX XTX",
"XX XXXXX XX XXXXXXX X XXX",
"X  XXXXX XX XXXXXXX X   X",
"X  XXXXX XX        TX   X",
"XX       XXXXXXXXXXXX  UX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_5 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                    EXX",
"XX   XXXXXXXX          XX",
"XX XXXXXXXXXX  XXXXXXX XX",
"XX XXXXXXXXXX       EXTXX",
"XX XXXX        XXXXXXXXXX",
"XX   XX XXXXX XXXX   XTXX",
"XX XXXX XXXXX XXXX X X XX",
"XX XXXX XXXXXEXXXX X X XX",
"XX XXXX XXXXX    X X X XX",
"XX   XX XXXXX XXXX X X XX",
"XX XXXX    XX XXXX X    X",
"XX XXXXX X XX    X XXXX X",
"XX   XXX X XX XXXX XE   X",
"XX XXXXX X XX XXXX XXXX X",
"XX XXXXX X XX    X    X X",
"XXEXXXXX X XX XXXXXXX X X",
"XX       X XX       X X X",
"XXXXXXXXX  X  XXXXX X X X",
"XXXXX   X XX  XE    X X X",
"XXXXX XTX XX  XXXXX X X X",
"XXXXX XXX XX  XT      X X",
"XXXXX  E  XX  XXXXXXXXX X",
"XXXXXXXXXXXX  XXXXXXXXX X",
"XXXXXXXXXXXX         XXOX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]



level_6 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP               TXXXXXXX",
"XX X XXXXXXXXXXXXXX     X",
"XX X X            X XXX X",
"XX X X XXXXXXXXX  X XTX X",
"XX X X      XX    X X X X",
"XX X XXXXXX XXXX EX X X X",
"XX X        XX    X X X X",
"XX XXXXXXXXXXXXX  X X X X",
"XX      XXXXXX    X   X X",
"XXXXXXX XXXXXXXX EXXX X X",
"XXX  TX XXXXXX    XXX X X",
"XXX XXX XXXXXXXX      X X",
"X        E   X    XXX X X",
"XXXXXX X X X XXX  X   X X",
"X   XX X X X XXXXXXXXXX X",
"X X XX X X X XXXXXXXX   X",
"X X XXXXXXXX XXXXXXXE XXX",
"X X      TXX XXXXXXX  XXX",
"X XXXXXX     XXXXXXX   TX",
"X XX    XXXXXXXXXXXX  XXX",
"X    XX XT             TX",
"XXXXXXX XXXXX X X XX  XXX",
"XXXXXXX         X  X   AX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_7 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP X                    X",
"X  X  XXXXXXXXXXXXXXXXX X",
"X  X  XXXX           XX X",
"X  X  XXXX XXXXXXXXX XX X",
"X  X  XXXX XT     TX XX X",
"X  X  X    XXXXE XXX XX X",
"X  X  X XXXXXT    TX XX X",
"X  X  X XXXXXXX  XXX XX X",
"X  X  X XX           XX X",
"X  X  X XX  XXXXXXXXXXX X",
"X  X  X XX            X X",
"X  X  X XXXXXXXXXXX   X X",
"X  X  X XXXXX         X X",
"X  X  X     X E  XXXXXX X",
"X  X  XXXXX X         X X",
"X EX  X   X XXXXXXXXX X X",
"X  X  X E X X  X      X X",
"X  X      X X  E XXXXXX X",
"X  XXXX   X X  X        X",
"X  X      X XXXXXXXXXXXXX",
"X  X    E X        XXXXXX",
"X  XXXX   XXXXXXXX XXX  X",
"X             E  X     KX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_8 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                      X",
"X   X       E   E   E   X",
"X   X X X X X X X X X X X",
"X   X X X X X X X X X X X",
"X   XTXTXTXTXTXTXTXTXTXTX",
"X   XXXXXXXXXXXXXXXXXXXXX",
"X        E    X         X",
"X         E   X XXXXXXX X",
"XXXXXXXXXXXXX X X     X X",
"X      XXXXXX X X       X",
"X XXXX     XX X X XXXXXXX",
"X XTTX XXX XX X X       X",
"X X  X XTX XX X XXXXXXX X",
"X X  X X   XX X XXXXXXX X",
"X X  X XXXXXX X XXXXXXX X",
"X    X        X X    XX X",
"X  E XXXXXXXXXX XX X X  X",
"X    XXXXXXXXXX XX X X  X",
"X XXXXX          E X X  X",
"X XX   XXXXXXXXX   X X  X",
"X XX X X   X   X   X X  X",
"X XX X X X X X XXXXX XE X",
"X    X   X   X       X BX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]



level_9 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                      X",
"X XXXXXXXXXXXXXXXXXXXXX X",
"X        X              X",
"XXXXXXXX X XXXXXXXXXXXXXX",
"X        X        E     X",
"X  XXXXXXX              X",
"X        XXXXXXXXXXXXXX X",
"X  XXXXXXX          E   X",
"X    E   X XXXXXXXXXXXXXX",
"X        X        XXXXXXX",
"XXXXXXXX XXXXXXX        X",
"X  E  TX X        XXXXX X",
"X        X XXXXX  X   X X",
"XXXXXXXX X X   X  X XTXTX",
"XXXXX   EX XTX X  X X X X",
"X    XXX X X X X  X XTXTX",
"X XX XXX X XTX X  X X X X",
"X XX X   X XXX X  X XTXTX",
"X XX XXX X     X  X XXX X",
"X XX XXX XXXXXXX  X     X",
"X XX     XX       XXXXXXX",
"X  XXXXXXXX X XXXXX     X",
"XV        X          E 1X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]


level_10 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP         X            X",
"XXXXXXXX X X XXXXXXXX X X",
"X        X   X        X X",
"X        XXXXX XXXXXXXX X",
"X XXXXXXXXXXXX X    XX  X",
"X         XXXX   XX XXE X",
"XXXXXXXXX X   XXXXX XX  X",
"X         X X       XX  X",
"X  XXXXXXXX XXXXXXXXXX  X",
"X        TX          X  X",
"X  XXXXXX XXXXXXXXXX X  X",
"X       X TX   X   X X  X",
"X     E XXXX X X X X X  X",
"XX X X  X    X   X   X  X",
"XXTXTX  X XXXXXXXXXXXX  X",
"XXTXTX  X          XXX  X",
"XXXXXX  XXXXXXXXXX X T  X",
"XX E XX X       XX X X  X",
"X     X X XXXXX XX XTXE X",
"X X X X X    XX XX X X  X",
"X XTX X XXXX XX XX X    X",
"X XXX   XXX   X    XX XXX",
"X  Z XXXXXXT2TXXXXXX 3 XX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

levels = ["", level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9, level_10]

levels.append(level_1)

enemies = []
treasures = []





def destroy_enemies():
    for enemy in enemies:
        enemy.goto(2000, 2000)
        enemy.hideturtle()
    enemies.clear()        



def touch_treasure():
        if player.is_collision(treasure):
            player.gold += 100
        messagebox.showinfo("Gold erhalten!", f"Du hast jetzt {player.gold} Gold!")
    

def destroy_treasures():
    for treasure in treasures:
        treasure.goto(2000, 2000)
        treasure.hideturtle()
    treasures.clear()


def setup_maze(level):
    
    walls.clear()
    
    for y in range(len(level)):
        for x in range(len(level[y])):
            charakter = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)


            if charakter == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if charakter == "P":
                player.goto(screen_x, screen_y)

            if charakter == "E":
                enemies.append(Enemy(screen_x, screen_y, speed=1))
               
                
        
            if charakter == "T":
                treasures.append(Treasure(screen_x, screen_y))

            if charakter == "F":
                player2.goto(screen_x, screen_y)

            if charakter == "G":
                player3.goto(screen_x, screen_y)

            if charakter == "Q":
                player4.goto(screen_x, screen_y)

            if charakter == "U":
                player5.goto(screen_x, screen_y)

            if charakter == "O":
                player6.goto(screen_x, screen_y)

            if charakter == "A":
                player7.goto(screen_x, screen_y)

            if charakter == "K":
                player8.goto(screen_x, screen_y)

            if charakter == "B":
                player9.goto(screen_x, screen_y)


            if charakter == "1":
                player10.goto(screen_x, screen_y)

            if charakter == "V":
                player11.goto(screen_x, screen_y)

            if charakter == "2":
                player12.goto(screen_x, screen_y)

            if charakter == "3":
                player13.goto(screen_x, screen_y)

            if charakter == "Z":
                player14.goto(screen_x, screen_y)

    

    


    

    











       
                
                
   
                
pen = Pen()
player= Player()
player2= Finishline()
player3= Finishline2()
player4= Finishline3()
player5= Finishline4()
player6= Finishline5()
player7= Finishline6()
player8= Finishline7()
player9= Finishline8()
player10= Fakeline1()
player11= Finishline9()
player12= Fakeline2()
player13= Fakeline3()
player14= Finishline10()
walls = []
game_state = "game"
setup_maze(levels[1])






turtle.onkeypress(player.go_left, "Left")
turtle.onkeypress(player.go_left, "a")
turtle.onkeypress(player.go_right, "d")
turtle.onkeypress(player.go_right, "Right")
turtle.onkeypress(player.go_up, "w")
turtle.onkeypress(player.go_up, "Up")
turtle.onkeypress(player.go_down, "s")
turtle.onkeypress(player.go_down, "Down")
turtle.onkeyrelease(player.stop, "Left")
turtle.onkeyrelease(player.stop, "a")
turtle.onkeyrelease(player.stop, "Right")
turtle.onkeyrelease(player.stop, "d")
turtle.onkeyrelease(player.stop, "Up")
turtle.onkeyrelease(player.stop, "w")
turtle.onkeyrelease(player.stop, "Down")
turtle.onkeyrelease(player.stop, "s")

info_text = ("Die blaue Figur ist der Spieler, den du mit WASD steuern kannst. "
                "Die roten Kreise sind Gegner. Wenn du sie berührst, endet das Spiel. "
                    "Die gelben Kreise sind Truhen. Wenn du sie berührst, bekommst du 100 Gold. "
                     "Die farbigen Quadrate unten rechts sind die Endpunkte. "
                     "Wenn du sie erreichst, kommst du zum nächsten Level. "
                     "Dein Ziel ist es, sicher aus dem Labyrinth zu kommen und so viel Gold wie möglich zu erbeuten.")





def show_info():
    messagebox.showinfo("Spielinformation", info_text)

def show_gold():
    messagebox.showinfo("Goldstatus", gold_counter)

  

fenster.listen()
fenster.onkeypress(lambda: turtle.bye() ,"p")
fenster.onkeypress(show_info,"i")

fenster.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)


def destroy_walls():
    pen.goto(2000,2000)
    pen.clear()



def start_menu():
    global game_state
    game_state = "menu"

def start_trap():
    global game_state
    game_state = "Trap"



while True:

    

    for enemy in enemies:
        if player.is_collision(enemy):
            start_menu()
            

    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
            touch_treasure()



    if player2.is_collision(player):
        destroy_walls()
        destroy_enemies()
        destroy_treasures()
        player2.destroy_finishline()
        pen.shape("circle")
        pen.color("magenta")
        player.shape("circle")
        setup_maze(levels[2])
        player3.showturtle()
        

    if player3.is_collision(player):
        destroy_walls()
        destroy_enemies()
        destroy_treasures()
        pen.shape("square")
        pen.color("deepskyblue")
        player.shape("square")
        player3.destroy_finishline2()
        setup_maze(levels[3])
        player4.showturtle()
        

    if player4.is_collision(player):
        destroy_walls()
        destroy_enemies()
        destroy_treasures()
        pen.shape("square")
        pen.color("springgreen")
        player.shape("square")
        player4.destroy_finishline3()
        setup_maze(levels[4])
        player5.showturtle()
        

    
    if player5.is_collision(player):
        destroy_walls()
        destroy_enemies()
        destroy_treasures()
        pen.shape("circle")
        pen.color("violet")
        player.shape("circle")
        player5.destroy_finishline4()
        setup_maze(levels[5])
        player6.showturtle()


    if player6.is_collision(player):
        destroy_walls()
        destroy_enemies()
        destroy_treasures()
        pen.shape("square")
        pen.color("deepskyblue")
        player.shape("square")
        player6.destroy_finishline5()
        setup_maze(levels[6])
        player7.showturtle()

    if player7.is_collision(player):
        destroy_walls()
        destroy_enemies()
        destroy_treasures()
        player7.destroy_finishline6()
        pen.shape("circle")
        pen.color("magenta3")
        player.shape("circle")
        setup_maze(levels[7])
        player8.showturtle()

    if player8.is_collision(player):
        destroy_walls()
        destroy_enemies()
        destroy_treasures()
        player8.destroy_finishline7()
        pen.shape("square")
        pen.color("firebrick3")
        player.shape("square")
        setup_maze(levels[8])
        player9.showturtle()



    if player9.is_collision(player):
        destroy_walls()
        destroy_enemies()
        destroy_treasures()
        player9.destroy_finishline8()
        pen.shape("circle")
        pen.color("mediumpurple2")
        player.shape("circle")
        setup_maze(levels[9])
        player11.showturtle()
        player10.showturtle()


    if player11.is_collision(player):
        destroy_walls()
        destroy_enemies()
        destroy_treasures()
        player11.destroy_finishline9()
        player10.destroy_fakeline1()
        pen.shape("square")
        pen.color("violet")
        player.shape("circle")
        setup_maze(levels[10])
        player14.showturtle()
        player12.showturtle()
        player13.showturtle()

        

    if player10.is_collision(player):
        start_trap()

    if player12.is_collision(player):
        start_trap()

    if player13.is_collision(player):
        start_trap()

    

    if game_state == "menu":
        fenster.bgpic("Menü.gif")
        destroy_enemies()
        destroy_treasures()
        player.goto(2000,2000)
        destroy_walls()
        player2.destroy_finishline()
        player3.destroy_finishline2()
        player4.destroy_finishline3()
        player5.destroy_finishline4()
        player6.destroy_finishline5()
        player7.destroy_finishline6()
        player8.destroy_finishline7()


    if game_state == "Trap":
        fenster.bgpic("Trap1.gif")
        destroy_enemies()
        destroy_treasures()
        player.goto(2000,2000)
        destroy_walls()
        player2.destroy_finishline()
        player3.destroy_finishline2()
        player4.destroy_finishline3()
        player5.destroy_finishline4()
        player6.destroy_finishline5()
        player7.destroy_finishline6()
        player8.destroy_finishline7()
        

        

    if player14.is_collision(player):
        destroy_walls()
        destroy_enemies()
        destroy_treasures()
        player14.destroy_finishline10()
        player12.destroy_fakeline2()
        player13.destroy_fakeline3()
        player.goto(2000,2000)
        start_menu()

    
        
            
            
    fenster.update()


    






    
