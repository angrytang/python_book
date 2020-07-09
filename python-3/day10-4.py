import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    x, y = 50, 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()
        pygame.time.delay(50)
        x, y = x + 5, y + 5

if __name__ == '__main__':
    main()