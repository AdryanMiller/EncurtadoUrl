
---

# Documento de Contexto — Projeto Encurtador de URL

## Objetivo do projeto

Construir um encurtador de URL simples usando **Python + Flask + SQLite3**, focado em aprendizado, arquitetura e construção de portfólio para estágio.

O objetivo não é criar um produto completo, mas um sistema pequeno, funcional e bem estruturado.

---

# Escopo Atual

## Funcionalidades que existirão

* Receber uma URL longa
* Validar entrada
* Normalizar URL
* Salvar URL no banco
* Gerar URL curta usando **ID incremental + Base62**
* Redirecionar URL curta para URL original

---

## Funcionalidades que NÃO existirão agora

Esses itens foram removidos do escopo para manter simplicidade:

* autenticação
* login
* cache
* expiração de links
* contagem de acessos
* analytics
* URLs personalizadas
* rate limiting
* controle anti spam
* MySQL
* histórico
* soft delete

Podem existir futuramente.

---

# Stack

## Backend

* Python

## Framework

* Flask

## Banco

* SQLite3 puro

## ORM

* Não usar ORM

---

# Arquitetura

Projeto dividido em camadas.

Fluxo:

```text
Route
↓
Service
↓
Repository
↓
Database
```

Utilitários separados.

---

# Estrutura de Pastas

```text
app/
├── routes/
│   └── url_routes.py

├── service/
│   └── url_service.py

├── repository/
│   └── url_repository.py

├── database/
│   └── connection.py

├── utils/
│   └── base62.py

└── main.py
```

---

# Responsabilidades

## routes/

Responsável por:

* receber requisição HTTP
* validar formato básico
* retornar resposta

Não contém regra de negócio.

---

## service/

Responsável por:

* coordenar fluxo
* normalizar URL
* chamar repository
* chamar Base62
* controlar regras da aplicação

Não executa SQL.

---

## repository/

Responsável por:

* executar SQL
* inserir registros
* buscar registros

Não contém regra de negócio.

---

## database/

Responsável por:

* criar conexão com SQLite

---

## utils/base62.py

Responsável por:

* converter ID → Base62
* converter Base62 → ID

Sem acesso ao banco.

---

# Banco de Dados

Tabela:

```sql
urls
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    created_at DATETIME
)
```

---

## Decisão Importante

NÃO armazenar:

```text
short_code
```

O código será gerado dinamicamente:

```text
short_code = Base62(id)
```

Motivo:

* menos complexidade
* menos redundância
* projeto mais simples

---

# Fluxo — Criar URL

```text
Receber URL
↓
Validar entrada
↓
Normalizar URL
↓
Salvar no banco
↓
Banco gera ID
↓
Converter ID → Base62
↓
Retornar URL curta
```

Exemplo:

```text
POST /shorten

google.com

↓

https://google.com

↓

id = 125

↓

base62(125)

↓

cb

↓

localhost:5000/cb
```

---

# Fluxo — Redirecionar

```text
GET /cb

↓

Validar código

↓

Base62 → ID

↓

Buscar no banco

↓

Redirecionar
```

Exemplo:

```text
GET /cb

↓

decode

↓

125

↓

SELECT

↓

redirect()
```

---

# Estratégia de Normalização

Entrada:

```text
google.com
```

Resultado:

```text
https://google.com
```

Regras:

1. remover espaços
2. verificar esquema
3. se faltar → adicionar https://
4. validar resultado
5. salvar normalizada

Exemplos:

```text
google.com
→ https://google.com

https://google.com
→ manter

http://google.com
→ manter
```

---

# Estratégia para URLs Iguais

Não haverá deduplicação.

Exemplo:

```text
https://google.com
→ /b

https://google.com
→ /c
```

Cada requisição gera um novo link.

Motivo:

* implementação simples
* menos consultas
* independência entre criações

---

# Tratamento de Erros

```text
400 → entrada inválida

404 → URL não encontrada

500 → erro interno
```

Exemplos:

```text
GET /$$$$
→ 400

GET /abc
(não existe)
→ 404

erro no banco
→ 500
```

---

# Exclusão

No momento não implementar.

Se existir futuramente:

* usar DELETE
* apagar registro diretamente
* sem histórico

---

# Possíveis melhorias futuras

* MySQL
* URLs customizadas
* cache
* analytics
* contagem de acesso
* autenticação
* limite de requisições
* expiração

---

# Filosofia do Projeto

Não adicionar funcionalidade sem requisito.

Prioridade:

```text
terminar
>
deixar preparado para tudo
```

Objetivo principal:

```text
mostrar arquitetura
+
mostrar organização
+
mostrar entendimento de fluxo HTTP
+
mostrar separação de responsabilidades
```

---

Esse documento representa o estado atual do projeto e deve ser usado como contexto para continuar a implementação.
