import pygame 

class SoundHelper(object):


    async def play_preopen():
        await SoundHelper.play("./sounds/preopen.mp3")

    async def play_open():
        await SoundHelper.play("./sounds/open.mp3")

    async def play_close():        
        await SoundHelper.play("./sounds/close.mp3")

    async def play_preclose():
        await SoundHelper.play("./sounds/preclose.mp3")


    async def play(file):
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()        