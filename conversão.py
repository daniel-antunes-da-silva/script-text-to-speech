from gtts import gTTS
import playsound

arquivo = open('texto.txt', 'r', encoding='UTF-8').read()
txt_para_audio = gTTS(arquivo, lang='pt-br')
txt_para_audio.save('poema.mp3')

# Deve-se ter cuidado, pois se o diretório mudar, o arquivo não reproduzirá.
playsound.playsound(r'C:\Users\Daniel\Documents\Projetos Python\txt_para_mp3\poema.mp3')
