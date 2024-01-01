import time

import pygame

print('==== DESAFIO 21 ====')
print('  REPRODUTOR DE MP3')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer_music.play()
pygame.event.wait(input())