import pygame
import sys
import element_ZHANG
import main_ZHANG


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption('Apple Town')
base_font = pygame.font.Font(None, 40)
logo_image = pygame.image.load('images/Logo.png')
pygame.display.set_icon(logo_image)
user_text = ''

font0 = pygame.font.SysFont('Arial', 60)
font1 = pygame.font.SysFont('New Time Roma', 40)

background_msc = pygame.mixer.Sound('bgm/Disco Elysium Record(Not do commercial).mp3')
pygame.mixer.Sound.play(background_msc)
pygame.mixer.Sound.set_volume(background_msc, 0.2)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.display.update()
                main_ZHANG.level1()

    screen.fill((255,255,255))

    element_ZHANG.tree()
    line0 = font0.render(f"Apple Town ", True, (139, 137, 137))
    screen.blit(line0, (500, 400))
    line2 = font1.render(f"Press 'SPACE' to enter the apple town", True, (0, 0, 0))
    screen.blit(line2, (380, 800))
    line3 = font1.render(f"Control:'WASD'", True, (0, 0, 0))
    screen.blit(line3, (280, 600))
    line4 = font1.render(f"About :", True, (0, 0, 0))
    screen.blit(line4, (280, 500))
    line5 = font1.render(f"There are too many apples in this town", True, (0, 0, 0))
    screen.blit(line5, (380, 500))
    line6 = font1.render(f"Select them and fill the blank using ", True, (0, 0, 0))
    screen.blit(line6, (380, 540))
    line7 = font1.render(f"Author: Hanhao ZHANG", True, (0, 0, 0))
    screen.blit(line7, (280, 700))

    pygame.display.flip()
