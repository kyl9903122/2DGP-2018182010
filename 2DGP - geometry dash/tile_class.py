from pico2d import*

class TILE:
    def __init__(self,x,y,size_x,size_y,mode):
        #mode에 따라 타일의 모양이 달라진다. 1. basic tile
        self.image = None
        if(mode == 1):
            self.image = load_image('basic_tile.png')
        elif(mode == 2):
            self.image = load_image('tile2.png')
        self.x, self.y, self.size_x, self.size_y = x,y,size_x,size_y
        pass

    def Move(self, speed):
        if(self.x>-self.size_x/2):
            self.x -= speed
        pass

    def Draw(self):
        if(self.x>-self.size_x/2 and self.x<1000+self.size_x/2):
            self.image.draw(self.x,self.y,self.size_x,self.size_y)
        pass

    def ColideCheck(self,character_x,character_y,character_size):
        pass