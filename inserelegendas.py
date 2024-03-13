import os, glob, random, string, shutil

def get_random_filename(ext):
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(20)]) + ext

for filename in glob.glob("*.mp4"):
    try:
        print(str(filename))
        _, ext = os.path.splitext(filename)
        random_filename = get_random_filename(ext)
        shutil.copyfile(filename, random_filename)
        for legenda in glob.glob(filename.replace(".mp4",".srt")):
            novalegenda = random_filename.replace('.mp4','.srt')
            shutil.copyfile(legenda, novalegenda)
            with open(novalegenda, 'r') as arquivo_orig:
                conteudo = arquivo_orig.read()
            with open(novalegenda, 'w', encoding='utf-8') as novo_arquivo:
                novo_arquivo.write(conteudo)
            print(str(legenda))
            randomlegendado = random_filename.replace('.mp4','(L).mp4')
            os.system('ffmpeg -sub_charenc ANSI -i "' + str(random_filename) + '" -vf subtitles="' + str(novalegenda) + '" -maxrate 2000000 -crf 20 -c:a aac -c:v libx264 -movflags frag_keyframe "' + str(randomlegendado) + '"')
            shutil.copyfile(randomlegendado, filename.replace('.mp4','(L).mp4'))
            os.remove(random_filename)
            os.remove(novalegenda)
    except Exception as e:
        print(e)