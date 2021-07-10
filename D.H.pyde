def setup():
    size(200, 200) 
    
def draw():
    rect(50,50,100,100)
    fill(25, 0, 0)
    textSize(38)
    text('D H', 68, 113)
    a = fill(255, 25, 400)
    if ((mouseX >= 50 and mouseX <= 150)and(mouseY <= 150 and mouseY >= 50)):
        if mousePressed:
            text('D H', 68, 113)
            a = fill(0, 0, 0)
    if keyPressed:
        if key == 'q' or key == 'Q':
            text('D H', 68, 113)
            a = fill(500, 0, 0)
        if key == 'e' or key == 'E':
            text('D H', 68, 113)
            a = fill(200, 50, 0)
        if key == 'w' or key == 'W':
            text ('D H', 68, 113)
            a = fill(30, 44, 0)
        if key == 'r' or key == 'R':
            text('D H', 68, 113)
            a = fill(90, 5, 111)
