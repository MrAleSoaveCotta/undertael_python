import asyncio
import pygame 

pygame.init()


height = 720
width = 1280
screen = pygame.display.set_mode([width,height])

pygame.display.set_caption("undertale test")


#fps
clock = pygame.time.Clock()
FPS=60

#colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

#assets
heart = pygame.image.load('heart.png')
heart = pygame.transform.scale(heart, (32,32))


def player(x,y):
    screen.blit(heart,(x,y))


async def main():

    player_x = 100
    player_y = 100

    player_x_move = 0
    player_y_move = 0

    move_velocity = 5


    running = True
    
    while running:  

        screen.fill(black)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            #keydown handler
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_y_move = -move_velocity
                if event.key == pygame.K_DOWN:
                    player_y_move = move_velocity

                if event.key == pygame.K_RIGHT:
                    player_x_move = move_velocity
                if event.key == pygame.K_LEFT:
                    player_x_move = -move_velocity


            #keyup handler
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    player_y_move = 0
                if event.key == pygame.K_DOWN:
                    player_y_move = 0

                if event.key == pygame.K_RIGHT:
                    player_x_move = 0
                if event.key == pygame.K_LEFT:
                    player_x_move = 0
        



        player_x += player_x_move
        player_y += player_y_move

        player(player_x,player_y)


        pygame.display.update()


        clock.tick(FPS)
        await asyncio.sleep(0)

        if not running:
            pygame.quit()

                

asyncio.run(main())