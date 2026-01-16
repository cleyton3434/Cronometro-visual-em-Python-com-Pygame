# ⏱️ Cronômetro Visual em Pygame

Projeto de cronômetro múltiplo desenvolvido em Python com Pygame, focado em uso educacional
(aulas, atividades cronometradas, dinâmicas em sala).

## 🚀 Funcionalidades
- Múltiplos cronômetros simultâneos
- Alerta sonoro e visual ao finalizar o tempo
- Execução automática em sequência
- Interface leve e flutuante (sem bordas)
- Arrastar a janela pela lateral

## 🧠 Motivação
Este projeto nasceu da necessidade de um cronômetro simples, visual e eficiente
para uso em aulas de programação.

## 🛠️ Tecnologias
- Python
- Pygame

## ▶️ Como executar
```bash
pip install -r requirements.txt
python Relogio.py
🕹️ Como usar o aplicativo
▶️ 1. Abrindo o aplicativo

Após executar o comando:

python Relogio.py


Uma janela flutuante será exibida sem bordas, com um painel lateral à esquerda.

➕ 2. Adicionar um cronômetro

Clique no botão + no canto superior esquerdo

Um novo cronômetro será criado automaticamente

Você pode adicionar quantos cronômetros quiser.

⏱️ 3. Ajustar o tempo

Cada cronômetro possui dois botões:

▲ min → adiciona 1 minuto

▼ seg → remove 10 segundos

O tempo ajustado será salvo como tempo inicial do cronômetro.

▶️ 4. Iniciar ou pausar o cronômetro

Clique no botão ▶ (play)

O mesmo botão serve para iniciar e pausar

🔔 5. Alerta de tempo esgotado

Quando o tempo chega a 00:00:

Um som de alerta é reproduzido

O cronômetro pisca em vermelho

A mensagem “TEMPO ESGOTADO” aparece por alguns segundos

🔁 6. Execução automática em sequência

Se houver mais de um cronômetro:

Ao finalizar um cronômetro

O próximo inicia automaticamente

Ideal para:

Aulas

Dinâmicas

Rodízio de atividades

🔄 7. Resetar o cronômetro

Atualmente, para resetar:

Ajuste novamente o tempo usando os botões ▲ min ou ▼ seg

Ou pause e reinicie manualmente

(Sugestão futura: botão de reset dedicado)

❌ 8. Remover um cronômetro

Clique no botão X no canto superior direito do cronômetro

Ele será removido da tela

🖱️ 9. Mover a janela

Clique e segure a barra lateral esquerda

Arraste para mover a janela pela tela

💡 Dicas de uso

Use vários cronômetros para controlar etapas da aula

Combine tempos curtos para atividades rápidas

Ideal para professores, tutores e apresentações



🤝 Contribuições!!!!!!!!!

Contribuições são muito bem-vindas!

Ideias de melhorias:

Interface mais acessível

Configuração via teclado

Exportar presets de tempo

Suporte a fullscreen

Internacionalização (PT/EN)

Como contribuir

Faça um fork do projeto

Crie uma branch (feature/minha-melhoria)

Commit suas mudanças

Abra um Pull Request
