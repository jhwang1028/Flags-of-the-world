import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# 각 국기 클릭에 대한 함수들을 정의한다.
def drawKorea(): #대한민국 태극기 그리기
    import turtle 
    import importlib
    import time
    myPen = turtle.Turtle() 
    myPen.shape("arrow")
    myPen.speed(10)

    turtle.bgcolor("white")
    myPen.turtlesize(1)
    myPen.penup()       #그리기 중지
    myPen.goto(0,0)     #원점(화면 중심)으로 이동
    myPen.pendown()     #그리기 시작
    tg = 33.7 #대각선 각=arcTAN(2/3)
    jil = 300 #문양 지름(세로 길이/2)

    #위쪽 태극문양 붉은 부분(대각선에서 시작)
    myPen.color("red")       #선색 및 채우기 붉은색
    myPen.begin_fill()       #채우기 시작
    myPen.rt(90 + tg)        #동에서 남으로 +tg
    myPen.circle(-jil/4,180) #시계방향으로 작은 반원
    myPen.circle(-jil/2,180)   #시계방향으로 큰 반원
    myPen.lt(180)            #남에서 북으로  
    myPen.circle(jil/4,180)  #반시계방향으로 작은 반원
    myPen.end_fill()         #채우기 종료

    #아래쪽 태극문양 파란  부분(대각선 시작)
    myPen.color("blue")     #선색 및 채우기 파란색
    myPen.begin_fill()      #채우기 시작
    myPen.circle(-jil/4,180)#남에서 시계방향으로 작은 반원
    myPen.rt(180)           #북에서 남으로  
    myPen.circle(jil/2,180)   #남에서 반시계방향으로 큰 반원
    myPen.circle(jil/4,180) #북에서 반시계방향으로 작은 반원
    myPen.end_fill()        #채우기 종료
    myPen.rt(90)            #남에서 서쪽으로
    # 태극기 긴 검은 줄<북동시작 남동 종료>

    def long():  #long변수에 긴 검은막대(100*12.5) 정의
        myPen.begin_fill()  #채우기 시작
        myPen.forward(jil/2)  #북동쪽으로 직선 100mm
        myPen.left(90)      #북동에서 왼쪽 90도 북서로
        myPen.forward(jil/12) #북서쪽으로 직선 12.5mm
        myPen.left(90)      #북서에서 왼쪽 90도 남서로
        myPen.forward(jil/2)  #남서로 직선 100mm
        myPen.left(90)      #남서에서 왼쪽 90도남동로
        myPen.forward(jil/12) #남동에서 직선 12.5mm
        myPen.end_fill()    #채우기 종료

    # 태극기 짧은 검은 줄
    def short(): #short변수에 검은막대(45*12.5) 정의
        myPen.begin_fill()
        myPen.forward(jil/4 - jil/48) #잛은 검은선 길이
        myPen.rt(90)
        myPen.forward(jil/12)
        myPen.rt(90)
        myPen.forward(jil/4 - jil/48)
        myPen.rt(90)
        myPen.forward(jil/12)
        myPen.end_fill()

    # 태극기 긴줄 간격 1
    def space1(): #space1변수에  
        myPen.left(180)
        myPen.penup()
        myPen.forward(jil/12 + jil/24)  #18.75
        myPen.pendown()
        myPen.right(90)

    # 태극기 짧은 선 2개 그리고 다음 이동
    def space4():
        myPen.penup()
        myPen.rt(90)
        myPen.backward(jil/4 + jil/48) #간격 18.75mm이동
        myPen.rt(90)
        myPen.forward(jil/12 + jil/24) #간격 18.75mm이동
        myPen.lt(90)
        myPen.pendown()

    # 태극기 짧은검은선 이동(1/24) 이동
    def space2():
        myPen.rt(90)  #왼쪽으로 90도
        myPen.penup()
        myPen.forward(jil/4 + jil/48) #직선(짧은45+간격10=55mm)이동
        myPen.pendown()

    # 태극기 짧은선에서 긴선으로 이동
    def space3():
        myPen.rt(90)
        myPen.penup()
        myPen.forward(jil/4 - jil/48) #직선(짧은45+간격10=55mm)이동
        myPen.rt(90)
        myPen.forward(jil/12 + jil/24) #직선(짧은45+간격10=55mm)이동
        myPen.rt(90)
        myPen.pendown()

    # 태극기 짧은선에서 긴선으로 이동
    def space5():
        myPen.lt(90)
        myPen.penup()
        myPen.forward(jil/2)  #18.75
        myPen.lt(90)
        myPen.forward(jil/12 + jil/24)  #18.75
        myPen.lt(90)
        myPen.pendown()

    # 태극기 건
    myPen.color("black")
    myPen.penup()
    myPen.forward(jil//2 + jil/4)  #-240, 165)
    myPen.right(90)
    myPen.backward(jil/4)
    myPen.pendown()
    long()
    space1()
    long()
    space1()
    long()

    # 태극기 곤
    myPen.penup()
    myPen.goto(0,0)
    myPen.forward(jil//2 + jil/4)
    myPen.left(90)
    myPen.backward(jil//4)
    myPen.pendown()
    short()
    space2()
    short()
    space4()
    short()
    space2()
    short()
    space4()
    short()
    space2()
    short()

    # 태극기 감
    myPen.penup()
    myPen.goto(0,0)
    myPen.rt(90.+22.6)
    myPen.forward(jil/2 + jil/4)
    myPen.left(90)
    myPen.backward(jil/4)
    myPen.pendown()
    short()
    space2()
    short()
    space3()
    long()
    space5()
    short()
    space2()
    short()

    # 태극기 리
    myPen.penup()
    myPen.goto(0, 0)
    myPen.forward(jil/2 + jil/4)
    myPen.right(90)
    myPen.backward(jil//4)
    myPen.pendown()
    long()
    space5()
    short()
    space2()
    short()
    space3()
    long()
    myPen.hideturtle()

    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle)     
#    print("Drawing Korea...")

def drawGermany(): #독일 국기 그리기
    import turtle 
    import importlib
    import time
    myPen = turtle.Turtle() 
    myPen.shape("arrow")
    myPen.speed(10)

    myPen.penup() 
    myPen.goto(-200,-100) 
    myPen.pendown() 
    myPen.color('black') 
    for i in range (2): 
        myPen.forward(500) 
        myPen.left(90) 
        myPen.forward(300) 
        myPen.left(90) 
    myPen.color('yellow') 
    myPen.begin_fill() 

    for i in range (2): 
        myPen.forward(500) 
        myPen.left(90) 
        myPen.forward(100) 
        myPen.left(90) 

    myPen.end_fill() 
    myPen.left(90)
    myPen.forward(100) 
    myPen.left(270) 

    myPen.color('red') 
    myPen.begin_fill() 

    for i in range (2): 
        myPen.forward(500) 
        myPen.left(90) 
        myPen.forward(100) 
        myPen.left(90) 
    
    myPen.end_fill() 

    myPen.left(90) 
    myPen.forward(100) 
    myPen.left(270) 

    myPen.color('black') 
    myPen.begin_fill() 

    for i in range (2): 
        myPen.forward(500) 
        myPen.left(90) 
        myPen.forward(100) 
        myPen.left(90) 
    myPen.end_fill() 

    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle) 
    #print("Drawing Germany...")

def drawUSA(): #미국 국기 그리기
    import turtle
    import sys
    import importlib
    import time

    myPen = turtle.Turtle()

    # Flag height is width / 1.9
    xsize = 640
    ysize = xsize / 1.9

    xoffset = -(xsize / 2)
    yoffset = -(ysize / 2)

    # because ain't nobody got time for that...
    myPen.shape("arrow")
    myPen.speed(10)

    # myPen.exitonclick()
    def rectangle(myPen, x, y, width, height, fcolor = None):
        myPen.penup()
        myPen.setpos(x, y)
        myPen.towards(1, 0)
        myPen.pendown()

        if fcolor is not None:
            oldcolors = myPen.color()
            myPen.color(fcolor, fcolor)
            myPen.begin_fill()

        for _ in range(2):
            myPen.forward(width)
            myPen.left(90)
            myPen.forward(height)
            myPen.left(90)

        if fcolor is not None:
            myPen.end_fill()
            myPen.color(oldcolors[0], oldcolors[1])


    def star(myPen, x, y, radius, fcolor = None):
        unity = radius / 0.525731
        xdist = unity * 0.309017
        adist = unity * 0.381966
        rdist = unity * 0.200811
        ydist = unity * 0.224514

        myPen.penup()
        myPen.setpos(x - xdist, y - (rdist + ydist))
        myPen.towards(x + 1, y)
        myPen.pendown()

        if fcolor is not None:
            oldcolors = myPen.color()
            myPen.color(fcolor, fcolor)
            myPen.begin_fill()

        for _ in range(5):
            myPen.left(36)
            myPen.forward(adist)
            myPen.right(72)
            myPen.forward(adist)
            myPen.left(108)
  
        if fcolor is not None:
            myPen.end_fill()
            myPen.color(oldcolors[0], oldcolors[1])

    # Seven red stripes, Six white stripes.
    stripe_height = ysize / 13;
    sy = yoffset
    for _ in range(7):
        rectangle(myPen, xoffset, sy, xsize, stripe_height, '#BE0D34')
        sy += stripe_height * 2

    # Union is six stripes high, 0.4 of the width.
    union_height = stripe_height * 7
    union_width = xsize * 0.4
    rectangle(myPen, xoffset, stripe_height * 6 + yoffset, union_width, union_height, '#002663')

    # Stars.
    star_hspacing = union_width / 6
    star_vspacing = union_height / 5
    star_radius = (ysize * 0.0616) / 2
    sy_base = (stripe_height * 6) + (star_vspacing / 2) + yoffset

    # 5 rows with 6 stars.
    sy = sy_base
    for row in range(5):
        sx = star_hspacing / 2 + xoffset
        for col in range(6):
            star(myPen, sx, sy, star_radius, "white")
            sx += star_hspacing
        sy += star_vspacing

    # 4 rows with 5 stars.
    sy = sy_base + star_vspacing / 2
    for row in range(4):
        sx = star_hspacing + xoffset
        for col in range(5):
            star(myPen, sx, sy, star_radius, "white")
            sx += star_hspacing
        sy += star_vspacing

    # Border.
    rectangle(myPen, xoffset, yoffset, xsize, ysize)

    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle) 
    #print("Drawing USA...")

def drawRomania(): #루마니아 국기 그리기 
    import turtle
    import importlib
    import time
    myPen=turtle.Turtle()
    myPen.shape("arrow")
    myPen.speed(10)
    myPen.penup()

    myPen.left(90)
    myPen.forward(100)
    myPen.right(90)
    myPen.forward(-150)
    #myPen.back(150)

    myPen.color('dodgerblue4')
    myPen.begin_fill()
    for i in range(2):
        myPen.forward(100)
        myPen.right(90)
        myPen.forward(200)
        myPen.right(90)
    myPen.end_fill()
    myPen.forward(100)

    myPen.color('gold')
    myPen.begin_fill()
    for i in range(2):
        myPen.forward(100)
        myPen.right(90)
        myPen.forward(200)
        myPen.right(90)
    myPen.end_fill()
    myPen.forward(100)

    myPen.color('firebrick3')
    myPen.begin_fill()
    for i in range(2):
        myPen.forward(100)
        myPen.right(90)
        myPen.forward(200)
        myPen.right(90)
    myPen.end_fill()

    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle) 
    #print("Drawing Romania...")

def drawSweden():  #스웨덴 국기 그리기
    import turtle
    import importlib
    import time
    myPen = turtle.Turtle() 
    myPen.shape("arrow")
    myPen.speed(10)

    turtle.bgcolor("#DDDDDD")

    #Position the pen in the bottom left corner
    myPen.penup()
    myPen.goto(-180, -120)
    myPen.pendown()

    #Draw the frame for the flag
    myPen.color("#307DC1")
    myPen.pensize(2)
    myPen.fillcolor("#307DC1")
    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(360)
        myPen.left(90)
        myPen.forward(240)
        myPen.left(90)
    myPen.end_fill()  
  
    #Draw the yellow horizontal stripe
    myPen.color("#FFD900")
    myPen.pensize(2)
    myPen.fillcolor("#FFD900")

    myPen.penup()
    myPen.goto(-180, -20)
    myPen.pendown()

    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(360)
        myPen.left(90)
        myPen.forward(40)
        myPen.left(90)
    myPen.end_fill()  

    #Draw the yellow vertical stripe
    myPen.penup()
    myPen.goto(-80, -120)
    myPen.pendown()

    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(40)
        myPen.left(90)
        myPen.forward(240)
        myPen.left(90)
    myPen.end_fill()

    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle) 

    #print("Drawing Sweden...")

def drawIceland():  #아이슬랜드 국기 그리기
    import turtle
    import importlib
    import time
    myPen = turtle.Turtle()
    myPen.shape("arrow")
    myPen.speed(10)

    window = turtle.Screen()
    window.bgcolor("#DDDDDD")

    #Position the pen in the bottom left corner
    myPen.penup()
    myPen.goto(-180, -120)
    myPen.pendown()

    #Draw the frame for the flag
    myPen.color("royalblue")
    myPen.pensize(2)
    myPen.fillcolor("royalblue")
    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(360)
        myPen.left(90)
        myPen.forward(240)
        myPen.left(90)
    myPen.end_fill()  
  
    #Draw the white horizontal stripe
    myPen.color("white")
    myPen.pensize(2)
    myPen.fillcolor("white")

    myPen.penup()
    myPen.goto(-180, -20)
    myPen.pendown()

    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(360)
        myPen.left(90)
        myPen.forward(40)
        myPen.left(90)
    myPen.end_fill()  

    #Draw the white vertical stripe
    myPen.penup()
    myPen.goto(-80, -120)
    myPen.pendown()

    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(40)
        myPen.left(90)
        myPen.forward(240)
        myPen.left(90)
    myPen.end_fill()  

    #Draw the red horizontal stripe
    myPen.color("red")
    myPen.pensize(2)
    myPen.fillcolor("red")

    myPen.penup()
    myPen.goto(-180, -10)
    myPen.pendown()

    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(360)
        myPen.left(90)
        myPen.forward(20)
        myPen.left(90)
    myPen.end_fill()  

    #Draw the red vertical stripe
    myPen.penup()
    myPen.goto(-70, -120)
    myPen.pendown()

    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(20)
        myPen.left(90)
        myPen.forward(240)
        myPen.left(90)
    myPen.end_fill()  

    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle) 
    #print("Drawing Iceland...")

def drawIndia():   #인도 국기 그리기
    import turtle
    import importlib
    import time
    myPen = turtle.Turtle() 
    myPen.shape("arrow")
    myPen.speed(10)

    # initially penup()
    myPen.penup()
    myPen.goto(-400, 250)
    myPen.pendown()

    # Orange Rectangle 
    #white rectangle
    myPen.color("orange")
    myPen.begin_fill()
    myPen.forward(800)
    myPen.right(90)
    myPen.forward(167)
    myPen.right(90)
    myPen.forward(800)
    myPen.end_fill()
    myPen.left(90)
    myPen.forward(167)

    # Green Rectangle
    myPen.color("green")
    myPen.begin_fill()
    myPen.forward(167)
    myPen.left(90)
    myPen.forward(800)
    myPen.left(90)
    myPen.forward(167)
    myPen.end_fill()

    # Big Blue Circle
    myPen.penup()
    myPen.goto(70, 0)
    myPen.pendown()
    myPen.color("navy")
    myPen.begin_fill()
    myPen.circle(70)
    myPen.end_fill()

    # Big White Circle
    myPen.penup()
    myPen.goto(60, 0)
    myPen.pendown()
    myPen.color("white")
    myPen.begin_fill()
    myPen.circle(60)
    myPen.end_fill()

    # Mini Blue Circles
    myPen.penup()
    myPen.goto(-57, -8)
    myPen.pendown()
    myPen.color("navy")
    for i in range(24):
	    myPen.begin_fill()
	    myPen.circle(3)
	    myPen.end_fill()
	    myPen.penup()
	    myPen.forward(15)
	    myPen.right(15)
	    myPen.pendown()
	
    # Small Blue Circle
    myPen.penup()
    myPen.goto(20, 0)
    myPen.pendown()
    myPen.begin_fill()
    myPen.circle(20)
    myPen.end_fill()
    # Spokes
    myPen.penup()
    myPen.goto(0, 0)
    myPen.pendown()
    myPen.pensize(2)
    for i in range(24):
	    myPen.forward(60)
	    myPen.backward(60)
	    myPen.left(15)
	
    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle) 
    #print("Drawing India...")

def drawCzech(): #체코 국기 그리기
    import turtle
    import importlib
    import time
    myPen = turtle.Turtle() 
    myPen.shape("arrow")
    myPen.speed(10)

    turtle.bgcolor("#DDDDDD")

    #Position the pen in the bottom left corner
    myPen.penup()
    myPen.goto(-180, -120)
    myPen.pendown()

    #Draw the frame for the flag
    myPen.color("white")
    myPen.pensize(2)
    myPen.fillcolor("white")
    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(360)
        myPen.left(90)
        myPen.forward(240)
        myPen.left(90)
    myPen.end_fill()  
  
    #Draw the red horizontal stripe
    myPen.color("#CC2222")
    myPen.pensize(2)
    myPen.fillcolor("#CC2222")

    myPen.penup()
    myPen.goto(-180, -120)
    myPen.pendown()

    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(360)
        myPen.left(90)
        myPen.forward(120)
        myPen.left(90)
    myPen.end_fill()  

    #Draw the blue triangle
    myPen.penup()
    myPen.goto(-180, -120)
    myPen.pendown()

    myPen.color("#2222BB")
    myPen.pensize(2)
    myPen.fillcolor("#2222BB")

    myPen.begin_fill()
    myPen.goto(0,0)
    myPen.goto(-180,120)
    myPen.goto(-180,-120)
    myPen.end_fill()  

    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle) 
    #print("Drawing Czech Republic...")

def drawCameroon():   #카메룬 국기 그리기
    import turtle 
    import importlib
    import time
    myPen = turtle.Turtle() 

    # set up turtle 
    myPen.penup()
    myPen.goto(-300, 150)
    myPen.pendown()
    myPen.speed(10)

    # Draw green band 
    myPen.color("green")
    myPen.begin_fill()
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(300)
    myPen.right(90)
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(300)
    myPen.end_fill()
    myPen.right(90)
    myPen.forward(200)

    # Draw red band 
    myPen.color("red")
    myPen.begin_fill()
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(300)
    myPen.right(90)
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(300)
    myPen.end_fill()
    myPen.right(90)
    myPen.forward(200)

    # Draw yellow band 
    myPen.color("yellow")
    myPen.begin_fill()
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(300)
    myPen.right(90)
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(300)
    myPen.end_fill()
    myPen.right(90)
    myPen.forward(200)

    # Draw the yellow star
    myPen.penup()
    myPen.goto(10, 15)
    myPen.pendown()

    myPen.color("yellow")
    myPen.begin_fill()
    for i in range(5):
        myPen.forward(45)
        myPen.right(144)
        myPen.forward(45)
        myPen.left(144)
        myPen.right(72)
    
    myPen.end_fill()

    myPen.penup()
    myPen.goto(-300, 150)
    myPen.pendown()

    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle)
    #print("Drawing Cameroon...") 

def drawFrance():   #프랑스 국기 그리기
    import turtle 
    import importlib
    import time
    myPen = turtle.Turtle() 
    turtle.bgcolor("#DDDDDD")
    myPen.shape("arrow")
    myPen.speed(10)

    #window.bgcolor("#DDDDDD")

    #Position the pen in the bottom left corner
    myPen.penup()
    myPen.goto(-180, -120)
    myPen.pendown()

    #Draw the frame for the flag
    myPen.color("white")
    myPen.pensize(2)
    myPen.fillcolor("white")
    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(360)
        myPen.left(90)
        myPen.forward(240)
        myPen.left(90)
    myPen.end_fill()  
  
    #Draw the blue stripe
    myPen.color("blue")
    myPen.pensize(2)
    myPen.fillcolor("blue")

    myPen.penup()
    myPen.goto(-180, -120)
    myPen.pendown()

    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(120)
        myPen.left(90)
        myPen.forward(240)
        myPen.left(90)
    myPen.end_fill()  

    #Draw the red stripe
    myPen.color("red")
    myPen.pensize(2)
    myPen.fillcolor("red")

    myPen.penup()
    myPen.goto(60, -120)
    myPen.pendown()

    myPen.begin_fill()
    for i in range(0, 2):
        myPen.forward(120)
        myPen.left(90)
        myPen.forward(240)
        myPen.left(90)
    myPen.end_fill()  

    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle) 
#    print("Drawing France...")

def drawAllFlags(): #10개국 국기 그리기
    drawKorea()
    drawGermany()
    drawUSA()
    drawRomania()
    drawSweden()
    drawIceland()
    drawIndia()
    drawCzech()
    drawCameroon()
    drawFrance()
#    print("Drawing all flags...")

def drawMyLogo(): #나의 로고 그리기
    import turtle 
    import importlib
    import time
    myPen = turtle.Turtle() 
    myPen.shape("arrow")
    myPen.speed(10)

    window = turtle.Screen()
    window.bgcolor("#DDDDDD")

    def circle(color):
        myPen.begin_fill()
        myPen.fillcolor(color)
        myPen.circle(-70)
        myPen.end_fill()

    myPen.penup() 
    myPen.goto(-200,-100) 
    myPen.pendown() 
    myPen.color('black') 
    for i in range (2): 
        myPen.forward(500) 
        myPen.left(90) 
        myPen.forward(300) 
        myPen.left(90) 
    myPen.color('blue') 
    myPen.begin_fill() 

    for i in range (2): 
        myPen.forward(500) 
        myPen.left(90) 
        myPen.forward(100) 
        myPen.left(90) 

    myPen.end_fill() 
    myPen.left(90)
    myPen.forward(100) 
    myPen.left(270) 

    myPen.color('white') 
    myPen.begin_fill() 

    for i in range (2): 
        myPen.forward(500) 
        myPen.left(90) 
        myPen.forward(200) 
        myPen.left(90) 
    
    myPen.end_fill() 

    myPen.left(90) 
    myPen.forward(100) 
    myPen.left(270) 
 
    myPen.goto(-90,165)
    myPen.penup()    
    myPen.color('red')
    myPen.forward(150)
    myPen.pendown()    

    circle('red')

    time.sleep(3)
    turtle.bye()  

    importlib.reload(turtle) 
#    print("Drawing my logo...")

# 메인 윈도우 초기화
root = tk.Tk()
root.title("선택된 국기를 아래에 클릭하면 'Turtle Graphic'을 사용하여 그립니다.")

# 각 국기를 Dictionary로 정의
flags = {
    "Korea.png": ("대한민국", drawKorea),
    "Germany.png": ("독일", drawGermany),
    "USA.png": ("미국", drawUSA),
    "Romania.png": ("루마니아", drawRomania),
    "Sweden.png": ("스웨덴", drawSweden),
    "Iceland.png": ("아이슬랜드", drawIceland),
    "India.png": ("인도", drawIndia),
    "Czech.png": ("체코", drawCzech),
    "Cameroon.png": ("카메룬", drawCameroon),
    "France.png": ("프랑스", drawFrance),
    "allFlags.png": ("10개 국기", drawAllFlags),
    "myLogo.png": ("나의 로고", drawMyLogo),
}

# 각 국기와 레이블을 만들어서 행렬을 구성하는 기능
def create_flag_entry(filename, label_text, command, row, col):
    img_path = f'png/{filename}'
    img = Image.open(img_path).resize((466, 270), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    img_label = ttk.Label(root, image=photo)
    img_label.image = photo  # keep a reference!
    img_label.grid(row=row*2, column=col, padx=5, pady=5)
    img_label.bind("<Button-1>", lambda e: command())

    label = ttk.Label(root, text=label_text, font=("Arial", 14, "bold"))
    label.grid(row=row*2+1, column=col, padx=5, pady=5)

# 각 국기의 Dictionary를 순환하여 행렬에 배치
for index, (file, (label, action)) in enumerate(flags.items()):
    row, col = divmod(index, 4)
    create_flag_entry(file, label, action, row, col)

root.mainloop()
