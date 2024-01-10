from utils import *
# code for window for the app
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# code for the grid and color
def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range (cols):
            grid[i].append(color)
            
    return grid

# draw function
def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            
# code to make the background white
def draw(win, grid):
    win.fill(BG_COLOR)
    pygame.display.update()
    
# start application
run = True

# set the speed (FPS) for which the while loop exectutes
clock = pygame.time.Clock()

# calling the grid that was defined above
grid = init_grid(ROWS, COLS, BG_COLOR)

# while loop to have the game running until the user clicks 'X'
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    draw(WIN)
    
pygame.quit()



