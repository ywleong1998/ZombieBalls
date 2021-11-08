import pygame
import random
import math
from os import path
from setting import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("ZombieBalls")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Path folders
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "img")
snd_folder = path.join(game_folder, "snd")
intr_folder = path.join(game_folder, "interface")
zom1_folder = path.join(game_folder, "zombie1")
zom2_folder = path.join(game_folder, "zombie2")
zom3_folder = path.join(game_folder, "zombie3")

allyhp_img = pygame.image.load(path.join(img_folder, 'Basehpbar.png')).convert_alpha()
powerbar_img = pygame.image.load(path.join(img_folder, 'PowerBar.png')).convert_alpha()
pause_img = pygame.image.load(path.join(intr_folder, 'pausemenu.png')).convert_alpha()
pause_resume1 = pygame.image.load(path.join(intr_folder, 'PauseResume1.png')).convert_alpha()
pause_resume2 = pygame.image.load(path.join(intr_folder, 'PauseResume2.png')).convert_alpha()
pause_resume3 = pygame.image.load(path.join(intr_folder, 'PauseResume3.png')).convert_alpha()
pause_help1 = pygame.image.load(path.join(intr_folder, 'PauseHelp1.png')).convert_alpha()
pause_help2 = pygame.image.load(path.join(intr_folder, 'PauseHelp2.png')).convert_alpha()
pause_help3 = pygame.image.load(path.join(intr_folder, 'PauseHelp3.png')).convert_alpha()
pause_exit1 = pygame.image.load(path.join(intr_folder, 'PauseExit1.png')).convert_alpha()
pause_exit2 = pygame.image.load(path.join(intr_folder, 'PauseExit2.png')).convert_alpha()
pause_exit3 = pygame.image.load(path.join(intr_folder, 'PauseExit3.png')).convert_alpha()
bg = pygame.image.load(path.join(img_folder, 'backyard.jpg')).convert_alpha()
ball_img = pygame.image.load(path.join(img_folder, "ball1.png")).convert_alpha()
box_img = pygame.image.load(path.join(img_folder, "box.png")).convert_alpha()
castle_img = pygame.image.load(path.join(img_folder, "castle.png")).convert_alpha()
zom_walk = [pygame.image.load(path.join(zom1_folder, 'go_%s.png' % frame)).convert_alpha() for frame in range(1, 11)]
zom2_walk = [pygame.image.load(path.join(zom2_folder, '2go_%s.png' % frame)).convert_alpha() for frame in range(1, 17)]
zom3_walk = [pygame.image.load(path.join(zom3_folder, '3go_%s.png' % frame)).convert_alpha() for frame in range(1, 17)]
gos_img = pygame.image.load(path.join(img_folder, 'GAME-OVER.png')).convert_alpha()
win_img = pygame.image.load(path.join(img_folder, 'YOU-WIN.png')).convert_alpha()
wave_img = pygame.image.load(path.join(img_folder, 'WAVE-CLEARED.png')).convert_alpha()

charging_snd = pygame.mixer.Sound(path.join(snd_folder, 'charging.ogg'))
decrease_snd = pygame.mixer.Sound(path.join(snd_folder, 'decrease.ogg'))
fire_snd = pygame.mixer.Sound(path.join(snd_folder, 'fire.ogg'))
hitcastle_snd = pygame.mixer.Sound(path.join(snd_folder, 'hitcastle.ogg'))
mhover_snd = pygame.mixer.Sound(path.join(intr_folder, 'buttonhoversound.wav'))
mclick_snd = pygame.mixer.Sound(path.join(intr_folder, 'buttonclickedsound.wav'))
pause_snd = pygame.mixer.Sound(path.join(intr_folder, 'pauseappear.ogg'))
box1_snd = pygame.mixer.Sound(path.join(snd_folder, 'boxdestory1.ogg'))
box2_snd = pygame.mixer.Sound(path.join(snd_folder, 'boxdestory2.ogg'))
castle_snd = pygame.mixer.Sound(path.join(snd_folder, 'baselose.ogg'))
exit_snd = pygame.mixer.Sound(path.join(intr_folder, 'exitsound.ogg'))
waveclr_snd = pygame.mixer.Sound(path.join(snd_folder, 'waveclearedsnd.ogg'))
gameover_snd = pygame.mixer.Sound(path.join(snd_folder, 'gameoversnd.ogg'))
finalwin_snd = pygame.mixer.Sound(path.join(snd_folder, 'finalwin.ogg'))
groan_snd = pygame.mixer.Sound(path.join(snd_folder, 'groan.ogg'))

# Zombies sound effects
zom1_spawn = pygame.mixer.Sound(path.join(zom1_folder, 'zomb1.ogg'))
zom1_atk = pygame.mixer.Sound(path.join(zom1_folder, 'zomb1atk.ogg'))
zom1_die = pygame.mixer.Sound(path.join(zom1_folder, 'zomb1die.ogg'))
zom1_hit = pygame.mixer.Sound(path.join(zom1_folder, 'zomb1hit.ogg'))
zom2_spawn = pygame.mixer.Sound(path.join(zom2_folder, 'zomb2.ogg'))
zom2_atk = pygame.mixer.Sound(path.join(zom2_folder, 'zomb2atk.ogg'))
zom2_die = pygame.mixer.Sound(path.join(zom2_folder, 'zomb2die.ogg'))
zom3_spawn = pygame.mixer.Sound(path.join(zom3_folder, 'zomb3.ogg'))
zom3_atk = pygame.mixer.Sound(path.join(zom3_folder, 'zomb3atk.ogg'))
zom3_die = pygame.mixer.Sound(path.join(zom3_folder, 'zomb3die.ogg'))
zom3_hit = pygame.mixer.Sound(path.join(zom3_folder, 'zomb3hit.ogg'))

pygame.mixer.Sound.set_volume(fire_snd, 0.5)
pygame.mixer.Sound.set_volume(zom1_atk, 0.25)
pygame.mixer.Sound.set_volume(zom1_die, 0.4)
pygame.mixer.Sound.set_volume(zom2_atk, 0.3)
pygame.mixer.Sound.set_volume(zom2_die, 0.6)
pygame.mixer.Sound.set_volume(zom3_die, 0.35)
pygame.mixer.Sound.set_volume(exit_snd, 0.2)
pygame.mixer.music.load(path.join(snd_folder, 'gamebgm.ogg'))
pygame.mixer.music.set_volume(0.15)

# Fonts
font_name = pygame.font.match_font('DeterminationMonoWeb')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('DeterminationMonoWeb.ttf', size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def pause():
    inside_range2 = False
    paused = True
    button1 = False
    enter_game2 = False
    inside_info2 = False
    decision = 0
    sound = 0
    psound = 0
    while paused:
        screen.blit(pause_img, (356, 20))
        psound += 1
        if psound == 1:
            pause_snd.play()
        mouse = pygame.mouse.get_pos()
        RangeResume = 706 > mouse[0] > 494 and 263 > mouse[1] > 160
        RangeHelp2 = 706 > mouse[0] > 494 and 398 > mouse[1] > 295
        RangeExit2 = 706 > mouse[0] > 494 and 532 > mouse[1] > 429
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and RangeResume or event.type == pygame.MOUSEBUTTONDOWN and RangeHelp2 or event.type == pygame.MOUSEBUTTONDOWN and RangeExit2:
                inside_range2 = True
        mouse1, mouse2, mouse3 = pygame.mouse.get_pressed()
        if RangeResume and not inside_info2 and not button1:
            screen.blit(pause_resume2, (494, 160))
            sound += 1
            if sound == 1:
                mhover_snd.play()
            if mouse1 and inside_range2:
                screen.blit(pause_resume3, (494, 160))
                enter_game2 = True
            if not mouse1 and enter_game2:
                paused = False
                enter_game2 = False
                mclick_snd.play()
                pause_snd.play()
        if RangeHelp2 and not inside_info2:
            screen.blit(pause_help2, (494, 295))
            sound += 1
            if sound == 1:
                mhover_snd.play()
            if mouse1 and inside_range2:
                screen.blit(pause_help3, (494, 295))
                enter_game2 = True
            if not mouse1 and enter_game2:
                mclick_snd.play()
                decision = 2
                break
        if RangeExit2 and not inside_info2:
            screen.blit(pause_exit2, (494, 429))
            sound += 1
            if sound == 1:
                mhover_snd.play()
            if mouse1 and inside_range2:
                screen.blit(pause_exit3, (494, 429))
                enter_game2 = True
                exit_snd.play()
            if not mouse1 and enter_game2:
                pygame.quit()
                quit()
        if not RangeResume and not RangeHelp2 and not RangeExit2 and not inside_info2:
            sound = 0
            enter_game2 = False
            inside_range2 = False
        pygame.display.update()
    return decision

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 35
        self.y = 550
        self.image = pygame.transform.scale(ball_img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x + 30//2, self.y + 30//2)
        self.y_speed = 5
        self.shoot = False
        self.charging = False
        self.charge = 0
        self.firstclick = False
        self.decreasepower = False
        self.increasepower = False
        self.angle = 0
        self.power = 0
        self.time = 0
        self.startShoot = False
        self.hp = 1
    def deducthp(self):
        self.hp -= 1
        self.shoot = False
    def findAngle(self, pos):
        sX = self.x
        sY = self.y
        try:
            angle = math.atan((sY - pos[1]) / (sX - pos[0]))
        except:
            angle = math.pi / 2
        if pos[1] < sY and pos[0] > sX:
            angle = abs(angle)
        elif pos[1] < sY and pos[0] < sX:
            angle = math.pi - angle
        elif pos[1] > sY and pos[0] < sX:
            angle = math.pi + abs(angle)
        elif pos[1] > sY and pos[0] > sX:
            angle = (math.pi * 2) - angle
        return angle
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse_buttons = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if mouse_buttons[0] and self.rect.x == 35 and self.rect.y == 550:
            self.charging = True
            self.increasepower = True
            if self.increasepower:
                if self.power == 0:
                    charging_snd.play()
            self.firstclick = True
            if self.increasepower:
                self.power += 1
                if self.power >= 100:
                    self.increasepower = False
                    self.decreasepower = True
            if self.decreasepower:
                if self.power == 100:
                    decrease_snd.play()
                self.power -= 2
                if self.power <= 0:
                    self.increasepower = True
                    self.decreasepower = False
        if not mouse_buttons[0] and self.charging:
            fire_snd.play()
            self.angle = self.findAngle(pos)
            self.shoot = True
            self.decreasepower = False
            self.increasepower = False
            self.time = 0
            self.firstclick = False
            self.charging = False
        if self.startShoot:
            self.rect.x = self.x
            self.rect.y = self.y
            self.power = 0
            self.time = 0
            self.startShoot = False
        if self.shoot:
            self.charge = 0
            if self.rect.y < 600:
                self.time += 0.15
                velox = math.cos(self.angle) * self.power
                veloy = math.sin(self.angle) * self.power
                distX = velox * self.time
                distY = (veloy * self.time) + ((-4.9 * (self.time) ** 2) / 2)
                newx = round(distX + self.x)
                newy = round(self.y - distY)
                self.rect.x = newx
                self.rect.y = newy
                if self.rect.x < - 50 or self.rect.x > WIDTH + 100 or self.rect.y < -500:
                    self.shoot = False
                    self.rect.x = self.x
                    self.rect.y = self.y
                    self.power = 0
                    self.time = 0
            else:
                self.shoot = False
                self.rect.x = self.x
                self.rect.y = self.y
                self.power = 0
                self.time = 0
        power1 = self.power*4.5
        if power1 > 0:
            pygame.draw.rect(screen, (0+self.power*2.12, 255-self.power*2.12 ,0), (154, 647, power1, 21))
        screen.blit(powerbar_img, (110, 642))
class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = box_img
        self.x = WIDTH/2
        self.y = 555
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.hpbar = 200
        self.broken = False
    def health(self):
        return self.hpbar
    def damaged(self):
        self.hpbar -= 10
    def destroyed(self):
        self.broken = True
    def recreate(self):
        self.hpbar = 200
        self.broken = False
    def update(self):
        pygame.draw.rect(screen, GREEN, (self.x - 38, self.rect.y - 30, (self.hpbar*3/8), 15))
        pygame.draw.rect(screen, WHITE, (self.x - 38, self.rect.y - 30, 75, 15), 2)
        if self.hpbar <= 0:
            box1_snd.play()
            self.broken = True
            self.kill()
            Game.score -= 250
class Box2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = box_img
        self.x = WIDTH/2+250
        self.y = 555
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.hpbar = 200
        self.broken = False
    def health(self):
        return self.hpbar
    def damaged(self):
        self.hpbar -= 10
    def recreate(self):
        self.hpbar = 200
        self.broken = False
    def destroyed(self):
        self.broken = True
    def update(self):
        pygame.draw.rect(screen, GREEN, (self.x - 38, self.rect.y - 30, (self.hpbar*3/8), 15))
        pygame.draw.rect(screen, WHITE, (self.x - 38, self.rect.y - 30, 75, 15), 2)
        if self.hpbar <= 0:
            box2_snd.play()
            self.broken = True
            self.kill()
            Game.score -= 250
class Base(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = castle_img
        self.x = 285
        self.y = 500
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.hpbar = 500
        self.broken = False
    def health(self):
        return self.hpbar
    def damaged(self):
        self.hpbar -= 12
    def recreate(self):
        self.hpbar = 500
        self.broken = False
    def destroyed(self):
        self.broken = True
    def update(self):
        screen.blit(allyhp_img, (self.x - 100, self.rect.y - 40))
        pygame.draw.rect(screen, GREEN, (self.x - 86, self.rect.y - 40, (self.hpbar*185/500), 17))
        if self.hpbar <= 0:
            castle_snd.play()
            self.broken = True
            self.kill()
class Mob(pygame.sprite.Sprite):
    zom_walk = [pygame.image.load(path.join(zom1_folder, 'go_%s.png' % frame)).convert_alpha() for frame in range(1, 11)]
    zom_die = [pygame.image.load(path.join(zom1_folder, 'die_%s.png' % frame)).convert_alpha() for frame in range(1, 9)]
    zom_atk = [pygame.image.load(path.join(zom1_folder, 'hit_%s.png' % frame)).convert_alpha() for frame in range(0, 9)]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = zom_walk[0]
        self.x = random.randrange(1250, 1400)
        self.y = 530
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.hpbar = 2
        self.Dead = False
        self.Attack = False
        self.Walk = True
        self.attacking_barricade = False
        self.attacking_barricade2 = False
        self.attacking_base = False
        self.frame = 0
        self.die_frame = 0
        self.attack_frame = 0
        self.walk_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def die_animation(self):
        now = pygame.time.get_ticks()
        self.Walk = False
        self.Attack = False
        zom1_die.play()
        if self.die_frame < 8:
            self.image = self.zom_die[self.die_frame]
            if now - self.last_update > self.frame_rate:
                self.last_update = now -50
                self.die_frame += 1
        else:
            self.kill()
            self.die_frame = 0
            Game.score += 100
    def attack_animation(self):
        if self.Attack:
            now = pygame.time.get_ticks()
            if self.attack_frame == 0:
                zom1_atk.play()
            if self.attack_frame < 9:
                self.image = self.zom_atk[self.attack_frame]
                if now - self.last_update > self.frame_rate:
                    self.last_update = now
                    self.attack_frame += 1
            else:
                if now - self.last_update > 800:
                    self.attack_frame = 0
                    if self.attacking_barricade:
                        Game.barricade.damaged()
                    if self.attacking_barricade2:
                        Game.barricade2.damaged()
                    if self.attacking_base:
                        Game.Cs.damaged()
    def dying(self):
        self.Dead = True
    def attackingBox(self):
        self.Attack = True
        self.Walk = False
        self.attacking_barricade = True
        self.attacking_barricade2 = False
    def attackingBox2(self):
        self.Attack = True
        self.Walk = False
        self.attacking_barricade = False
        self.attacking_barricade2 = True
    def attackingBase(self):
        self.Attack = True
        self.Walk = False
        self.attacking_base = True
    def walking(self):
        self.Attack = False
        self.Walk = True
        self.attacking_barricade = False
        self.attacking_barricade2 = False
        self.attacking_base = False
    def health(self):
        return self.hpbar
    def damage(self):
        self.hpbar -=1
        zom1_hit.play()
    def update(self):
        now = pygame.time.get_ticks()
        pygame.draw.rect(screen, RED, (self.rect.x + 15, self.rect.y - 35, self.hpbar*50, 22))
        pygame.draw.rect(screen, WHITE, (self.rect.x + 15, self.rect.y - 35, 100, 22),2)
        if self.Attack:
            self.vx = 0
            self.attack_animation()
        if self.Dead:
            self.die_animation()
        if self.Walk:
            if self.rect.x > 0:
                self.vx = 1
                if now - self.walk_frame > 40:
                    self.rect.x -= self.vx
                    self.walk_frame = now
            if now - self.last_update > 125:
                if self.frame < 10:
                    self.image = self.zom_walk[self.frame]
                    if now - self.last_update > self.frame_rate:
                        self.last_update = now
                        self.frame += 1
                else:
                    self.frame = 0
                    self.walking()
class Mob2(pygame.sprite.Sprite):
    zom2_walk = [pygame.image.load(path.join(zom2_folder, '2go_%s.png' % frame)).convert_alpha() for frame in range(1, 17)]
    zom2_die = [pygame.image.load(path.join(zom2_folder, '2die_%s.png' % frame)).convert_alpha() for frame in range(1, 21)]
    zom2_atk = [pygame.image.load(path.join(zom2_folder, '2hit_%s.png' % frame)).convert_alpha() for frame in range(1, 21)]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = zom2_walk[0]
        self.x = random.randrange (1250, 1500)
        self.y = 545
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.hpbar = 1
        self.Dead = False
        self.Attack = False
        self.Walk = True
        self.attacking_barricade = False
        self.attacking_barricade2 = False
        self.attacking_base = False
        self.frame = 0
        self.die_frame = 0
        self.attack_frame = 0
        self.walk_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def die_animation(self):
        now = pygame.time.get_ticks()
        self.Attack = False
        self.Walk = False
        zom2_die.play()
        if self.die_frame < 19:
            self.image = self.zom2_die[self.die_frame]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.die_frame += 1

        else:
            self.kill()
            self.die_frame = 0
            Game.score += 100
    def attack_animation(self):
        if self.Attack:
            now = pygame.time.get_ticks()
            if self.attack_frame == 0:
                zom2_atk.play()
            if self.attack_frame < 20:
                self.image = self.zom2_atk[self.attack_frame]
                if now - self.last_update > 120:
                    self.last_update = now
                    self.attack_frame += 1
            else:
                self.attack_frame = 0
                if self.attacking_barricade:
                    Game.barricade.damaged()
                if self.attacking_barricade2:
                    Game.barricade2.damaged()
                if self.attacking_base:
                    Game.Cs.damaged()
                self.walking()
    def dying(self):
        self.Dead = True
    def attackingBox(self):
        self.Attack = True
        self.Walk = False
        self.attacking_barricade = True
        self.attacking_barricade2 = False
    def attackingBox2(self):
        self.Attack = True
        self.Walk = False
        self.attacking_barricade = False
        self.attacking_barricade2 = True
    def attackingBase(self):
        self.Attack = True
        self.Walk = False
        self.attacking_base = True
    def walking(self):
        self.Attack = False
        self.Walk = True
        self.attacking_barricade = False
        self.attacking_barricade2 = False
        self.attacking_base = False
    def health(self):
        return self.hpbar
    def damage(self):
        self.hpbar -=1
    def update(self):
        now = pygame.time.get_ticks()
        pygame.draw.rect(screen, RED, (self.rect.x + 15, self.rect.y - 35, self.hpbar*50, 20))
        pygame.draw.rect(screen, WHITE, (self.rect.x + 15, self.rect.y - 35, 50, 20), 2)
        if self.Attack:
            self.vx = 0
            self.attack_animation()
        if self.Dead:
            self.die_animation()
        if self.Walk:
            if self.rect.x > 0:
                self.vx = 2
                if now - self.walk_frame > 45:
                    self.rect.x -= self.vx
                    self.walk_frame = now
            if now - self.last_update > 100:
                if self.frame < 16:
                    self.image = self.zom2_walk[self.frame]
                    if now - self.last_update > self.frame_rate:
                        self.last_update = now
                        self.frame += 1
                else:
                    self.frame = 0
                    self.walking()
class Mob3(pygame.sprite.Sprite):
    zom3_walk = [pygame.image.load(path.join(zom3_folder, '3go_%s.png' % frame)).convert_alpha() for frame in range(1, 17)]
    zom3_die = [pygame.image.load(path.join(zom3_folder, '3die_%s.png' % frame)).convert_alpha() for frame in range(1, 21)]
    zom3_atk = [pygame.image.load(path.join(zom3_folder, '3hit_%s.png' % frame)).convert_alpha() for frame in range(1, 17)]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = zom3_walk[0]
        self.x = random.randrange(WIDTH + 100, WIDTH + 200)
        self.y = 500
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.hpbar = 15
        self.Dead = False
        self.Attack = False
        self.Walk = True
        self.attacking_barricade = False
        self.attacking_barricade2 = False
        self.attacking_base = False
        self.frame = 0
        self.die_frame = 0
        self.attack_frame = 0
        self.walk_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def die_animation(self):
        now = pygame.time.get_ticks()
        self.Walk = False
        zom3_die.play()
        if self.die_frame < 20:
            self.image = self.zom3_die[self.die_frame]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.die_frame += 1
        else:
            self.kill()
            Game.score += 1000
            self.die_frame = 0
    def attack_animation(self):
        if self.Attack:
            now = pygame.time.get_ticks()
            if self.attack_frame == 0:
                zom3_atk.play()
            if self.attack_frame < 16:
                self.image = self.zom3_atk[self.attack_frame]
                if now - self.last_update > 150:
                    if self.attacking_barricade:
                        Game.barricade.damaged()
                    if self.attacking_barricade2:
                        Game.barricade2.damaged()
                    if self.attacking_base:
                        Game.Cs.damaged()
                    self.last_update = now
                    self.attack_frame += 1
            else:
                self.attack_frame = 0
                self.walking()
    def dying(self):
        self.Dead = True
    def attackingBox(self):
        self.Attack = True
        self.Walk = False
        self.attacking_barricade = True
        self.attacking_barricade2 = False
    def attackingBox2(self):
        self.Attack = True
        self.Walk = False
        self.attacking_barricade = False
        self.attacking_barricade2 = True
    def attackingBase(self):
        self.Attack = True
        self.Walk = False
        self.attacking_base = True
    def walking(self):
        self.Attack = False
        self.Walk = True
        self.attacking_barricade = False
        self.attacking_barricade2 = False
        self.attacking_base = False
    def health(self):
        return self.hpbar
    def damage(self):
        self.hpbar -=1
        zom3_hit.play()
    def update(self):
        now = pygame.time.get_ticks()
        pygame.draw.rect(screen, RED, (self.rect.x + 30, self.rect.y - 70, self.hpbar*200/15, 30))
        pygame.draw.rect(screen, WHITE, (self.rect.x + 30, self.rect.y - 70, 200, 30), 2)
        if self.Attack:
            self.vx = 0
            self.attack_animation()
        if self.Dead:
            self.die_animation()
        if self.Walk:
            if self.rect.x > 0:
                self.vx = 1
                if now - self.walk_frame > 130:
                    self.rect.x -= self.vx
                    self.walk_frame = now
            if now - self.last_update > 100:
                if self.frame < 16:
                    self.image = self.zom3_walk[self.frame]
                    if now - self.last_update > self.frame_rate:
                        self.last_update = now
                        self.frame += 1
                else:
                    self.frame = 0
                    self.walking()

class Game():
    score = 0
    wave = 1
    barricade = Box()
    barricade2 = Box2()
    Cs = Base()
    def __init__(self, scr):
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group() 
        self.castle = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(Game.Cs)
        self.castle.add(Game.Cs)
        self.play = False
        self.all_sprites.add(self.player, self.mobs, Game.barricade, Game.barricade2, self.castle)
        self.wavecleared = False
        self.counter = 0
        self.COUNTER = 0
        self.running = True
        self.endless = 0
        self.endless1 = 0
        self.endless2 = 0
        self.endless3 = 0
        self.endless0 = 2000
        self.endless00 = 5000
        self.endless000 = 10000
        self.groan1 = 0
        self.groan2 = 0
        self.groan3 = 0
        self.groan4 = 0
        self.start = pygame.time.get_ticks()
        self.screen = scr
        self.clock1 = pygame.time.Clock()
        self.clock2 = pygame.time.Clock()
        self.clock3 = pygame.time.Clock()
    def GameOverScreen(self):
        gameover_snd.play()
        self.screen.blit(bg, (0, 0))
        self.screen.blit(gos_img, (205, 178))
        draw_text(self.screen, "Score: " +str(Game.score), 50, WIDTH/2, 450)
        pygame.display.update()
        finaldec = self.wait_for_key()
        return finaldec
    def wait_for_key(self):
        waiting = True
        decide = 0
        waveclr = 0
        while waiting:
            self.clock.tick(FPS)
            if self.wavecleared:
                waveclr += 1
                if waveclr == 1:
                    waveclr_snd.play()
                self.screen.blit(wave_img, (280, 257))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting = False
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            waiting = False
                            self.wavecleared = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        decide = 1
                        waiting = False
                        break
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        decide = 2
                        waiting = False
                        break
        return decide
    def VictoryScreen(self):
        finalwin_snd.play()
        Game.wave = 4
        self.screen.blit(bg, (0,0))
        self.screen.blit(win_img, (255, 242))
        draw_text(self.screen, "Score: " + str(Game.score), 50, WIDTH/2, 475)
        pygame.display.update()
        finaldec = self.wait_for_key()
        return finaldec
    def newmob(self):
        zombie = Mob()
        self.all_sprites.add(zombie)
        self.mobs.add(zombie)
        zom1_spawn.play()
    def newmob2(self):
        zombie2 = Mob2()
        self.all_sprites.add(zombie2)
        self.mobs.add(zombie2)
        zom2_spawn.play()
    def newmob3(self):
        zombie3 = Mob3()
        self.all_sprites.add(zombie3)
        self.mobs.add(zombie3)
        zom3_spawn.play()
    # Game loop
    def run(self):
        pygame.mixer.music.fadeout(750)
        pygame.mixer.music.play(loops = -1)
        final = 0
        previous_key = pygame.key.get_pressed()
        while self.running:
            clock = pygame.time.Clock()
            time = pygame.time.get_ticks()
            time1 = pygame.time.get_ticks()
            time2 = pygame.time.get_ticks()
            time3 = pygame.time.get_ticks()
            self.clock.tick(FPS)
            if Game.wave == 1 or Game.wave == 2:
                if time - self.start > 6000:
                    if self.COUNTER < 4 and Game.wave == 1:
                        snd1 = pygame.time.get_ticks()
                        if snd1 - self.groan1 > 5000 + random.choice([-2000, -1000, -500, 0, 500, 1000, 2000]):
                            groan_snd.play()
                            self.groan1 = snd1
                        self.newmob()
                        self.counter += 1
                        self.COUNTER += 1
                    if self.COUNTER == 4 and self.counter == 0 and Game.wave == 1:
                        Game.wave = 2
                        self.wavecleared = True
                        self.COUNTER = 0
                        duration = time
                        Game.score += round(Game.barricade2.health()*1 + Game.barricade.health()*0.75 + Game.Cs.health()*0.6 + (-duration/1000 + time/100))
                        self.wait_for_key()
                    if self.COUNTER < 4 and Game.wave == 2:
                        snd2 = pygame.time.get_ticks()
                        if snd2 - self.groan2 > 5000 + random.choice([-2000, -1000, -500, 0, 500, 1000, 2000]):
                            groan_snd.play()
                            self.groan2 = snd2
                        self.newmob()
                        self.newmob2()
                        self.counter += 1
                        self.COUNTER += 1
                    if self.COUNTER == 4 and self.counter == -4 and Game.wave == 2:
                        Game.wave = 3
                        self.wavecleared = True
                        self.COUNTER = 0
                        self.counter = 0
                        duration2 = duration
                        Game.score += round(Game.barricade2.health() * 1.5 + Game.barricade.health() * 1.1 + Game.Cs.health() * 0.95 + (-(time - duration2)/2000 + time/100))
                        self.wait_for_key()
                    self.start += 6000
            if Game.wave == 3:
                snd3 = pygame.time.get_ticks()
                if snd3 - self.groan1 > 5000 + random.choice([-2000, -1000, -500, 0, 500, 1000, 2000]):
                    groan_snd.play()
                    self.groan1 = snd3
                if self.COUNTER == 0 and self.counter == 0:
                    self.newmob3()
                    self.newmob2()
                    self.newmob()
                    self.COUNTER += 1
                if time - self.start > 7500:
                    if self.COUNTER <= 4 and self.counter < 4:
                        self.newmob2()
                        self.newmob()
                        self.counter += 2
                        self.COUNTER += 1
                    self.start += 12500
                    if self.counter == -3 and self.COUNTER == 5:
                        Game.score += round(Game.barricade2.health() * 3 + Game.barricade.health() * 3 + Game.Cs.health() * 2.5 + 1000)
                        self.VictoryScreen()
            if Game.wave == 4:
                snd4 = pygame.time.get_ticks()
                if snd4 - self.groan1 > 5000 + random.choice([-1000, -500, 0, 500, 1000]):
                    groan_snd.play()
                    self.groan1 = snd4
                if time - self.endless > 100:
                    Game.score += 1
                now1 = pygame.time.get_ticks()
                if now1 - self.endless > 12500 + random.choice([-1000, -500, 0, 2000, 3500]):
                    self.newmob()
                    self.endless = now1
                now2 = pygame.time.get_ticks()
                if now2 - self.endless0 > 22000 + random.choice([-2000, -1000, 0, 1500, 2500]):
                    self.newmob2()
                    self.endless0 = now2
                now3 = pygame.time.get_ticks()
                if now3 - self.endless00 > 45000 + random.choice([-2500, -1000, 0, 2500, 5500]):
                    self.newmob3()
                    self.endless00 = now3

            # Process input (events)
            pygame.event.pump()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE] and not previous_key[pygame.K_ESCAPE]:
                STOP = pause()
                if STOP == 2:
                    self.running = False
            # Draw / render
            self.screen.blit(bg, (0,0))
            if Game.wave <= 3:
                draw_text(self.screen, "Current score: " + str(Game.score), 40, WIDTH / 2 - 50, 10)
                draw_text(self.screen, "Wave: " + str(Game.wave), 30, 80, 10)
            if Game.wave == 4:
                draw_text(self.screen, "Current score: " + str(Game.score), 40, WIDTH / 2 + 20, 10)
                draw_text(self.screen, "Wave : Endless Mode", 30, 150, 10)
            # Update
            if Game.Cs.health() <= 0:
                final = self.GameOverScreen()
                break
            self.all_sprites.update()
            for ffire in pygame.sprite.spritecollide(self.player, self.castle, False, pygame.sprite.collide_mask):
                hitcastle_snd.play()
                self.player.shoot = False
                self.player.startShoot = True
                Game.score -= 200
            for zomb in pygame.sprite.spritecollide(self.player, self.mobs, False):
                self.player.shoot = False
                self.player.startShoot = True
                Game.score += 50
                zomb.damage()
                if zomb.health() <= 0:
                    zomb.dying()
                    self.counter -= 1
            for zombatk in pygame.sprite.spritecollide(Game.barricade, self.mobs, False):
                if zombatk.health() > 0:
                    zombatk.attackingBox()
                if Game.barricade.health() <= 0:
                    Game.barricade.destroyed()
                    zombatk.walking()
            for zombatk2 in pygame.sprite.spritecollide(Game.barricade2, self.mobs, False):
                if zombatk2.health() > 0:
                    zombatk2.attackingBox2()
                if Game.barricade2.health() <= 0:
                    Game.barricade2.destroyed()
                    zombatk2.walking()
            for zombase in pygame.sprite.groupcollide(self.mobs, self.castle, False, False):
                if zombase.health() > 0:
                    zombase.attackingBase()
            for basezomb in pygame.sprite.groupcollide(self.castle, self.mobs, False, False):
                if basezomb.health() <= 0:
                    basezomb.damaged()
            self.all_sprites.draw(self.screen)
            pygame.event.pump()
            key = pygame.key.get_pressed()
            if key[pygame.K_0]:
                Game.Cs.damaged()
            if key[pygame.K_9] and key[pygame.K_8]:
                self.VictoryScreen()
            pygame.display.flip()
        Game.Cs.recreate()
        Game.barricade.recreate()
        Game.barricade2.recreate()
        Game.score = 0
        Game.wave = 1
        return final