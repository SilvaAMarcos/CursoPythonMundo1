from pygame import mixer
mixer.init()
mixer.music.load('audio.mp3')
mixer.music.play()
x = input('Digite a tecla que quiser parar...')
