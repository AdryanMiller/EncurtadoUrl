
---

# [Encurtador de Links]

> 💡 Transformando complexidade em simplicidade conectando pessoas ao seu destino final de maneira rapida.

---

## 📝 Descrição


Encurtador de link, pegando uma url longa e a transformando em uma curta, facilitando assim o seu uso, manuseio e diminuindo seu tamanho para um melhor entendimento.
Muitas urls sao grandes, sendo ruins de guardar, enviar e sem contar que confusas. Para melhorar isso encurtar um link seria muito bom para estes momentos, ajudando nao so esteticamente mas como manuseios das urls

---

## ⚡ Tecnologias e Ferramentas (Stack)

Listas de tecnologias usadas neste projeto.

* **Backend:** Python, Flask.
* **Banco de Dados:** SQLite3.
* **Ferramentas e Bibliotecas:** Flask, Os, sqlite3, dotenv.

---

## 🏗️ Arquitetura

Organizaçao do codigo e suas estruturas, e o porque da arquitetura

### Estrutura de Pastas

```text
ENCURTADORURL/
├──app/
    ├── database/        # Conexao banco e inicializacao
    ├── repository/      # Camada de persistência e acesso a dados
    ├── service/         # Definição das entidades e regras de negócio
    ├── routes/          # Criacao de rotas 
    ├── utils/           # Criacao de utilizaveis
    ├── templates/       # Paginas HTML 
    └── static/          # Estilizacao CSS

```

### O Porquê da Arquitetura

 Utilizamos o padrao de Arquitetura em Camadas **(Layered Architecture)** para separar as regras de negocio das decisoes de infraestrutura e desing, facilitando a manutençao e a criaçao de testes unitarios isolados.

---

## 🛠️ Decisões Técnicas

Aqui você justifica as escolhas críticas de design e engenharia que moldaram o projeto.

* **Escolha do Banco [SQLlite3]:** Optou-se por [SQL] devido à necessidade integridade e consistencia e escabilidade futuramente. Banco simplificado para o projeto, futuramente com uma escala trocariamos para MySQL mais completo e mais estrutural.

---

## 🚀 Funcionalidades (Features)

O que o sistema e capaz de fazer atualmente.

* ✅ Encurtar link longo para curto.
* ✅ Verificacao de URL.
* ✅ Nomarlizacao de URLs.

---

## 🛑 Fora do Escopo

O que o projeto **não faz** atualmente e seus motivos.

* ❌ **URLs diferentes de HTTP:** Fora do escopo atual devido a complexidade de normalizacao.
* ❌ **Autenticacao e Login:** Fora do escopo atual devido à falta de nescessidade no momento.
* ❌ **Expiração de links:** Fora do escopo atual devido a robustes que o projeto retia para o momento.
* ❌ **Cache:**  Fora do escopo atual devido a complexidade que o projeto estaria.
* ❌ **MySQL:**  Fora do escopo atual pois o SQLite3 supre as nescessidade no momento, caso o projeto escalhe trocariam o banco.
---

## 🔄 Melhorias Futuras

Melhorias futuras que o projeto haverar.

* 🔲 Expiração de links.
* 🔲 URLs personalizadas.
* 🔲 Autenticação e login.
* 🔲 Cache.
* 🔲 contagem de acessos.

---

## 💻 Como Rodar o Projeto

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

* [Tecnologia base: Python 3.14]
* [Gerenciador de pacotes: Pip]

### Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/AdryanMiller/EncurtadoUrl/tree/master
cd seu-repositorio

```
2. **Criacao e ativacao de venv:**
```bash
#criacao de venv
python -m venv venv 

#Ativando venv via Powershell
.\venv\Scripts\Activate.ps1

#Ativando venv via CMD
venv\Scripts\activate.bat

```

3. **Configure as variáveis de ambiente:**
```bash
cp .env.example .env
# Abra o arquivo .env e preencha com suas credenciais locais

```


4. **Instale as dependências:**
```bash
# Exemplo para Python/Pip
pip install -r requirements.txt

```


5. **Inicie o servidor de desenvolvimento:**
```bash
# Comando para rodar no terminal
python main.py
```


O servidor estará ativo em `http://localhost:5000`.

---