# 🚀 Floating Jetpack

Um jogo 2D estilo *Flappy Bird* com mecânica de jetpack, desenvolvido em Python utilizando **Pygame**.
Desvie dos obstáculos, sobreviva o máximo possível e veja até onde você consegue chegar!

---

## 🎮 Gameplay

* Controle um personagem com jetpack
* Desvie de obstáculos gerados dinamicamente
* Sistema de pontuação progressiva
* A dificuldade aumenta conforme você avança
* Sistema de níveis (Level System)
* Tela de menu e game over

---

## 🧠 Mecânicas

* Pressione **SPACE** para voar
* Evite colidir com obstáculos ou sair da tela
* Ganhe pontos ao passar pelos obstáculos
* A cada 10 pontos:

  * A velocidade aumenta
  * O espaço entre obstáculos diminui
  * O jogo fica mais desafiador 🔥

---

## 🖼️ Preview

> <img width="797" height="628" alt="gameplay" src="https://github.com/user-attachments/assets/d3bdf4ce-3992-41d8-8562-7ecd39ddf4ec" />
<img width="797" height="631" alt="menu" src="https://github.com/user-attachments/assets/6175273c-058b-480e-8bbf-f70c1d892914" />



---

## 🛠️ Tecnologias utilizadas

* Python 3
* Pygame

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/floating-jetpack.git
cd floating-jetpack
```

Crie um ambiente virtual (opcional):

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como rodar

```bash
python main.py
```

---

## 🧾 Estrutura do projeto

```
Floating-Jetpack/
│
├── main.py
├── player.py
├── obstacle.py
├── menu.py
├── settings.py
├── requirements.txt
├── .gitignore
│
└── assets/
    ├── images/
    └── sounds/
```

---

## 🏗️ Build (.exe)

Para gerar o executável:

```bash
pyinstaller --onefile --noconsole --add-data "assets;assets" main.py
```

O arquivo será gerado em:

```
dist/main.exe
```

---

## 🎨 Assets

Os assets utilizados (imagens e sons) são de uso livre ou adaptados para fins educacionais.

---

## 👨‍💻 Autor

Desenvolvido por **Walisson Santiago**

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.
