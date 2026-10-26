# LoginShield-Python
Simulador de análise de riscos em tentativas de login, desenvolvido em Python.
![Uploading image.png…]()
# 🔐 LoginShield — Analisador de Logins Suspeitos

## 📌 Sobre o projeto

O LoginShield é um simulador educativo de análise de riscos em tentativas de login, desenvolvido em Python após a conclusão do curso Python 3 — Mundo 1 do Curso em Vídeo.

O sistema analisa informações fornecidas pelo usuário e calcula uma pontuação para classificar o acesso em risco baixo, médio ou alto.

## ⚙️ Funcionalidades

- Identificação do usuário
- Análise do país de origem
- Identificação de acessos em horários suspeitos
- Análise de tentativas incorretas de senha
- Verificação de dispositivos desconhecidos
- Classificação de risco com cores no terminal

## 📊 Regras de pontuação

| Condição | Pontuação |
|---|---:|
| Acesso fora do Brasil | +30 |
| Horário entre 00:00 e 05:59 | +15 |
| 3 ou mais tentativas incorretas | +25 |
| Dispositivo desconhecido | +30 |

### Classificação

- **0–24 pontos:** Risco baixo
- **25–59 pontos:** Risco médio
- **60–100 pontos:** Risco alto

## 🛠️ Tecnologias utilizadas

- Python 3
- Módulo datetime
- Estruturas condicionais (if, elif, else)
- Operadores relacionais e lógicos
- Manipulação de strings

## ▶️ Como executar

1. Instale o Python 3.
2. Baixe o arquivo `projetoAnalisadorLogin.py`.
3. Abra um terminal na pasta do arquivo.
4. Execute:

```bash
python projetoAnalisadorLogin.py
```

5. Responda às perguntas exibidas no terminal.

## 📚 Objetivo

Aplicar fundamentos de Python em um projeto relacionado à segurança da informação, desenvolvendo a lógica de classificação de riscos por meio de regras condicionais.

**Observação:** Este projeto é uma simulação educativa e não representa um sistema real de detecção ou prevenção de invasões.

## 👨‍💻 Desenvolvedor

Leonardo Giovanini

Graduado em Análise e Desenvolvimento de Sistemas, estudando Python, Inteligência Artificial e Cibersegurança.
