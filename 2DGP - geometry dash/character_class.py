from pico2d import*
import main_state
import tile_class

degree = 0

class CHARACTER:
    def __init__(self):
        self.image = load_image('character.png')
        self.x, self.y = 130, 130
        self.size = 50
        global velocity,dir, fall
        velocity = 7
        fall = -3
        dir = 1

    def Jump(self, isJump,tiles):
        global velocity, dir
        if (isJump == True):
            self.y += velocity
            velocity -= 0.3

            if (degree >= 360):
                isJump = False
                velocity = 0

            if(velocity < 0):
                for tile in tiles:
                    tile_left,tile_right, tile_top, tile_bottom = tile.x - tile.size_x/2, tile.x+tile.size_x/2, tile.y+tile.size_y/2, tile.y-tile.size_y/2
                    if (self.x - self.size / 2 > tile_left + 10 and self.x - self.size / 2 > tile_right - 10) or (
                            self.x + self.size / 2 > tile_left + 10 and self.x + self.size / 2 < tile_right - 10):
                        if (self.y - self.size / 2 <= tile_top ):
                            self.y = tile_top + self.size/2
                            isJump = False
                            velocity = 7
        return isJump
    def Fall(self,tiles):
        global fall
        for tile in tiles:
            tile_left, tile_right, tile_top, tile_bottom = tile.x - tile.size_x / 2, tile.x + tile.size_x / 2, tile.y + tile.size_y / 2, tile.y - tile.size_y / 2
            if (self.x - self.size / 2 > tile_left + 10 and self.x - self.size / 2 > tile_right - 10) or (
                    self.x + self.size / 2 > tile_left + 10 and self.x + self.size / 2 < tile_right - 10):
                if(self.y - self.size/2 >= tile_top  or self.y - self.size/2 <= tile_top):
                    self.y = tile_top + self.size / 2
                    fall = -3
                    return
        self.y += fall
        fall -= 0.2


    def Draw(self):
        self.image.clip_draw(0, 0, 117, 118, self.x, self.y, self.size, self.size)
        pass

    def OutCharacterPos(self):
        return self.x, self.y

    def OutCharacterSize(self):
        return self.size