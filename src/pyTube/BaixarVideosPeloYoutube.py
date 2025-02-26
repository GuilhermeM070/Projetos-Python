from pytubefix import YouTube
from pytubefix.cli import on_progress  # Authenticate once for subsequent downloads

print("Bem-vindo ao programa de baixar vídeos do YouTube!")

while True:
    url = input("\nInsira o link do vídeo (ou digite 'sair' para encerrar): ")
    
    if url.lower() == "sair":
        print("Programa encerrado. Até mais!")
        break  # Sai do loop se o usuário digitar 'sair'

    try:
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)

        print(f"\nTítulo: {yt.title}")
        print(f"Thumbnail: {yt.thumbnail_url}")

        stream = yt.streams.get_highest_resolution()  # Melhor resolução disponível
        output_path = "C:\\Users\\Guima\\Videos\\Python"
        
        print("\nBaixando o vídeo... Aguarde.")
        stream.download(output_path=output_path)  # Faz o download do vídeo
        
        print("\nDownload concluído com sucesso! O arquivo está salvo em:", output_path)

    except Exception as e:
        print(f"\nErro ao baixar o vídeo: {e}\nTente novamente.")

