from inspect import CORO_CLOSED
from turtle import Screen
import pygame
from pygame import mixer
   
    pygame.init()
    mixer.init()

    screen = pygame.display.set_mode((624,434))
    pygame.display.set_caption("test")
    chute_state = [0,1,2,3,4,5,6]
    chute_state[0] = "images/6.png"
    chute_state[1] = "images/5.png"
    chute_state[2] = "images/4.png"
    chute_state[3] = "images/3.png"
    chute_state[4] = "images/2.png"
    chute_state[5] = "images/1.png"
    chute_state[6] = "images/0.png"

    state = "images/4.png"
    mixer.music.load("sound/wind.wav")
    mixer.music.load("sound/chute.wav")
    mixer.music.set_volume(0.7)
    mixer.music.play()

    background_surface = pygame.image.load("images/sky.jpg")
    player_surface = pygame.image.load("images/John.png")
    player_surface = pygame.transform.scale(player_surface,(200,200))
        


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for i in range (0,6):
            parachute_surface = pygame.image.load(chute_state[i])
            parachute_surface1 = pygame.transform.scale(parachute_surface,(200,200))
            pygame.time.delay(500)
            screen.blit(background_surface,(0,0))
            screen.blit(player_surface,(212,200))
            screen.blit(parachute_surface1,(200,78))    
            
            
            pygame.display.update()
        