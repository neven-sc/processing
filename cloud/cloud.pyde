cloud_speed = 5
cloud_movement = -1000


def setup():
    size(800, 500)
    global homer
    homer = loadImage("homer.jpg")
    homer.resize(width, height)


def draw():
    global cloud_speed, cloud_movement
    background(homer)
    # background(9, 116, 232)
    drawCloud(500+cloud_movement*7/8, 200, "#f4f41a")
    drawCloud(700+cloud_movement, 400, "#f716e8")
    drawCloud(150+cloud_movement*4/5, 250, "#34db13")
    
    cloud_movement += cloud_speed
    
    if cloud_movement > 1000:
        cloud_movement = -1000

def drawCloud(xpos, ypos, colour):
    noStroke()
    fill(colour)
    ellipse(xpos, ypos-50, 150, 100)
    ellipse(xpos+40, ypos, 170, 100)
    ellipse(xpos-70, ypos+10, 150, 100)
