import pygame

# Initialize Pygame
pygame.init()

# Set screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game loop variable
running = True

# Main loop to keep the game running
while running:
    # Handle events (explained in next class)
    for event in pygame.event.get():
	    # Check for quit event
	    if event.type == pygame.QUIT:
	        running = False

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw a white rectangle for the paddle
    pygame.draw.rect(screen, WHITE, (20, screen_height // 2 - 50, 10, 100))

    # Draw a white circle for the ball
    pygame.draw.circle(screen, WHITE, (screen_width // 2, screen_height // 2), 10)

    # Ball properties
    ball_x = screen_width // 2  # Initial x-position (center of the screen)
    ball_y = screen_height // 2  # Initial y-position (center of the screen)
    ball_speed_x = 5  # Speed in the x-direction (pixels per frame)
    ball_speed_y = 5  # Speed in the y-direction (pixels per frame)
    
    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

