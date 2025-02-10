from pytubefix import YouTube

print("Bem vindo ao programa de baixar videos do YouTube!")

yt = YouTube(input("Insira o link do video: ")) # Insira o link do video...

print(yt.title) # Para descobrir o título do video...

print(yt.thumbnail_url) # Para receber a URL da Thumb...

#stream = yt.streams.get_audio_only() # Para baixar somente o audio...
stream = yt.streams.get_highest_resolution() # Melhora a resolução do vídeo...

#stream.download(mp3=True)
stream.download(output_path="C:\\Users\\Guima\\Videos\\Python")

print("Video ou Música Baixado Com Sucesso!")
