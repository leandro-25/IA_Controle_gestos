# IA Controle de Gestos

Reconhecimento de gestos de mão pela webcam para controlar o Windows: abria/fecha o Microsoft Paint e ajusta o volume do sistema de 0% a 100%.

## 📸 Demonstração

> Em breve — gravando um vídeo com a detecção das mãos e as ações sendo executadas.

Enquanto isso, execute localmente e observe a janela `Detecção de Gestos`:

```bash
python IA_controle.py
```

## ✨ Funcionalidades

| # | Funcionalidade | Entrada | Efeito |
|---|----------------|---------|--------|
| 1 | **Abrir o Paint** | Mão esquerda com 1 dedo levantado | `start mspaint` |
| 2 | **Fechar o Paint** | Mão esquerda com 4 dedos levantados | `taskkill /f /im mspaint.exe` |
| 3 | **Controle de volume** | Mão direita com 0 a 5 dedos | Volume do sistema em 0% / 20% / 40% / 60% / 80% / 100% |

Detalhes do volume:

| Dedos levantados (mão direita) | Volume |
|--------------------------------|--------|
| 0 | 0% |
| 1 | 20% |
| 2 | 40% |
| 3 | 60% |
| 4 | 80% |
| 5 | 100% |

- Espelhamento horizontal da imagem (`cv2.flip`) para a interação ficar natural.
- Verificação via `psutil` antes de abrir/fechar o Paint, evitando ações duplicadas.
- Cada gesto dispara **uma única vez** — a ação só ocorre quando o gesto muda, sem repetir a cada frame.
- Mão esquerda e mão direita são tratadas de forma independente.
- Pressione **Q** para encerrar.

## 🛠️ Tecnologias

| Biblioteca | Finalidade |
|------------|------------|
| [OpenCV](https://pypi.org/project/opencv-python/) | Captura de vídeo, espelhamento e exibição da janela |
| [cvzone](https://pypi.org/project/cvzone/) (`HandTrackingModule`) | Detecção e rastreamento das mãos (MediaPipe) |
| [PyCaw](https://pypi.org/project/pycaw/) | Controle do volume do sistema (Windows Core Audio) |
| [comtypes](https://pypi.org/project/comtypes/) | Acesso à interface COM `IAudioEndpointVolume` |
| [psutil](https://pypi.org/project/psutil/) | Verificar se o `mspaint.exe` está em execução |

## 📦 Instalação

Pré-requisitos:

- **Windows** (PyCaw e `taskkill` são específicos da plataforma)
- **Python 3.x**
- **Webcam** funcionando

Crie um ambiente virtual (recomendado) e instale as dependências:

```bash
python -m venv .venv
.venv\Scripts\activate

pip install opencv-python pycaw cvzone psutil comtypes
```

> O `cvzone` instala o `mediapipe` automaticamente como dependência.

## ⚙️ Configuração

Ajuste em `IA_controle.py`, se necessário:

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `CAMERA_INDEX` | `0` | Índice da câmera. Use `1`, `2`... se tiver mais de uma webcam |
| `DETECTION_CON` | `0.7` | Confiança mínima de detecção. Reduza para detectar mais fácil, aumente para reduzir falsos positivos |
| `ajustarVolume()` | `0.0` a `1.0` | Faixa de volume aplicada ao sistema |

Permissões: a webcam precisa estar liberada para o terminal/IDE e o microfone/áudio não é usado (apenas saída de áudio).

## 🚀 Como usar

```bash
python IA_controle.py
```

1. Posicione-se a cerca de 40–60 cm da webcam, com boa iluminação.
2. Mostre a **mão esquerda** para controlar o Paint (1 dedo = abrir, 4 dedos = fechar).
3. Mostre a **mão direita** para controlar o volume (0–5 dedos = 0% a 100%).
4. Pressione **Q** na janela de vídeo para sair.

## 📁 Estrutura do projeto

```
IA_Controle_gestos/
├── IA_controle.py   # Código principal
├── README.md        # Documentação
└── LICENSE          # Licença MIT
```

## 🧪 Testes

Testes manuais (não há suite automatizada):

| Cenário | Esperado |
|---------|----------|
| Mão esquerda, 1 dedo, Paint fechado | Paint abre |
| Mão esquerda, 4 dedos, Paint aberto | Paint fecha |
| Mão direita, 0 dedos | Volume em 0% |
| Mão direita, 5 dedos | Volume em 100% |
| Nenhuma mão na frente da câmera | Janela apenas exibe o vídeo, sem ações |
| Tecla **Q** | Programa encerra e libera a câmera |

## 🚢 Deploy

Este é um aplicativo desktop local — **não há etapa de deploy**.

Para distribuição:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole IA_controle.py
```

O binário gerado fica em `dist/IA_controle.exe` e pode ser copiado para qualquer máquina Windows com Python não instalado.

## 🗺️ Roadmap

- [ ] Suporte a gestos personalizados (mão aberta, punho, pinça)
- [ ] Controle de mídia (play/pause, próxima/faixa anterior)
- [ ] Ajuste fino do volume por distância dos dedos, em vez de faixas fixas
- [ ] Calibração automática de fundo e iluminação
- [ ] Interface gráfica para escolher câmera e sensibilidade
- [ ] Suporte a Linux/macOS (volume via `pulsectl` / `osascript`)

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Faça um fork do repositório.
2. Crie uma branch: `git checkout -b feature/minha-melhoria`
3. Faça suas alterações e committe: `git commit -m "Adiciona minha melhoria"`
4. Envie para o fork: `git push origin feature/minha-melhoria`
5. Abira um **Pull Request** descrevendo o que mudou e por quê.

Por favor, mantenha o código simples e documente gestos novos na tabela de funcionalidades.

## 📄 Licença

Distribuído sob a licença [MIT](LICENSE).
