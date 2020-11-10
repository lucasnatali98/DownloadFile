# DownloadFile

### Esse mini-projeto consiste uma forma fácil e prática de baixar um ou mais arquivos de uma url da web.

# Uso

Para que seja possível fazer o download dos arquivos que você quer será necessário fornecer ao programa algumas informações como:
*   **url**: é o endereço web referente ao arquivo desejado. Caso os arquivos a serem baixados sejam padronizados em termos de endereço é possível utilizar do **BASE_URL** para iterar sobre os arquivos.
*   **path**: Responsável por definir o caminho do diretório local onde serão salvos os arquivos baixados. 

E antes de executar o programa, precisamos criar uma pasta para armazenar os arquivos baixados, para isso no diretório raiz da aplicação, executaremos:

```
  mkdir output
```

Com isso, em um terminal você pode rodar:
```
  python3 main.py
```
 
# Instalação 
Em primeiro lugar, para utilizar a aplicação será necessário que tenhamos o módulo **request** instalado. Caso não possua-o em sua máquina:

```
  pip install request
```
# Atualizações futuras

- [ ] Leitura de arquivo texto com links selecionados e realização do download a partir dele.
- [ ] Passagem dos parâmetros via terminal. 

# Referências

@programacaodinamica
