from gtts import gTTS
import playsound

# Criando arquivo de texto

nome_arquivo = str(input('Digite um nome para o arquivo de texto (sem o .txt): ')) + '.txt'
texto = str(input('Digite o texto que será escrito no arquivo: '))
arquivo = open(f'{nome_arquivo}', 'w', encoding='UTF-8')
# Escrevendo o texto no arquivo criado.
arquivo.write(texto)
# Fechando o arquivo
arquivo.close()


# Lendo arquivo de texto
arquivo = open(nome_arquivo, 'r', encoding='UTF-8').read()
# Transformando em mp3 e salvando
txt_para_audio = gTTS(arquivo, lang='pt-br')
arquivo_mp3 = nome_arquivo.replace('.txt', '.mp3')
txt_para_audio.save(arquivo_mp3)

# Reproduzindo o mp3 (do texto que foi transformado)
# Deve-se ter cuidado, pois se o diretório mudar, o arquivo não reproduzirá.
playsound.playsound(fr'C:\Users\Daniel\Documents\Projetos Python\txt_para_mp3\{arquivo_mp3}')
