# Импортируем нежные библиотеки
import pygame, os
from pygame import *
from player import *


#Объявляем переменные
screen_weight = 400 #Ширина  окна
screen_height = 600 # Высота окна
size = (screen_weight, screen_height) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#ffffff"

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 35
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__)


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/data/platform.png" % ICON_DIR)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
        
        
def camera_configure(camera, target_rect):
    global screen_weight, screen_height
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+screen_weight / 2, -t+screen_height / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-screen_weight), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-screen_height), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return Rect(l, t, w, h)        


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    #image = image.convert_alpha()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

level = 0

def start_screen():
    global level
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    intro_text = [" ", " ", " "," ", " ", " "," ",
                 "< - easy",
                  "> - hurd"
                  ]

    fon = pygame.transform.scale(load_image('fon.jpg'), (400, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 2, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()



def main():
    global level

    pygame.init() # Инициация PyGame, обязательная строчка  # Создаем окошко
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Doodle Jump") # Пишем в шапку
    bg = Surface((400,600)) # Создание видимой поверхности
                                         # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом
    
    hero = Player(55,55) # создаем героя по (x,y) координатам
    left = right = False # по умолчанию - стоим
    up = False
    
    entities = pygame.sprite.Group() # Все объекты
    platforms = [] # то, во что мы будем врезаться или опираться
    
    entities.add(hero)
           
    level = [
 
        "----------------------------------",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -                     --------",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -             --             -",
        "-   -                            -",
        "-   -                            -",
        "-   -        -                   -",
        "-   -                     -      -",        
        "-   -                            -",
        "-   -         --                  -",
        "-   -                            -",
        "-   -                            -",
        "-   -                 -          -",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -          --                -",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -                --          -",
        "-   -                            -",        
        "-   -                            -",
        "-   -                            -",
        "-   -          ---               -",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -               --           -",
        "-   -                            -",
        "-   -                            -",
        "-   -                      -     -",
        "-   -        -                   -",
        "-   -                            -",
        "-   -                            -",
        "-   -                -           -",        
        "-   -                            -",
        "-   -                            -",
        "-   -                       -    -",
        "-   -                            -",
        "-   -                -           -",
        "-   -                            -",
        "-   -        -                   -",
        "-   -                 -          -",
        "-   -                            -",
        "-   -                        -   -",
        "-   -                            -",
        "-   -                --          -",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -  --       --               -",
        "-   -                            -",        
        "-   -                            -",
        "-   -                            -",
        "-   -     --       --      --    -",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -  --     -        --      - -",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -      --       --     --    -",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -           --      --       -",        
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   ---     --     --        --  -",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -  --       --     --      ---",
        "-   -                            -",
        "-   -                            -",
        "-   -                            -",
        "-   -       -       --      -    -",
        "-   -                            -",
        "-                                -",
        "-                                -",
        "-                -       --      -",
        "-                                -",
        "-                                -", 
        "----------------------------------"
    ]
   
    timer = pygame.time.Clock()
    y=0
    x=0# координаты
    for row in level: # вся строка
        for col in row: # каждый символ
            if col == "-":
                pf = Platform(x,y)
                entities.add(pf)
                platforms.append(pf)


            x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT    #то же самое и с высотой
        x = 0                   #на каждой новой строчке начинаем с нуля
    
    total_level_width  = len(level[0])*PLATFORM_WIDTH # Высчитываем фактическую ширину уровня
    total_level_height = len(level)*PLATFORM_HEIGHT   # высоту
    
    camera = Camera(camera_configure, total_level_width, total_level_height) 
    y=-1850
    x=10    
    while 1: # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get(): # Обрабатываем события
            up = True
            if e.type == QUIT:
                raise SystemExit
            
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать 


        camera.update(hero) # центризируем камеру относительно персонажа
        hero.update(left, right, up,platforms) # передвижение
        #entities.draw(screen) # отображение
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        
        
        pygame.display.update()     # обновление и вывод всех изменений на экран
        

if __name__ == "__main__":
    start_screen()
    main()
