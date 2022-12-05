# Prática #6 - Visão Computacional & API

__Alunos:__
* Hadler Henrique Tempesta (11801095)
* Lucas Daudt Franck (11845726)
---

### Resumo:
O código simula uma base meteorológica amadora na RaspberryPi. Os dados climáticos são coletados remotamente do Laboratório de Climatologia da UFSC através de uma [API da Oracle](https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583) no formato JSON. Uma câmera é usada para tirar fotos e gravar vídeos para simular a aquisição de dados de iluminação do ambiente.

### Código:
O funcionamento do código depende do uso das bibliotecas `json`, `requests`, `pprint`, `time` e `picamera`. Caso essas bibliotecas não estejam disponíveis, executar os seguintes comandos no Bash:
```bash
pip install json
pip install requests
pip install pprint
pip install time
pip install picamera
```
No arquivo `pratica6.py` está o código do projeto comentado.

### Imagem e Vídeo:
Os arquivos `foto.jpg` e `video.h264` são a foto e o vídeo obtidos durante a realização da prática no laboratório, respectivamente. Neles estão anotados os nomes dos alunos e seus números USP.


