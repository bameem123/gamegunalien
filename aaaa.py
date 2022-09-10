#Import thư viện hỗ trợ 
from pygame import *
#sử dụng thư viên random 
from random import *


#GameStrite là class của con strite.strite
#strite.strite lấy từ thư viện pygame
#GameStrite sẽ được dùng để tạo ra các nhân vật trong game
class GameSprite(sprite.Sprite):
    # hàm khởi tạo
    # luôn phải có từ khóa self
    def __init__(self, character_image, x, y, width, height, speed):
        #kêu cha thực thi trước 
        sprite.Sprite.__init__(self)
        #Tạo ra một cái biến để chứa ảnh của nhân vật 
        self.image = image.load(character_image)
        #phóng to hoặc thu nhỏ ảnh thành kíck thước của  em mong muốn
        self.image = transform.scale(self.image, (width, height))
        # lưu thông tin về tốc độ nhân vật 
        self.speed = speed

        #Tạo ra một hình chữ nhật 
        #Biến self.rect chữa hình chữ nhật bằng kích thước tấm ảnh 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #vẽ nhân vật ở tọa độ x, y
        window.blit(self.image,(x, y))
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        # Tạo ra class người chơi - class của GameSpite
        # Tức là class con có mọi thứ của cha 
class Player(GameSprite):
            #hàm lắng nghe sự điều khiển
    def update(self):
                #lấy ra những nút mới được ấn 
        keys = key.get_pressed()
                # kiểm tra nút vừa ấn 
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x +=self.speedw
    #hàm bắn viên đạn
    def fire(self):
    #TẠo ra một cái biên chứa đạn 
        bullet = Bullet(img_bullet, self.rect.centerx,y=self.rect.top,
            width=15, height=20,speed=-15)
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0 :
            self.kill()
# class kẻ thù  - con của class gamesprite
class Enemy(GameSprite):
    def update(self):
        #tăng tọa độ y - di chuyển lên trên 
        self.rect.y += self.speed
        # Biến  đếm số quái vật đã bị bắng hụt 
        global lost 
        #nếu con quái vật đụng vác phiến trên 
        if self.rect.y > win_height:
            #chọn vị trí ngẫu nhiên mới cho quái vật
            self.rect.x= randint(80, win_widtn - 80)
            self.rect.y = 0
            #tăng quái vật bị bắn hụt 
            lost = lost + 1
# tạo ra một phong chữ dùng hiên lên màng hình
font.init()
font1 = font.Font(None,80)
font2 = font.Font(None,36)
# viết dòng chữ thắng thua 
win = font1.render('YOU WIN',True,(255, 255, 255))
lose = font1.render('YOU LOSE',True,(0, 0, 0))
# taọ bộ phát nhạc 
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
#âm thanh bắn đạn 
fire_sound = mixer.Sound('fire.ogg')
#ảnh cho các nhân vật và thể trong game 
img_back = 'galaxy.jpg' #game background
img_bullet = 'bullet.png'#bullet
img_hero='rocket.png'#hhero
img_enemy = 'ufo.png'#enemy
# biến chứa điểm 
score =  0 # chưa tiêu diêt kẻ địch 
#số điểm cần đạt được 
goal=10
#số điểm để thua 
lost=0
#số điểm tối đa để thắng 
max_lost = 3 
# tạo kích thước màn hình   chơi game 
win_widtn = 700
win_height = 500
#đặt tên cho game 
display.set_caption('Shooter')
#tạo ra màn hình với kích thước đã chọn 
window = display.set_mode((win_height, win_widtn))
# hình nền 
background = image.load(img_back)
#phóng to / thu nhỏ tấm hình cho vừa màn hình game 
background = transform.scale(background , (win_widtn , win_height))
#tạo phi thuyền 
ship = Player(img_hero,x=5,y=win_height-100,width=80, height=100, speed=10)
#taọ ra & con quái vật 
monsters = sprite.Group()

#tạo ra & cpn quái vật sử dụng vòng lập 
for i in range(1, 6):
    monster = Enemy(img_enemy, x=randint(80, win_widtn - 80), y=-40, width=80, height=50, speed=3 )
    monsters.add(monster)
#danh sách những viên đạn 
bullets = sprite.Group()
#tạo ra một biến tính xem game kết thúc 
finish = False
# tạo biến kiểm tra coi gâme có chạy hay ko
run = True
#trong khi game còn đang chạy 
while run:
    #trong tất cả các hoạt động 
    for e in event.get():

        if e.type == QUIT:
            run = False
    #bắn đạn 
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
           #kích hoạt âm thanh 
                fire_sound.play()
            #cho phi thuyền di chuyển
                ship.fire()
    if not finish:
        #cập nhật lại hình nên 
        window.blit(background,(0,0))
        #cập nhật chuyển động cho game 
        ship.update()
        monster.update()
        bullets.update()

        ship.reset()
        # về những con quái vật lên màn hình 
        monsters.draw(window)
        bullets.draw(window)
        #kiểm tra coi viên đạn nào bắn trúng 
        collides = sprite.groupcollide(monsters,bullets, True, False)

        for c in collides:
            score+=1
            x=randint(80,win_widtn - 80)
            y=-40
            widtn=80,
            height=-50
            speed=randint(1, 5)
        monsters.add(monster)
        #bắn hụt quá nhiều con quái vật 
        if sprite.spritecollide(ship, monsters,False) or lost >= max_lost:
            finish =True
            window.blit(lose,(200,200))

        text = font2.render("Score:  " + str(score),1 , (255,255,255))
        window.blit(text,(10,20))

        text_lose = font2.render("missed  " +str(lost),1,(255,255,255))
        # Cập nhật màn hình game sau mỗi giây
        display.update()
    else:
        finish = True
        score = 0
        lost = 0
        for bullet in bullets:
            bullet.kill()
 
        for monster in monsters:
            monster.kill()
 
        time.delay(3000)
    
    time.delay(50)


