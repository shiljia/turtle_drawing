
import turtle

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('gray')
t.pensize(2)

t.goto(-100,0)
t.fillcolor('blue')
t.begin_fill()
for i in range(4):
    t.fd(100)
    t.rt(90)
t.end_fill()
t.fd(100)

t.fillcolor('purple')
t.begin_fill()
t.fd(250)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(250)
t.end_fill()

t.fd(70)
t.rt(90)


t.fillcolor('brown')
t.begin_fill()
t.fd(60)
t.rt(90)
t.fd(35)
t.rt(90)
t.fd(60)
t.end_fill()


t.pu()
t.home()
t.pd()

t.fillcolor('pink')
t.begin_fill()
t.lt(125)
t.fd(90)
t.lt(110)
t.fd(90)
t.end_fill()


t.bk(90)
t.lt(35)

t.fillcolor('yellow')
t.begin_fill()
t.fd(30)
t.rt(90)
t.circle(10)
t.end_fill()

    
t.pu()
t.home()
t.pd()




t.fillcolor('orange')
t.begin_fill()
t.fd(250)
t.lt(90)
t.fd(74)
t.lt(90)
t.fd(302)
t.end_fill()

t.pu()
t.home()
t.rt(90)
t.fd(33)
t.lt(90)
t.fd(70)
t.pd()


t.fillcolor('brown')
t.begin_fill()
for j in range(2):
    t.fd(70)
    t.rt(90)
    t.fd(40)
    t.rt(90)
t.end_fill()

t.fd(35)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(35)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(70)
t.ht()

    





