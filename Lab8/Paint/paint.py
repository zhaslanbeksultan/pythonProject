import pygame
pygame.init()

# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('Paint')

draw_on = False
last_pos = (0, 0)

# Radius of the Brush
radius = 5

ch_color = (255,255,255)

# Create a Font object
font = pygame.font.Font('fonts/Tilt_Neon/static/TiltNeon-Regular.ttf',25)

# Messages to display
messages = ["E - eraser", "C - draw circle", "R - draw rectangle", "B - color:sky blue", "Y - color: yellow", "P - color: purple"]


def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

def draw_rect(ch_color):
    # Get the current mouse position
    pos = pygame.mouse.get_pos()
    # The size of the rectangle
    rect_size = (50, 50)
    # The position of the top-left corner of the rectangle
    rect_pos = (pos[0] - rect_size[0]/2, pos[1] - rect_size[1]/2)
    # Draw the rectangle on the screen
    pygame.draw.rect(screen, ch_color, (rect_pos, rect_size))

def draw_circle(ch_color):
    # Get the current mouse position
    pos = pygame.mouse.get_pos()
    # Radius of the circle
    radius = 25
    # Draw the circle on the screen
    pygame.draw.circle(screen, ch_color, pos, radius)

try :
    while True :
        # Waiting for any action
        e = pygame.event.wait()

        if e.type == pygame.QUIT :
            raise StopIteration
        # Blit message on the screen
        for i, message in enumerate(messages):
            text_surface = font.render(message, True, (0,255,0))
            screen.blit(text_surface, (10, 10 + i * 40))

        # User action
        if e.type == pygame.KEYDOWN:
            if e.key == ord("p"):
                ch_color = (128,0,128)
            if e.key == ord("b"):
                ch_color = (0,191,255)
            if e.key == ord("y"):
                ch_color = (255,255,0)
            if e.key == ord("r"):
                draw_rect(ch_color)
            if e.key == ord("c"):
                draw_circle(ch_color)
            if e.key == ord("e"):
                ch_color = (0,0,0)


        if e.type == pygame.MOUSEBUTTONDOWN :
            # Chosen color
            color = ch_color
            # Draw a single circle wheneven mouse is clicked down.
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        # When mouse button released it will stop drawing
        if e.type == pygame.MOUSEBUTTONUP :
            draw_on = False
        # It will draw a continuous circle with the help of roundline function.
        if e.type == pygame.MOUSEMOTION :
            if draw_on :
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos
        pygame.display.flip()

except StopIteration :
    pass

# Quit
pygame.quit()