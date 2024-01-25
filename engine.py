import pygame
import photos

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Minecraft Engine")

clock = pygame.time.Clock()

angle = 1
def render():
    return pygame.image.load(photos.photos["angle" + str(angle)])

running = True
while running:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if angle == 8:
                    angle = 1
                else:
                    angle += 1
            elif event.key == pygame.K_RIGHT:
                if angle == 1:
                    angle = 8
                else:
                    angle -= 1
            
    screen.blit(render(), (0, 0))
    pygame.display.flip()        
    
pygame.quit()