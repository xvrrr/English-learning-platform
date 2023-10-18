import pygame
import sys
import store_ZHANG
import submain

pygame.init()
screen1 = pygame.display.set_mode((600, 800))
pygame.display.set_caption('memoriE')
clock = pygame.time.Clock()
user_text = ''
base_font = pygame.font.Font(None, 32)
font0 = pygame.font.SysFont('Microsoft Ya Hei Ui', 80)
font1 = pygame.font.SysFont('Microsoft Ya Hei Ui', 25)
font2 = pygame.font.SysFont('Microsoft Ya Hei Ui', 26)

input_rect = pygame.Rect(160, 400, 100, 32)
color = (0, 0, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[: -1]
            else:
                user_text += event.unicode
            if event.key == pygame.K_RETURN:
                final_user = user_text[: -1]
                store_ZHANG.login(user_text[: -1])
                line0 = base_font.render("GL & HF, your score is {}".format(store_ZHANG.num[:-1]), True, (0, 0, 0))
                screen1.blit(line0, (160, 500))
                pygame.display.update()
                pygame.time.delay(1600)
                pygame.quit()
                submain.main()

    screen1.fill((255, 255, 255))
    pygame.draw.rect(screen1, color, input_rect, 2)
    text_surface = base_font.render(user_text, True, (0, 0, 0))
    screen1.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(20, text_surface.get_width() + 10)

    line1 = font0.render('memoriE', True, (0, 0, 0))
    screen1.blit(line1, (182, 200))
    line2 = font1.render("              Presented by G4-4", True, (0, 0, 255))
    screen1.blit(line2, (160, 300))
    line3 = base_font.render("User Name:", True, (0, 0, 0))
    screen1.blit(line3, (20, 405))
    line4 = font2.render("  Enter your name and press 'ENTER' to choose game", True, (0, 0, 0))
    screen1.blit(line4, (80, 600))
    pygame.display.flip()
    clock.tick(60)
