import pygame
from os import path
from setting import *
from classes import *

pygame.init()
pygame.mixer.init()
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "img")
snd_folder = path.join(game_folder, "snd")
intr_folder = path.join(game_folder, "interface")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ZomBalls!")
clock = pygame.time.Clock()

zomicon_img = pygame.image.load(path.join(img_folder, "ZomBallIcon.png")).convert_alpha()
control_img = pygame.image.load(path.join(img_folder, "Controls.png")).convert_alpha()
tips_img = pygame.image.load(path.join(img_folder, "Tips.png")).convert_alpha()
info_img = pygame.image.load(path.join(img_folder, "Info.png")).convert_alpha()
next_img = pygame.image.load(path.join(intr_folder, "Next.png")).convert_alpha()
next_img2 = pygame.image.load(path.join(intr_folder, "NextHover.png")).convert_alpha()
next_img3 = pygame.image.load(path.join(intr_folder, "NextClicked.png")).convert_alpha()
done_img = pygame.image.load(path.join(intr_folder, "Done.png")).convert_alpha()
done_img2 = pygame.image.load(path.join(intr_folder, "DoneHover.png")).convert_alpha()
done_img3 = pygame.image.load(path.join(intr_folder, "DoneClicked.png")).convert_alpha()
menu_img = pygame.image.load(path.join(img_folder, "MenuPage.png")).convert_alpha()
menu_img_rect = menu_img.get_rect()

pygame.display.set_icon(zomicon_img)

pygame.mixer.music.load(path.join(snd_folder, 'gamebgm.ogg'))
mhover_snd = pygame.mixer.Sound(path.join(intr_folder, 'buttonhoversound.wav'))
mclick_snd = pygame.mixer.Sound(path.join(intr_folder, 'buttonclickedsound.wav'))
exit_snd = pygame.mixer.Sound(path.join(intr_folder, 'exitsound.ogg'))

pygame.mixer.Sound.set_volume(exit_snd, 0.2)

class Start(pygame.sprite.Sprite):
    play1 = pygame.image.load(path.join(intr_folder, "Play.png")).convert_alpha()
    play2 = pygame.image.load(path.join(intr_folder, "PlayHover.png")).convert_alpha()
    play3 = pygame.image.load(path.join(intr_folder, "PlayClicked.png")).convert_alpha()
    x = 512
    y = 261
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Help(pygame.sprite.Sprite):
    help1 = pygame.image.load(path.join(intr_folder, "Help.png")).convert_alpha()
    help2 = pygame.image.load(path.join(intr_folder, "HelpHover.png")).convert_alpha()
    help3 = pygame.image.load(path.join(intr_folder, "HelpClicked.png")).convert_alpha()
    x = 261
    y = 439
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Exit(pygame.sprite.Sprite):
    exit1 = pygame.image.load(path.join(intr_folder, "Exit.png")).convert_alpha()
    exit2 = pygame.image.load(path.join(intr_folder, "ExitHover.png")).convert_alpha()
    exit3 = pygame.image.load(path.join(intr_folder, "ExitClicked.png")).convert_alpha()
    x = 761
    y = 439
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class MenuGame:
    def __init__(self):
        self.running = True
        self.enter_game = False
        self.inside_range = False
        self.inside_info = False
        self.inside_next = False
        self.next_range = False
        self.info_page = False
        self.info_page2 = False
        self.info_page3 = False
        self.info_page4 = False
        self.info_page5 = False
        self.done_light = False
        self.exit_info = False
        self.big_out = False
        self.soundhover = 0
    def Helppp(self):
        Ran = True
        next_range1 = False
        next_range2 = False
        next_range3 = False
        page1 = True
        page2 = False
        page3 = False
        presssnd = 0
        presssnd1 = 0
        while Ran:
            if page1:
                screen.blit(control_img, (177, 26))
                screen.blit(next_img, (878, 534))
            mouse = pygame.mouse.get_pos()
            RangeNext1 = 952 > mouse[0] > 878 and 609 > mouse[1] > 545
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and RangeNext1:
                    next_range1 = True
                    if page2:
                        next_range2 = True
                    if page3:
                        next_range3 = True
            leftclick1, middlemouse1, rightclick1 = pygame.mouse.get_pressed()
            if RangeNext1 and not leftclick1 and page1:
                screen.blit(next_img2, (878, 534))
            if leftclick1 and next_range1 and page1:
                screen.blit(next_img3, (878, 534))
            if not leftclick1 and next_range1:
                screen.blit(tips_img, (177, 26))
                screen.blit(next_img, (878, 534))
                page1 = False
                page2 = True
            if page2:
                presssnd += 1
                if presssnd == 1:
                    mclick_snd.play()
                if RangeNext1 and not leftclick1 and not page1:
                    screen.blit(next_img2, (878, 534))
                if leftclick1 and next_range2:
                    screen.blit(next_img3, (878, 534))
                if not leftclick1 and next_range2:
                    screen.blit(info_img, (177, 26))
                    screen.blit(done_img, (878, 534))
                    page2 = False
                    page3 = True
            if page3:
                presssnd1 += 1
                if presssnd1 == 1:
                    mclick_snd.play()
                if RangeNext1 and not leftclick1 and not page2:
                    screen.blit(done_img2, (878, 534))
                    if self.soundhover == 1:
                        mhover_snd.play()
                if leftclick1 and next_range3:
                    screen.blit(done_img3, (878, 534))
                if not leftclick1 and next_range3:
                    mclick_snd.play()
                    page3 = False
                    Ran = False
            pygame.display.update()
    def Menuing(self):
        pygame.mixer.music.play(loops=-1)
        while self.running:
            screen.blit(menu_img, menu_img_rect)
            screen.blit(Start.play1, (Start.x, Start.y))
            screen.blit(Help.help1, (Help.x, Help.y))
            screen.blit(Exit.exit1, (Exit.x, Exit.y))
            mouse = pygame.mouse.get_pos()
            RR = []
            RangeStart = 688 > mouse[0] > 512 and 439 > mouse[1] > 261
            RangeHelp = 437 > mouse[0] > 261 and 618 > mouse[1] > 439
            RangeExit = 937 > mouse[0] > 761 and 617 > mouse[1] > 439
            RangeNext = 952 > mouse[0] > 878 and 609 > mouse[1] > 545
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and RangeStart or event.type == pygame.MOUSEBUTTONDOWN and RangeHelp or event.type == pygame.MOUSEBUTTONDOWN and RangeExit:
                    self.inside_range = True
                if event.type == pygame.MOUSEBUTTONDOWN and RangeNext:
                    self.next_range = True
            leftclick, middlemouse, rightclick = pygame.mouse.get_pressed()
            if RangeStart and not self.inside_info and not self.inside_next:
                self.soundhover += 1
                screen.blit(Start.play2, (Start.x, Start.y))
                if leftclick and self.inside_range:
                    screen.blit(Start.play3, (Start.x, Start.y))
                    self.enter_game = True
                if leftclick == 0 and self.enter_game and self.running:
                    mclick_snd.play()
                    self.enter_game = False
                    PLAY = Game(screen)
                    Restart = PLAY.run()
                    while Restart == 1:
                        RR.append(Game(screen))
                        Restart = RR[-1].run()
                if self.soundhover == 1:
                    mhover_snd.play()
            if RangeHelp and not self.inside_info and not self.info_page:
                self.soundhover += 1
                screen.blit(Help.help2, (Help.x, Help.y))
                if leftclick and self.inside_range:
                    screen.blit(Help.help3, (Help.x, Help.y))
                    self.enter_game = True
                if leftclick == 0 and self.enter_game and self.running:
                    mclick_snd.play()
                    self.Helppp()
                    self.inside_next = False
                    self.inside_range = False
                    self.enter_game = False
                if self.soundhover == 1:
                    mhover_snd.play()
            if RangeExit and not self.inside_info and not self.inside_next:
                self.soundhover += 1
                screen.blit(Exit.exit2, (Exit.x, Exit.y))
                if leftclick and self.inside_range:
                    screen.blit(Exit.exit3, (Exit.x, Exit.y))
                    self.enter_game = True
                    exit_snd.play()
                if leftclick == 0 and self.enter_game and self.running:
                    self.running = False
                    self.enter_game = False
                if self.soundhover == 1:
                    mhover_snd.play()
            if not RangeHelp and not RangeStart and not RangeExit and not self.inside_info and not self.inside_next:
                self.enter_game = False
                self.inside_range = False
                self.soundhover = 0
            pygame.display.flip()




