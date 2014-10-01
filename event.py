#-------------------------------------------------------------------------------
# Name:        event.py
# Purpose: manipulate the movement of a beach ball
#
# Author: Sabastian Mugazambi
#
# Created:     25/05/2014
# Copyright:   (c) smuga_000 2014
# Original copy :  by Jadrian Miles
#-------------------------------------------------------------------------------

import sys
import pygame
from pygame.locals import *

def main():
   """Creating the graphical window and loading the ball and the background image."""
   pygame.init()
   width, height = 720, 480
   size = (width, height)
   speed = [2, 2]
   black = (0, 0, 0)
   screen = pygame.display.set_mode(size)

   #loading the background and drawing it on to the graphical window. Blitting the image onto the window.
   beach = pygame.image.load("beach.jpg")
   screen.blit(beach,(0,0))
   pygame.display.flip

   ball = pygame.image.load("ball.gif")
   ballrect = ball.get_rect()

   while True:
    #looping through the event list to see if there any events to exxecute.
      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
         elif event.type == KEYDOWN:
            if event.key == K_q:
               pygame.quit()
               sys.exit()
            elif event.key == K_LEFT:
               speed[0] -= 1
            elif event.key == K_RIGHT:
                speed[0] += 1
            elif event.key == K_DOWN:
                speed[1] += 1
            elif event.key == K_UP :
                speed[1] -= 1
            elif event.key == K_c:
                speed[0] = -speed[0]
                speed[1] = -speed[1]
            # executing the following commands once mouse is clicked as an event.
         elif  event.type == MOUSEBUTTONDOWN:
            if ballrect.collidepoint(pygame.mouse.get_pos()):
                print "You clicked on the ball"
            else:
                print "You did not click on the ball"

      screen.blit(beach,ballrect,ballrect)

      ballrect = ballrect.move(speed)
      if ballrect.left < 0 or ballrect.right > width:
         speed[0] = -speed[0]
      if ballrect.top < 0 or ballrect.bottom > height:
         speed[1] = -speed[1]


      screen.blit(ball, ballrect)
      pygame.display.flip()

if __name__ == '__main__':
   main()
