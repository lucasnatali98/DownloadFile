import os
import requests


def download_file(url, path):
    # faz requisição ao servidor
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        with open(path, 'wb') as new_file:
            new_file.write(response.content)
        print("Download finalizado. Salvo em: {}".format(path))
    else:
        response.raise_for_status()

if __name__ == "__main__":
    BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'

    OUTPUT_DIR = 'output'
    for i in range(1, 26):
        name_file = os.path.join(OUTPUT_DIR, 'nota_de_aula_{}.pdf'.format(i))
        download_file(BASE_URL.format(i), name_file)