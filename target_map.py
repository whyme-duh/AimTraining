import pygame, random, sys, os, math
from pygame.locals import *
pygame.init()
pygame.mixer.init()

W, H = 900, 500
x, y = random.randrange(200, 400), random.randrange(100, 400)
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Target")
map = pygame.image.load('target_map.jpg')
numbers = 1000
targets = []
clock = pygame.time.Clock()
colors = (255,0,0)
white = (255,255,255)
box = pygame.image.load('box.png')
rect = pygame.image.load('rect.png')

# sounds
pygame.mixer.music.load('offsound.mp3')
hit_sound = [pygame.mixer.Sound('metalHit.wav'), pygame.mixer.Sound('fart.wav'), pygame.mixer.Sound('start.wav')]
menu_sound = pygame.mixer.Sound('intro.wav')
# for fonts
font = pygame.font.Font("Pokemon_GB.ttf", 70)
font1 = pygame.font.Font("Pokemon_GB.ttf", 23)
another_font = pygame.font.Font('Beauty Mermaid - Personal Use.ttf', 25)

# rect variables
rect_width = 150
rect_height = 71
r1, r2 = 270, 200
s1 , s2 = 270, 300

# box variables
a1, a2 = 300, 230
b1, b2 = 300, 310
box_width = 300
box_height = 100


class Circle:
    def __init__(self):
        self.x = random.randrange(100, 850)
        self.y =random.randrange(100, 450)
        self.width = random.randrange(10, 20)
        self.radius = self.width
        self.time = 300
        self.visible = True

    def drawing(self, win):

        pygame.draw.circle(win,colors, (self.x, self.y), self.radius, self.width)

for i in range(numbers):
    circlei = Circle()
    targets.append(circlei)
color = (0,0,0)
mouse_x = round(W/2)
mouse_y = round(H/2)


def menu():
    running = True
    while running:
        pygame.mixer.Sound.play(menu_sound)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                p_1, p_2 = pygame.mouse.get_pos()
                if p_1 > a1 and p_1 < a1 + box_width:
                    if p_2 > a2 and p_2 < a2 + box_height:
                        running = False
                        draw()

        win.blit(map, (0,0))
        heading = font.render("TARGETS" , 1 ,(0,0,255))
        play = another_font.render('PLAY', 1, ((255,0,0)))
        settings = another_font.render('SETTINGS', 1, ((255, 0, 0)))
        win.blit(box , (a1, a2))
        win.blit(play , (420, 260))
        win.blit(box, (b1, b2))
        win.blit(settings, (400, 337))
        win.blit(heading , (210, H/2 - 120))
        pygame.display.update()


def play_again():

    play_again = True
    while play_again:
        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_again = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                r_x, r_y = pygame.mouse.get_pos()
                if r_x > r1 and r_x < r1 + rect_width:
                    if r_y > r2 and r_y < r2 + rect_height:
                        draw()
                if r_x > s1 and r_x < s1 + rect_width:
                    if r_y > s2 and r_y < s2 + rect_height:
                        running = True
                        while running:
                            for e in pygame.event.get():
                                if e.type == pygame.QUIT:
                                    running = False
                                    pygame.quit()
                                if e.type == pygame.MOUSEBUTTONDOWN:
                                    p_1, p_2 = pygame.mouse.get_pos()
                                    if p_1 > a1 and p_1 < a1 + box_width:
                                        if p_2 > a2 and p_2 < a2 + box_height:
                                            running = False


                                            draw()

                            win.blit(map, (0, 0))
                            heading = font.render("TARGETS", 1, (0, 0, 255))
                            play = another_font.render('PLAY', 1, ((255, 0, 0)))
                            settings = another_font.render('SETTINGS', 1, ((255, 0, 0)))
                            win.blit(box, (a1, a2))
                            win.blit(play, (420, 260))
                            win.blit(box, (b1, b2))
                            win.blit(settings, (400, 337))
                            win.blit(heading, (210, H / 2 - 120))
                            pygame.display.update()

        replay = font1.render("Play Again", 1, (255, 0, 0))
        menu = font1.render('Menu', 1, (255, 0, 0))
        win.blit(replay, (304, H / 2 - 15))
        win.blit(menu, (374, H / 2 + 90))
        win.blit(rect, (r1, r2))
        win.blit(rect, (s1, s2))
        total_shots = hit_shot + off_shot
        if hit_shot == 0 and off_shot == 0:
            accuracy = 0
        else:
            accuracy = round((hit_shot/ total_shots) * 100)
        average = another_font.render(f'You aim accuracy is: {accuracy} %', 1, (255,255,255))
        win.blit(average, (270, 100))
        pygame.display.update()

def draw():
    # score

    pygame.mixer.Sound.stop(menu_sound)
    pygame.mixer.Sound.play(hit_sound[2])
    global hit_shot, off_shot, total_shots
    hit_shot = 0
    off_shot = 0
    total_shots = 0
    score = 0
    playing = True
    while playing:
        cursor = False
        global colors

        pygame.mouse.set_visible(cursor)
        global mouse_x, mouse_y, white
        r1, r2 = 270, 200
        s1, s2 = 270, 270
        win.blit(map, (0,0))

        now = pygame.time.get_ticks()
        time = 0
        num = 1
        numbers = 1000
        for i in range(num):   # num is for the number of targets increasing for one shot
            # time of one target
            #targets[i].visible = True
            if targets[i].visible :
                if targets[i].time >= 1:
                    targets[i].drawing(win)
                    targets[i].time -= 1
                if targets[i].time == 0:
                    targets.remove(targets[i])
                    play_again()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                # tracking the mouse movement
                if e.type == pygame.MOUSEMOTION:
                    mouse_x = e.pos[0] + 2
                    mouse_y = e.pos[1] + 2
                if e.type == pygame.MOUSEBUTTONDOWN:
                    m_x , m_y = pygame.mouse.get_pos()
                    for i in range(num):
                        dis = math.sqrt((targets[i].x - m_x)**2 + (targets[i].y - m_y)**2)
                        if dis < targets[i].radius:
                            pygame.mixer.Sound.play(hit_sound[1])
                            hit_shot += 1
                            score = score + 1
                            if score > 10:
                                colors = (0,0,255)
                            targets.remove(targets[i])
                        else:
                            off_shot += 1
                            pygame.mixer.music.play(1)
                        total_shots = hit_shot + off_shot
        # for crosshair
        pygame.draw.line(win, color, (mouse_x, mouse_y + 5), (mouse_x, mouse_y - 5))
        pygame.draw.line(win, color, (mouse_x + 5, mouse_y ), (mouse_x- 5, mouse_y ))
        total_score = another_font.render(f"Score : {score}" , 1, (255,255,255))
        win.blit(total_score, (W - 150,50))
        pygame.display.flip()



run = True
while run:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    menu()

pygame.quit()
