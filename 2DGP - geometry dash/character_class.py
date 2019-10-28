from pico2d import*
import main_state

degree = 0

class CHARACTER:
    def __init__(self):
        self.image = load_image('character.png')
        self.x, self.y = 130, 130
        self.size = 50
        global degree
        degree = 0

    def Move(self, isJump):
        global degree
        if (isJump == True):
            self.y += math.sin(degree / 360 * 2 * math.pi) * 4
            degree += 7
            if (degree >= 360):
                isJump = False
                degree = 0
        return isJump

    def Draw(self):
        self.image.clip_draw(0, 0, 117, 118, self.x, self.y, self.size, self.size)
        pass

    def OutCharacterPos(self):
        return self.x, self.y

    def OutCharacterSize(self):
        return self.size