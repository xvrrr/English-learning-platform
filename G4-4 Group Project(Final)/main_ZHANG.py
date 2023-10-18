import pygame, sys
import element_ZHANG
import pickwords_ZHANG
import store_ZHANG


def level1():
    global player_x
    global player_y
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1280, 960))
    screen.fill((255,255,255))
    pygame.display.set_caption('Apple Town')
    background_image = pygame.image.load('images/Background.png')  #actual size (1280, 720)
    logo_image = pygame.image.load('images/Logo.png')
    pygame.display.set_icon(logo_image)
    player_image = pygame.image.load('images/Player.png')
    player_x, player_y = 620, 300
    player_step_x = 0
    player_step_y = 0

    pickwords_ZHANG.select()


    wordcheck = []

    font1 = pygame.font.SysFont('New Time Roma', 40)
    output_rect = pygame.Rect(35, 735, 850, 40)
    color = (0, 0, 0)
    pygame.draw.rect(screen, color, output_rect, 2)

    def frame():
        global player_x
        global player_y
        if player_x > 1240:
            player_x = 1240
        if player_x < 0:
            player_x = 0
        if player_y > 680:
            player_y = 680
        if player_y < 0:
            player_y = 0
        if 0 <= player_x <= 480 and 0 <= player_y <= 240:   #top left
            player_x -= player_step_x
            player_y -= player_step_y
        if 0 <= player_x <= 480 and 355 <= player_y <= 720:     #bottom-left
            player_x -= player_step_x
            player_y -= player_step_y
        if 700 <= player_x <= 760 and 385 <= player_y <= 720:   #bottom-right fence
            player_x -= player_step_x
            player_y -= player_step_y
        if 700 <= player_x <= 766 and 0 <= player_y <= 240:     #top right fence
            player_x -= player_step_x
            player_y -= player_step_y
        if 737 <= player_x <= 866 and 210 <= player_y <= 240:   #house left fence
            player_x -= player_step_x
            player_y -= player_step_y
        if 900 <= player_x <= 1280 and 210 <= player_y <= 240:  #house right fence
            player_x -= player_step_x
            player_y -= player_step_y
        if 737 <= player_x <= 1020 and 0 <= player_y <= 170:  #house
            player_x -= player_step_x
            player_y -= player_step_y

    def checking():
        if player_x == 0 and player_y == 260:
            line0 = font1.render(f"a ", True, (0, 0, 0))
            screen.blit(line0, (40, 900))
            wordcheck.append('a')
        if player_x == 0 and player_y == 350:
            wordcheck.append('b')
            line1 = font1.render(f"b ", True, (0, 0, 0))
            screen.blit(line1, (80, 900))
        if player_x == 120 and player_y == 245:
            wordcheck.append('c')
            line2 = font1.render(f"c ", True, (0, 0, 0))
            screen.blit(line2, (120, 900))
        if player_x == 120 and player_y == 350:
            wordcheck.append('d')
            line3 = font1.render(f"d ", True, (0, 0, 0))
            screen.blit(line3, (160, 900))
        if player_x == 240 and player_y == 245:
            wordcheck.append('e')
            line4 = font1.render(f"e ", True, (0, 0, 0))
            screen.blit(line4, (200, 900))
        if player_x == 240 and player_y == 350:
            wordcheck.append('f')
            line5 = font1.render(f"f ", True, (0, 0, 0))
            screen.blit(line5, (240, 900))
        if player_x == 360 and player_y == 245:
            wordcheck.append('g')
            line6 = font1.render(f"g ", True, (0, 0, 0))
            screen.blit(line6, (280, 900))
        if player_x == 360 and player_y == 350:
            wordcheck.append('h')
            line7 = font1.render(f"h ", True, (0, 0, 0))
            screen.blit(line7, (320, 900))
        if player_x == 1150 and player_y == 245:
            wordcheck.append('i')
            line8 = font1.render(f"i ", True, (0, 0, 0))
            screen.blit(line8, (360, 900))
        if player_x == 810 and 175 <= player_y <= 185:
            wordcheck.append('j')
            line9 = font1.render(f"j ", True, (0, 0, 0))
            screen.blit(line9, (400, 900))
        if player_x == 485 and player_y == 440:
            wordcheck.append('k')
            line10 = font1.render(f"k ", True, (0, 0, 0))
            screen.blit(line10, (440, 900))
        if player_x == 485 and player_y == 520:
            wordcheck.append('l')
            line11 = font1.render(f"l ", True, (0, 0, 0))
            screen.blit(line11, (480, 900))
        if player_x == 485 and player_y == 0:
            wordcheck.append('m')
            line12 = font1.render(f"m ", True, (0, 0, 0))
            screen.blit(line12, (520, 900))
        if player_x == 695 and player_y == 0:
            wordcheck.append('n')
            line13 = font1.render(f"n ", True, (0, 0, 0))
            screen.blit(line13, (560, 900))
        if player_x == 695 and player_y == 80:
            wordcheck.append('o')
            line14 = font1.render(f"o ", True, (0, 0, 0))
            screen.blit(line14, (600, 900))
        if player_x == 485 and player_y == 80:
            wordcheck.append('p')
            line15 = font1.render(f"p ", True, (0, 0, 0))
            screen.blit(line15, (640, 900))
        if player_x == 485 and player_y == 600:
            wordcheck.append('q')
            line16 = font1.render(f"q ", True, (0, 0, 0))
            screen.blit(line16, (680, 900))
        if player_x == 485 and player_y == 680:
            wordcheck.append('r')
            line17 = font1.render(f"r ", True, (0, 0, 0))
            screen.blit(line17, (720, 900))
        if player_x == 695 and player_y == 680:
            wordcheck.append('s')
            line18 = font1.render(f"s ", True, (0, 0, 0))
            screen.blit(line18, (760, 900))
        if player_x == 695 and player_y == 600:
            wordcheck.append('t')
            line19 = font1.render(f"t ", True, (0, 0, 0))
            screen.blit(line19, (800, 900))
        if player_x == 695 and player_y == 480:
            wordcheck.append('u')
            line20 = font1.render(f"u ", True, (0, 0, 0))
            screen.blit(line20, (840, 900))
        if player_x == 820 and player_y == 550:
            wordcheck.append('v')
            line21 = font1.render(f"v ", True, (0, 0, 0))
            screen.blit(line21, (880, 900))
        if player_x == 1170 and player_y == 170:
            wordcheck.append('w')
            line22 = font1.render(f"w ", True, (0, 0, 0))
            screen.blit(line22, (920, 900))
        if player_x == 1020 and player_y == 595:
            wordcheck.append('x')
            line23 = font1.render(f"x ", True, (0, 0, 0))
            screen.blit(line23, (960, 900))
        if player_x == 970 and player_y == 440:
            wordcheck.append('y')
            line24 = font1.render(f"y ", True, (0, 0, 0))
            screen.blit(line24, (1000, 900))
        if player_x == 1070 and player_y == 60:
            wordcheck.append('z')
            line25 = font1.render(f"z ", True, (0, 0, 0))
            screen.blit(line25, (1040, 900))





    running = True
    while running:
        screen.blit(background_image, (0, 0))
        element_ZHANG.apple()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_step_y = -5
                elif event.key == pygame.K_s:
                    player_step_y = 5
                elif event.key == pygame.K_d:
                    player_step_x = 5
                    player_image = pygame.transform.flip(player_image, True, False)
                elif event.key == pygame.K_a:
                    player_step_x = -5
                    player_image = pygame.transform.flip(player_image, True, False)
                elif event.key == pygame.K_SPACE:
                    pickwords_ZHANG.word_checking(wordcheck)
                    Word_Line6 = font1.render("The answer is {}.".format(pickwords_ZHANG.word), True, (0, 0, 0))
                    screen.blit(Word_Line6, (900, 840))
                    Word_Line7 = font1.render("Press 'ENTER' to restart", True, (0, 0, 255))
                    screen.blit(Word_Line7, (900, 880))
                if event.key == pygame.K_RETURN:
                    level1()
                    pickwords_ZHANG()

            if event.type == pygame.KEYUP:
                player_step_x = 0
                player_step_y = 0


        element_ZHANG.apple()
        checking()
        screen.blit(player_image, (player_x, player_y))
        player_x += player_step_x
        player_y += player_step_y

        Word_Line0 = font1.render("Warning : Error in position judging, keep trying until shown", True, (255, 0, 0))
        screen.blit(Word_Line0, (40, 740))
        Word_Line1 = font1.render("The characters you picked is :", True, (0, 0, 0))
        screen.blit(Word_Line1, (40, 840))
        Word_Line3 = font1.render('{} different characters'.format(len(pickwords_ZHANG.word)), True, (0, 0, 0))
        screen.blit(Word_Line3, (900, 740))
        Word_Line4 = font1.render('Including {} {} {}'.format(pickwords_ZHANG.word[0], '.' * (len(pickwords_ZHANG.word) - 2), pickwords_ZHANG.word[-1]), True, (0, 0, 0))
        screen.blit(Word_Line4, (900, 780))
        Word_Line5 = font1.render("Your score is {}, press 'SPACE' to check your answer".format(store_ZHANG.num[:-1]), True, (0, 0, 0))
        screen.blit(Word_Line5, (40, 780))
        frame()
        pygame.display.update()
