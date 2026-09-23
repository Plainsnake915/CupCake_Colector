import pygame
import asyncio  # 1. Import asyncio

pygame.init()
screen = pygame.display.set_mode((800, 600))
score_font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

player_image = pygame.image.load("assets/player.png").convert_alpha()
player_image = pygame.transform.scale(
    player_image,
    (50, 50)
)
cupcake_image = pygame.image.load(
    "assets/cupcake.png"
).convert_alpha()
cupcake_image = pygame.transform.scale(
    cupcake_image,
    (30, 30)
)


cupcakes = [
    pygame.Rect(150, 230, 30, 30),
    pygame.Rect(400, 180, 30, 30),
    pygame.Rect(520, 310, 30, 30)
]

platforms = [
    pygame.Rect(0, 350, 600, 50),
    pygame.Rect(100, 270, 150, 20),
    pygame.Rect(350, 220, 150, 20)
]







# Place your game loop inside an async function
async def main():  # 2. Add 'async' before your main function definition
    running = True
    player_x = 50
    player_y = 300
    player_dy = 0
    gravity = 0.5
    jump_speed = -10
    on_ground = False
    score = 0


    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        player_rect = pygame.Rect(
            player_x,
            player_y,
            50,
            50
        )
        # --- Your Game Logic & Drawing Code Here ---
        screen.fill((0, 0, 0))
        screen.blit(player_image, (player_x, player_y))  # Example of drawing the player image
        for platform in platforms:
            pygame.draw.rect(
                screen,
                (100, 180, 100),
                platform
            )
            if player_rect.colliderect(platform):
                player_y = platform.top - player_rect.height+1
                player_dy = 0
                on_ground = True
            
        for cupcake in cupcakes:
            screen.blit(
                cupcake_image,
                (cupcake.x, cupcake.y)
            )

        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= 5
            

        if keys[pygame.K_RIGHT]:
            player_x += 5
            

        if keys[pygame.K_UP] and on_ground:
            player_dy = jump_speed
            on_ground = False

        # Apply gravity
        player_dy += gravity
        if on_ground:
            player_dy = 0
        player_y += player_dy

        for cupcake in cupcakes[:]:
            if player_rect.colliderect(cupcake):
                cupcakes.remove(cupcake)
                score += 1
        if not cupcakes:
            cupcakes.append(pygame.Rect(150, 230, 30, 30))
            cupcakes.append(pygame.Rect(400, 180, 30, 30))
            cupcakes.append(pygame.Rect(520, 310, 30, 30))

        collision = False
        for platform in platforms:
            if player_rect.colliderect(platform):
                collision = True
                break
        if not collision:
            on_ground = False
        
        



        clock.tick(60)  # Limit the frame rate to 60 FPS
        await asyncio.sleep(0)

# Run the game using asyncio
asyncio.run(main())  # 4. Initialize the loop


