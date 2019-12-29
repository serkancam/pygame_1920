#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

import random
import time
import locale
# locale.setlocale(locale.LC_ALL,'tr_TR.utf8')


## Renk tanımları
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLUE1 = (15,69,75)
BLUE2 = (106,144,147)

## Ekran değerleri ayarla
WIDTH = 360
HEIGHT = 480
FPS = 30
CAPTION = "Oyunum"
running = False
skorY=0
skorK=0
## Pygame başlangıç ayarları ve pencere oluşturma
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

# oyunda kullanılacak sınıflar

#Oyunda kullanılcak Fonksiyonlar

## oyun döngüsü
def oyun():
    #oyunda kullanılacak nesnelerin ilk başlatılması oyunda kullanışacak değişkenler
    global running
    running = True
    while running:
        ## keep loop running at the right speed
        #oyun hızının ayarlanması
        clock.tick(FPS)
        ## Process inputs(events)
        for event in pygame.event.get():
            #check for closing window
            if event.type == pygame.QUIT:
                print("Oyun Kapatıldı")
                running=False
                return
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    pass
                if event.key==pygame.K_RIGHT:
                    pass
            if event.type==pygame.KEYUP:
                pass
        ## update
        #Oyunda kullanılan nesnelerin değerlerinin değiştirilmesi x,y ses, renk vb


        ## draw/render
        #oyunda kullanılacak nesnelerin güncellenmiş değelere göre çizilmesi
        screen.fill(BLACK)


        #ekranın tekrar yeni çizimler ile güncellenmesi
        pygame.display.update()#pygame.display.flip()
    # pygame.quit()
if __name__ == "__main__":
    oyun()
    pygame.quit()
