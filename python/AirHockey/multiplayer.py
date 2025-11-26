import pygame

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

BG = pygame.transform.scale(pygame.image.load("AirHockey/assets/temp_multiplayer_bg.png"), (1600, 900))

PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200

PUCK_WIDTH = 120
PUCK_HEIGHT = 120

PLAYER_MODEL = pygame.transform.scale(pygame.image.load("AirHockey/assets/temp_red_pusher.jpg"), (PLAYER_WIDTH, PLAYER_HEIGHT))
PUCK_MODEL = pygame.transform.scale(pygame.image.load("AirHockey/assets/temp_puck.jpg"), (PUCK_WIDTH, PUCK_HEIGHT))

# wall positions
walls = [
    ((0, 0), (1600, 1)),
    ((0, 0), (1, 900)),
    ((0, 900), (1600, 1)),
    ((1600, 0), (1, 900)),
    ]


def draw(player_x, player_y, puck_x, puck_y):
    # draw background
    WIN.blit(BG, (0,0))

    # draw redplayer
    WIN.blit(PLAYER_MODEL, (player_x, player_y))

    # draw puck
    WIN.blit(PUCK_MODEL, (puck_x, puck_y))

    # update display
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    # make walls
    for wall in walls:
        wall_rects = []
        wall_rects.append(pygame.Rect(wall))

    # make player
    player = pygame.Rect((1000, 500), (PLAYER_WIDTH, PLAYER_HEIGHT))
    player_x = player.x
    player_y = player.y

    # make puck
    puck = pygame.Rect((800, 400), (PUCK_WIDTH, PUCK_HEIGHT))
    puck_x = puck.x
    puck_y = puck.y

    running = True
    while running:
        clock.tick(60)
        
        # event loop (checking for quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # assign keys value
        keys = pygame.key.get_pressed()

        # quit if escape is pressed
        if keys[pygame.K_ESCAPE]:
            running = False

        # temparary wasd movement
        if keys[pygame.K_w]:
            player_y += -10
        if keys[pygame.K_a]:
            player_x += -10
        if keys[pygame.K_s]:
            player_y += 10
        if keys[pygame.K_d]:
            player_x += 10

        #temp
        if pygame.Rect.collidelistall(wall_rects, player):
            pygame.quit

        draw(player_x, player_y, puck_x, puck_y)

    pygame.quit()

if __name__ == "__main__":
    main()