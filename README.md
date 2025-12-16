# SAEPD - Sistema de Acompanhamento Escolar para Pais e Docentes


## 🎓 Informações do Projeto

| Instituição | Disciplina | Professor |
| :--- | :--- | :--- |
| **UFCA** | **[ADS0013] Projeto Integrado II** | Allysson Araújo |

## 📝 Descrição do Projeto

O **SAEPD** é um **Produto Mínimo Viável (MVP)** desenvolvido para **melhorar a comunicação** e o acompanhamento da vida acadêmica do aluno, fornecendo uma plataforma organizada e segura para pais/responsáveis.

### 🛠️ Arquitetura e Engenharia de Software

O sistema está sendo desenvolvido em **Python**, seguindo uma arquitetura robusta baseada em **Programação Orientada a Objetos (POO)** e separação de responsabilidades (Camadas de Serviço).

**Princípios de POO Aplicados:**

1.  **Abstração e Herança:** O sistema é fundado na classe abstrata `administrador` (definida em `Administrador.py`), que estabelece um contrato de métodos obrigatórios (Polimorfismo) para todos os perfis (`Professor`, `Responsavel`, `Administrador`).
2.  **Polimorfismo:** Todas as classes de de perfiis implementam o método `Velidar`, mas com lógicas e interfaces específicas para cada perfil.
3.  **Encapsulamento:** Atributos sensíveis (como senha e IDs) são protegidos com acesso controlado .

**Hierarquia de Classes Principal:**
O diagrama a seguir ilustra a fundação da arquitetura, mostrando a herança da classe base `Usuario` e suas conexões.

## 🌐 Possíveis Usos da Nossa Solução (Componente Extensionista)

O projeto Painel de Acompanhamento Escolar para Pais/Responsáveis (SAEPD) tem como objetivo principal oferecer uma plataforma integrada para que pais e responsáveis dos discentes matriculados **acompanhem em tempo real seu desempenho escolar**.

O painel centraliza informações de notas, frequência, comportamento e ocorrências, além de permitir comunicação direta entre responsáveis e professores. O sistema visa aumentar a transparência e fortalecer a parceria entre família e escola, promovendo um acompanhamento mais próximo do desenvolvimento acadêmico e comportamental dos estudantes. Com isso, espera-se melhorar o engajamento dos responsáveis e apoiar a tomada de decisões pedagógicas.

### 💡 Benefícios para o Mundo Real (Instituições de Ensino)

* **Eficiência e Segurança:** O SAEPD digitaliza processos (registro de notas, mensagens), substituindo métodos manuais e garantindo que as informações críticas sejam armazenadas e acessadas de forma segura.
* **Melhoria na Comunicação:** A plataforma centraliza a troca de mensagens e notificações de ocorrências, otimizando o tempo de resposta e a rastreabilidade das interações entre professores, responsáveis e secretaria.
* **Tomada de Decisão Pedagógica:** Ao fornecer dados em tempo real (notas, frequência), o sistema apoia os administradores e professores na identificação rápida de alunos em risco, permitindo intervenções pedagógicas mais ágeis.

## 👥 Divisão de Trabalho e Contribuições (Grupo - UFCA)

O trabalho foi dividido em três grandes módulos. **A responsabilidade é definida pelas tarefas**, e os membros devem preencher seu nome e matrícula ao assumirem o módulo.

| Integrante | Módulo de Responsabilidade | Contribuições Principais | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Ilma Rodrigues V. A. **Estrutura Base / Documentação** | `README.md`, criação das Classe Abstrata , Estrutura Inicial |
| **Francisco Jeferson Simplicio de Sousa**  | **Módulo de Comunicação** | `Mensagem`, `justificativa`, Repositório e Serviço de Mensagens | 
| **Gyan Carlos Mateus de Oliveira**  | **Módulo de Perfis** | Implementação da classe `Professor`, `Responsavel` e Repositório de Perfis | 
| **Erislanio Jaco da Silva**  | **Módulo de Perfis** | Implementação da classe `aluno`,`Perfil_professor` e Serviço de Autenticação (classes de Validação) | 
| **Francisco Jeferson Simplicio de Sousa**  | **Módulo Acadêmico** | Classes `Turma`, `Nota`, `Frequencia` e seus Repositórios | Pendente |
| **Jose Nataniel Gomes Pereira**  | **Módulo Acadêmico / Principal** | Classes `login`, `Administrador` (Lógica de Execução) | 


## ⚙️ Como Executar o Projeto (Getting Started)
executar --- python login.py

### Pré-requisitos
* Python 3.8 ou superior instalado.

### Instalação
```bash
# 1. Clonar o repositório
git clone [https://github.com/Jeffsimplicio/projetointegrado-POO-SAEPD.git](https://github.com/Jeffsimplicio/projetointegrado-POO-SAEPD.git)
cd projetointegrado-POO-SAEPD
# Projeto-integrado-POO-SAEPD
