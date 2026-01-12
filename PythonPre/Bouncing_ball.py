import pygame
import sys 
#Initialise Pygame
pygame.init()
#Define screen dimensions 
WIDTH, HEIGHT = 800, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

#Define colors(R,G,B)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
#Ball properties
ball_radius = 20
#Start ball in the center 
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
# ball speed (velocity) in x and y directions 
# you can change these values to make the ball move faster or slower 
speed_x = 5
speed_y = 5
#Game loop control and frame rate 
running = True 
clock= pygame.time.Clock() # Used to manage frame rate 

#---2D Game Loop---
while running:
    #---Event Handling---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #Stop the loop if user closes the window 
    #---Game Logic(Movement)---
    #Move the ball 
    ball_x += speed_x
    ball_y += speed_y
    #check for boundary collisions and reverse direction (Bounce)

    #Horizontal bounce(left/right walls)
    if ball_x + ball_radius > WIDTH or ball_x - ball_radius <0:
        speed_x = -1 #Reverse x direction
    #Vertical bounce(top/bottom walls)
    if ball_y + ball_radius > HEIGHT or ball_y - ball_radius <0:
        speed_y = -1 #Reverse y direction
        #---Drawing/Rendering---
        #Fill the screen with black color(to clear previous frame)
    screen.fill(BLACK)
    #Draw the ball (surface, color, center_coordinates, radius)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    #Update the full display surface to the screen 
    pygame.display.flip()
    #Cap the frame rate at 60 frames per second
    clock.tick(60)      
    
#Quit Pygame
pygame.quit()   
sys.exit()