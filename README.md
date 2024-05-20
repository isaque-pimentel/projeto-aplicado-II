# Projeto Aplicado II

**Projeto Sentinela: Automatização do Controle de Acesso Veicular em Condomínios**
 
##  Grupo:
* ALINE CORRÊA – 10414773 – 10414773@mackenzista.com.br
* ISAQUE PIMENTEL – 10415608 – 10415608@mackenzista.com.br
* MAIKI SOARES – 10415481 – 10415481@mackenzista.com.br
* VANESSA CORDEIRO – 10415118 – 10415118@mackenzista.com.br

## Apresentação do Grupo

Somos alunos de Ciências de Dados trabalhando em um projeto de Aprendizado de Máquina para resolver problemas de dados com aplicação comercial. Desenvolvemos o **Sentinela**, um sistema para detectar e converter placas de veículos a partir de fotos da frente dos veículos. Após a divulgação do produto, uma administradora de condomínios (empresa fictícia) nos contatou interessada em implementar o sistema.

## Objetivo do Projeto

Nosso objetivo no Projeto Aplicado II de Ciência de Dados é desenvolver um modelo altamente preciso para reconhecimento de placas veiculares. Para alcançar isso, o modelo precisa realizar as seguintes tarefas:

1. Detectar placas veiculares em imagens de carros.
2. Aplicar processamento de imagem para segmentar a placa.
3. Aplicar OCR para extrair os caracteres da placa.

As metas do projeto são as ações a serem realizadas pelo modelo. Após o desenvolvimento do modelo, as próximas etapas na implementação efetiva do sistema são:

- Integrar o sistema de reconhecimento de placas com os sistemas de segurança existentes no condomínio.
- Realizar testes para validar a eficácia do sistema.
- Treinar a segurança do condomínio no uso do novo sistema.

### Dependências

* [OpenCV](https://opencv.org/): biblioteca de processamento de imagem, usada no pré-processamento de imagens, detecção de contorno e segmentação.
* [TensorFlow](https://www.tensorflow.org/): framework de aprendizado de máquina e deep learning usado no treinamento de modelo de reconhecimento de imagens.
* [PyTesseract](https://pypi.org/project/pytesseract/): interface para biblioteca OCR Tesseract, útil para reconhecer os caracteres das placas.
* [Matplotlib](https://matplotlib.org/) e [Seaborn](https://seaborn.pydata.org/): bibliotecas de visualização de dados e análise de resultados.
* [NumPy](https://numpy.org/) e [Pandas](https://pandas.pydata.org/): bibliotecas de manipulação e análise de dados padrão em Python.


### Apresentação do Projeto

A apresentação do projeto foi disponibilizada no YouTube. Clique nesse [link](https://www.youtube.com/watch?v=aALFHSPd3kQ) para acessar o vídeo.

### Relatório Técnico do Projeto

Ao final do projeto, um relatório técnico foi produzido e entregue para avaliação. Ele apresenta os elementos solicitados no início do projeto, como por exemplo, apresentação da organização, proposta analítica, análise exploratória de dados e os resultados pretendidos. Clique nesse [link](https://github.com/isaque-pimentel/projeto-aplicado-II/blob/main/Projeto%20Aplicado%20II%20-%20Relat%C3%B3rio%20T%C3%A9cnico.pdf) para acessar a versão final do relatório.

### Documentação do Projeto

A descrição de cada pasta no repositório é dada a seguir:
* `dataset`: contém o conjunto de dados (i.e., as etiquetas e as imagens em `annotations` e `images` respectivamente);
* `intermediate_reports`: contém o conjunto de relatórios intermediários que foram entregues nas etapas do projeto;
* `object_detection`: contém os históricos do processos de treinamento e validação com a ferramenta TensorBoard;
* `outputs`: contém diversos resultados intermediários que são salvos nessa pasta (para não ocupar muito espaço do repositório decidimos por não salvar esses dados aqui, apenas localmente);
* `script`: contém diversos scripts usados durante o processo de aprendizagem:
    * `parse_annotations.py`: Transforma os diferentes arquivos XML contendo as etiquetas em um único arquivo csv;
    * `verify_image.py`: Verifica se o quadro da etiqueta está corretamente assinalado para uma determinada imagem;
    * `read_data.py`: Realiza a leitura e renormalização das imagens em um array numpy tridimensional, assim como a leitura das etiquetas;
    * `train_model.py`: Realiza o treinamento do modelo usando o Keras e um modelo pré-treinado de Deep Learning chamado **Inception-ResNet-v2**;
    * `detect_place.py`: Realiza a leitura e renormalização das imagens de TEST para serem processadas pelo modelo, que fará a predição das quatro coordenadas (x_min, x_max, y_min, y_max) identificando a localização das placas;
    * `recognize_plate.py`: Realiza o processo de reconhecimento de caracteres a partir das placas identificadas usando a ferramenta Tesseract;
* `story`: contém as diferentes versões de storytelling que foram concebidas para esse projeto; 