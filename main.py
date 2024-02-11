from classes import *
Screen = screen(100,100,"Falling Sand",pygame.FULLSCREEN)
print(Screen.width*Screen.height)
dotick = True
step = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if event.button == 1:
                Screen.raster[event.pos[1]][event.pos[0]].pressure = 10000
            elif event.button == 3:
                Screen.raster[event.pos[1]][event.pos[0]].pressure = -10000
            print(Screen.raster[event.pos[1]][event.pos[0]].pressure)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Screen.reset()
            elif event.key == pygame.K_SPACE:
                dotick = not dotick
            elif event.key == pygame.K_f:
                step = True
    if dotick or step:
        Screen.tick()
        if step:
            step = False
    Screen.draw()
    display_text(Screen.screen, Screen.clock.get_fps()//1, 0, 0)
    pygame.display.update()
    Screen.clock.tick(999999)