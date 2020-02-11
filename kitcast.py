import subprocess, sys, os, glob


# Tenta converter um arquivo para o formato suportado pelo chromecast
# Caso consiga, retornara true
def convert_to_cast(video_name):
    try:
        print("./chromecastize.sh " + video_name)
        # subprocess.call("./chromecastize.sh " + video_name)
        os.system("./chromecastize.sh " + video_name)
        return True
    except Exception as e:
        print(e.with_traceback())
        return False

# verifica no diretorio atual se ha legendas para aquele video
def search_subtitles():
    sub = glob.glob('./*.srt')
    if sub:
        return sub[0]
    else:
        return False

# executa o video
def run_cast_now(video_name):
    sub = search_subtitles()
    try:
        if sub:
            print("Possui legenda")
            os.system('castnow --subtitle ./' + sub + " ./" + video_name)
        else:
            print("Nao possui legenda")
            os.system('castnow ./' + video_name)
    except Exception as e:
        print(e.with_traceback())


if __name__ == '__main__':
    # for arg in sys.argv: print(arg)
    video_name = sys.argv[1]
    if video_name:
        print("Convertendo o arquivo")
        if convert_to_cast(video_name):
            print('convertido com sucesso')
            run_cast_now(video_name)
        else:
            print("falhou ao converter o video")
