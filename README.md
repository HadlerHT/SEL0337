# Prática #6 - Visão Computacional & API

__Alunos:__
* Hadler Henrique Tempesta (11801095)
* Lucas Daudt Franck (11845726)
---

### Resumo:
O código simula uma base meteorológica amadora na RaspberryPi. Os dados climáticos são coletados remotamente do Laboratório de Climatologia da UFSC através de uma [API da Oracle](https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583) no formato JSON. Uma câmera é usada para tirar fotos e gravar vídeos para simular a aquisição de dados de iluminação do ambiente.

### Código:
No arquivo `pratica6.py` está o código do projeto comentado.

O funcionamento do código depende do uso das bibliotecas `json`, `requests`, `pprint`, `time` e `picamera`. Caso essas bibliotecas não estejam disponíveis, executar os seguintes comandos no Bash:
```
pip install json
pip install requests
pip install pprint
pip install time
pip install picamera
```

* __API__:
A coleta dos dados meteorológicos é feita pela função `get(endereco)` que envia uma requisição GET ao `endereco` especificado. Os dados solicitados são retornados no formato JSON que são decodificados pelo método `.json()` resultando em uma variável dicionário. A função `pprint` imprime os dados do dicionario formatados no terminal.

* __Camera__:
Uma instância da câmera é inicalizada com comando `with PiCamera as camera:`. Esse objeto conta com o método `.annotate_text` que permite escrever uma mensagem sobrescrita na imagem capturada pelo sensor. O método `.resolution` define a resolução da imagem da câmera; esse parâmetro varia para operação como foto e como vídeo. O método `.capture` salva a imagem da câmera, enquanto o `.start_recording` e `.stop_recording` permitem a gravação do vído.

### Imagem e Vídeo:
Os arquivos `foto.jpg` e `video.h264` são a foto e o vídeo obtidos durante a realização da prática no laboratório, respectivamente. Neles estão anotados os nomes dos alunos e seus números USP.

### Histórico de Comandos:
No arquivo `hist.txt` está disponível o histórico dos comandos inseridos no Bash.

