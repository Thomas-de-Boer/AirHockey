import pygame
pygame.display.init()

WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]

WIN_WIDTH, WIN_HEIGHT = WINDOW_SIZE

PLAYER_WIDTH, PLAYER_HEIGHT = WINDOW_SIZE[0] * 0.09375, WINDOW_SIZE[1] * 0.1666666666666667

PUCK_WIDTH, PUCK_HEIGHT = WINDOW_SIZE[0] * 0.05625, WINDOW_SIZE[1] * 0.1

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

BG = pygame.transform.scale(pygame.image.load("AirHockey/assets/temp_multiplayer_bg.png"), (WIN_WIDTH, WIN_HEIGHT))

RED_PLAYER_MODEL = pygame.transform.scale(pygame.image.load("AirHockey/assets/temp_red_pusher.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)).convert_alpha()
# BLUE_PLAYER_MODEL = pygame.transform.scale(pygame.image.load("AirHockey/assets/temp_blue_pusher.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)).convert_alpha()
PUCK_MODEL = pygame.transform.scale(pygame.image.load("AirHockey/assets/temp_puck.png"), (PUCK_WIDTH, PUCK_HEIGHT)).convert_alpha()

# wall positions
walls = [
    ((-WINDOW_SIZE[0] / 2, 0), (WINDOW_SIZE[0] * 2, -WINDOW_SIZE[0])),
    ((0, 0), (-WINDOW_SIZE[0], WINDOW_SIZE[1])),
    ((-WINDOW_SIZE[0] / 2, WINDOW_SIZE[1]), (WINDOW_SIZE[0] * 2, WINDOW_SIZE[0])),
    ((WINDOW_SIZE[0], 0), (WINDOW_SIZE[0], WINDOW_SIZE[1])),
    ]

#     ((0, -1), (1600, -1)),
#     ((-1, 0), (-1, 900)),
#     ((0, 900), (1600, 1)),
#     ((1600, 0), (1, 900)),


def draw(red_player_x, red_player_y, puck_x, puck_y):
    # draw background
    WIN.blit(BG, (0,0))

    # draw redplayer
    WIN.blit(RED_PLAYER_MODEL, (red_player_x, red_player_y))

    # draw puck
    WIN.blit(PUCK_MODEL, (puck_x, puck_y))

    # update display
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    # make walls
    for i in range(4):
        walls[i] = pygame.Rect(walls[i])

    # make red_player
    red_player = pygame.Rect((1000, 500), (PLAYER_WIDTH, PLAYER_HEIGHT))

    # make puck
    puck = pygame.Rect((800, 400), (PUCK_WIDTH, PUCK_HEIGHT))

    # make drag variable
    drag = False

    # make velocity variables
    red_player_vel_x, red_player_vel_y = 0, 0
    red_old_player_x, red_old_player_y = 0, 0
    puck_vel_x, puck_vel_y = 0, 0

    running = True
    while running:
        clock.tick(60)
        
        # event loop
        for event in pygame.event.get():

            # checks for escape to quit
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # red player movement
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if red_player.collidepoint(event.pos):
                        drag = True
                        mouse_x, mouse_y = event.pos
                        offset_x = red_player.x - mouse_x
                        offset_y = red_player.y - mouse_y
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drag = False
                    
            if event.type == pygame.MOUSEMOTION:
                if drag:
                    mouse_x, mouse_y = event.pos
                    red_player.x = mouse_x + offset_x
                    red_player.y = mouse_y + offset_y

        # calculate red_player velocity
        red_player_vel_x = red_player.x - red_old_player_x
        red_player_vel_y = red_player.y - red_old_player_y

        # make the red_player slide
        # if drag == False:
        #     red_player.x += red_player_vel_x
        #     red_player.y += red_player_vel_y

        #     if red_player_vel_x != 0:
        #         if red_player_vel_x < 0:
        #             red_player_vel_x -= (red_player_vel_x / 20)
        #         else:
        #             red_player_vel_x -= (red_player_vel_x / 20)
        #         if red_player_vel_y != 0:
        #             if red_player_vel_y < 0:
        #                 red_player_vel_y -= (red_player_vel_y / 20)
        #             else:
        #                 red_player_vel_y -= (red_player_vel_y / 20)

        # puck bounce off red_player
        # if red_player.colliderect(puck):
        #     if red_player_vel_x == 0 or red_player_vel_y == 0:
        #         puck_vel_x *= -1
        #         puck_vel_y *= -1

        # puck collision detection
        if red_player.colliderect(puck):
            puck_vel_x, puck_vel_y = red_player_vel_x, red_player_vel_y
        
        puck.x += puck_vel_x
        puck.y += puck_vel_y

        # puck velocity loss over time
        if puck_vel_x != 0:
            if puck_vel_x < 0:
                puck_vel_x -= (puck_vel_x / 70)
            else:
                puck_vel_x -= (puck_vel_x / 70)
        if puck_vel_y != 0:
            if puck_vel_y < 0:
                puck_vel_y -= (puck_vel_y / 70)
            else:
                puck_vel_y -= (puck_vel_y / 70)

        # add max velocity
        if puck_vel_x > 10:
            puck_vel_x = 10
        if puck_vel_y > 10:
            puck_vel_y = 10
        
        # puck wall collision detection
        if puck.colliderect(walls[0]):
            puck_vel_y *= -1
            puck.y += 10
        if puck.colliderect(walls[1]):
            puck_vel_x *= -1
            puck.x += 10
        if puck.colliderect(walls[2]):
            puck_vel_y *= -1
            puck.y -= 10
        if puck.colliderect(walls[3]):
            puck_vel_x *= -1
            puck.x -= 10

        draw(red_player.x, red_player.y, puck.x, puck.y)

        red_old_player_x, red_old_player_y = red_player.x, red_player.y

    pygame.quit()

if __name__ == "__main__":
    main()
