import store_ZHANG
import pygame,sys
import pickwords_ZHANG
from translate import Translator


pygame.init()
#create screen
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('English translate game')
screen.fill((135,206,250))
pygame.display.flip()

#create begin
pygame.init()
font1=pygame.font.SysFont('microsoftsansserif',40)
text1=font1.render('Get start(use your keyright)',True,(255,0,0),)
t1=pygame.transform.rotozoom(text1,360,0.5)
w,h = text1.get_size()
text2 = pygame.transform.rotozoom(text1,360,1)
screen.blit(text2,(70,300))
pygame.display.update()

#create back
pygame.init()
font3=pygame.font.SysFont('microsoftsansserif',40)
text3=font3.render('Get back(use your keyleft)',True,(255,0,0),)
t3=pygame.transform.rotozoom(text3,360,0.5)
w,h = text3.get_size()
text4= pygame.transform.rotozoom(text3,360,1)
screen.blit(text4,(70,400))
pygame.display.update()


while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
      print('Bye Bye')
      pygame.quit()
      sys.exit()
      pygame.display.update()
  if event.type== pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        print('Bye Bye')
        pygame.quit()
        sys.exit()
      elif event.key == pygame.K_RIGHT:
        print('Enjoyourself')
        pygame.quit()

        while True:
            name1=int(input('Which do u want choose:1.English to Chinese,2.Chinese to English:'))
            c=0
            b=0
            if name1==1:        
                 put1=input('Put a word: ')
                 put2=input('inputChinese: ')
                 translator = Translator(from_lang='English',to_lang='Chinese')
                 put3 = translator.translate(put1)
                 if put2 != put3 and put2!='?':
                     print('Wrong...if you press space you can give it up')
                     b+=1
                     print("Correct rate:",(int)(c/(b+c)*10000)/100,"%")
                     put2=input("Try again:")
                 if put2 == put3:
                     print('Well done')
                     name = store_ZHANG.a
                     score = str(int(store_ZHANG.num))
                     new_score = str(int(score) + 1)
                     combine1 = '{},{}'.format(name, score)
                     combine2 = '{},{}'.format(name, new_score)
                     store_ZHANG.changetext(combine1, combine2)
                     store_ZHANG.login(name)
                     c=c+1
                     print("Correct rate:",(int)(c/(b+c)*10000)/100,"%")
                 elif put2 == '?':
                     print('Correct answer is:',put3)
                     print("Correct rate:",(int)(c/(b+c)*10000)/100,"%")
                     sys.exit()
            if name1==2:   
                 put4=input('inputChinese: ')
                 put5=input('Put a  word: ')
                 translator = Translator(from_lang='Chinese',to_lang='English')
                 put6 = translator.translate(put4)
                 print('the correct answer is: ',put6)
                 if put5!=put6 and put5!='?':
                     print('Wrong...if you press space you can give it up')
                     b+=1
                     print("Correct rate:",(int)(c/(b+c)*10000)/100,"%")
                     put5=input("Try again:")
                 if put5==put6:
                     print('Well done')
                     name = store_ZHANG.a
                     score = str(int(store_ZHANG.num))
                     new_score = str(int(score) + 1)
                     combine1 = '{},{}'.format(name, score)
                     combine2 = '{},{}'.format(name, new_score)
                     store_ZHANG.changetext(combine1, combine2)
                     store_ZHANG.login(name)
                     c=c+1
                     print("Correct rate:",(int)(c/(b+c)*10000)/100,"%")
                     
                 elif put5 == '?':
                     print('Correct answer is:',put6)
                     print("Correct rate:",(int)(c/(b+c)*10000)/100,"%")
                     sys.exit()
