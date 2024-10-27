import pgzrun 
from random import randint

TITLE="FLAPPY BALL"
WIDTH=600
HEIGHT=500

R=randint(0,255)
G=randint(0,255)
B=randint(0,255)

CLR=R,G,B

GRAVITY=2000.0 #pixels per second

class Ball:
    #constructer
    def __init__(self,IX,IY):
        self.x=IX
        self.y=IY
        self.radius=40
        self.vx=200
        self.vy=0

    def draw(self):
         pos=(self.x,self.y)
         screen.draw.filled_circle(pos,self.radius,CLR)

ball = Ball(50,100)

def draw():
    screen.clear()
    ball.draw()

def update(dt):
    # Applying constant acceleration formule
    #v = u + at (u=initial velocity, v = final velocity, a = acceleration and t = time passed)
    uy = ball.vy
    ball.vy += GRAVITY * dt
    ball.y += (uy + ball.vy) * 0.5 * dt
    #detect and hndle bouncing
    if ball.y > HEIGHT-ball.radius: #We have bounced
        ball.y = HEIGHT-ball.radius# fix the position
        ball.vy = -ball.vy * 0.9 #For smooth bouncing effect

    #X component doesn't have acceleration
    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

#on pressing space key
def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -50

pgzrun.go()


    






        
