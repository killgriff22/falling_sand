from modules import *
class screen:
    def __init__(self, width, height, title,*args, **kwargs):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height), *args, **kwargs)
        pygame.display.set_caption(self.title)
        self.reset()
        self.clock = pygame.time.Clock()
    def reset(self):
        self.raster = [[cell(i,j) for i in range(self.width)] for j in range(self.height)]
    def draw(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.raster[j][i]:
                    #determine a color between blue, black ,and red for negative, zero, and positive pressure
                    if self.raster[j][i].pressure < 0:
                        color = (0, 0, (255 - abs(self.raster[j][i].pressure)%255))
                    elif self.raster[j][i].pressure > 0:
                        color = ((255 - self.raster[j][i].pressure)%255, 0, 0)
                    else:
                        color = (0, 0, 0)
                    self.screen.set_at((i,j), color)
    def tick(self):
        #disperse all the pressure
        for i in range(self.width):
            for j in range(self.height):
                if self.raster[j][i].pressure > 0:
                    for k in range(-1,2):
                        for l in range(-1,2):
                            if i+k >= 0 and i+k < self.width and j+l >= 0 and j+l < self.height:
                                self.raster[j+l][i+k].pressure += self.raster[j][i].pressure // 16
                    self.raster[j][i].pressure -= self.raster[j][i].pressure // 8
                elif self.raster[j][i].pressure < 0:
                    for k in range(-1,2):
                        for l in range(-1,2):
                            if i+k >= 0 and i+k < self.width and j+l >= 0 and j+l < self.height:
                                self.raster[j+l][i+k].pressure -= abs(self.raster[j][i].pressure) // 16
                    self.raster[j][i].pressure += abs(self.raster[j][i].pressure) // 8

                


class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pressure = 0
        self.element = None