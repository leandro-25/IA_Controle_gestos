# IA Controle - Controle de Paint e Volume por Gestos

Projeto de visão computacional que utiliza o reconhecimento de gestos de mão para o controle de duas funcionalidades no Windows:

- **Abrir e Fechar o Paint** — o gesto de um dedo abre o Microsoft Paint; o gesto de quatro dedos o fecha.
- **Ajustar o Volume** — o número de dedos levantados na mão direita define o volume do sistema, de 0% a 100%.

## Tecnologias Utilizadas

| Biblioteca | Finalidade |
|------------|------------|
| OpenCV | Captura de vídeo e processamento de imagens |
| cvzone (HandTrackingModule) | Rastreamento das mãos e reconhecimento de gestos |
| PyCaw | Controle do áudio do sistema |
| psutil | Verificação se o Paint está em execução |
| comtypes | Interface COM para o controle de volume |

## Requisitos

- Python 3.x
- Webcam
- Sistema Windows

## Instalação

Instale as dependências:

```bash
pip install opencv-python pycaw cvzone psutil comtypes
```

## Como Executar

```bash
python IA_controle.py
```

Pressione **Q** a qualquer momento para encerrar o programa.

## Funcionalidades

### 1. Abrir o Paint
Com um dedo levantado, o programa abre o Microsoft Paint (caso não esteja em execução).

### 2. Fechar o Paint
Com quatro dedos levantados, o programa encerra o Microsoft Paint (caso esteja em execução).

### 3. Controle de Volume (mão direita)
O volume do sistema é ajustado de acordo com o número de dedos levantados:

| Dedos levantados | Volume |
|------------------|--------|
| 0 | 0% |
| 1 | 20% |
| 2 | 40% |
| 3 | 60% |
| 4 | 80% |
| 5 | 100% |

## Estrutura do Projeto

```
IA_Controle/
├── IA_controle.py   # Código principal
└── README.md
```