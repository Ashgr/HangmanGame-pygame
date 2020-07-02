import pygame , math ,time,random



pygame.init()

"""set up the basics"""

WIDTH, HEIGHT = 800 , 500
# Colors   R       G       B
black = (  0   ,   0   ,   0)
white = (  255   ,   255   ,   255)
red = (  255   ,   0   ,   0)
green = (  0   ,   255   ,   0)
blue = (  0   ,   0   ,   255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
caption = pygame.display.set_caption("Hangman")
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)
screen.fill(white)

FPS = 60
clock = pygame.time.Clock()

"""Set up the game loop"""

images = []
for i in range(7):
    img = pygame.image.load("hangman"+str(i)+".png")
    images.append(img)

hangman_level = 0
RAD = 20
DIST = 15

words = ["ASHGR","MINECRAFT","EGG","BRHOM","LAPTOP","HANGMAN"]
word = random.choice(words)
guessed_char = []

startX = round((WIDTH - (RAD * 2 + DIST) * 13) / 2)
startY = 400
buttons = []
A = 65


# Fonts
Letter_Font = pygame.font.SysFont('comicsans',40)
Word_Font = pygame.font.SysFont('comicsans',60)
Title_Font = pygame.font.SysFont('comicsans',70)
BY_Font = pygame.font.SysFont('comicsans',25)


for i in range(26):
    x = startX+ DIST * 2 + ((RAD * 2 + DIST) * (i % 13))
    y = startY + ((i // 13) * (DIST + RAD * 2))
    buttons.append([x,y,chr(A+i),True])

def Draw():
    screen.fill(white)
    # draw title
    text = Title_Font.render("Hangman Game",1,black)
    screen.blit(text,(WIDTH/2 - text.get_width()/2,20))
    # draw by
    by = BY_Font.render("By: Ashgr",1,black)
    screen.blit(by, ((WIDTH / 2 - text.get_width() / 2)+395, 42))
    # draw a word
    display_word = ""
    for char in word:
        if char in guessed_char:
            display_word += char + " "
        else:
            display_word += "_ "


    text = Word_Font.render(display_word,1,black)
    screen.blit(text,(400, 200))

    # draw buttons
    for btn in buttons:
        x , y , chr , vis = btn
        if vis:
            pygame.draw.circle(screen,black,(x,y) , RAD , 3)
            text = Letter_Font.render(chr,1,black)
            screen.blit(text,(x-text.get_width()/2,y-text.get_width()/2))

    screen.blit(images[hangman_level], (150, 100))
    pygame.display.update()


def display_message(messege):
    pygame.time.delay(1000)
    screen.fill(white)
    text = Word_Font.render(messege, 1, black)
    screen.blit(text, (300, 200))
    pygame.display.update()
    pygame.time.delay(5000)

ALIVE = True
while ALIVE:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ALIVE = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            for btn in buttons:
                x , y , letter , vis = btn
                if vis:
                    dis = math.sqrt((x-mouse_x)**2 + (y-mouse_y)**2)
                    if dis < RAD:
                        guessed_char.append(letter)
                        btn[3] = False
                        if letter not in word:
                            hangman_level +=1
    Draw()
    winning = True
    for char in word:
        if char not in guessed_char:
            winning = False
            break
    if winning:
        display_message("You Won !")
        break
    if hangman_level == 6:
        display_message("You Lose !")
        break

pygame.quit()