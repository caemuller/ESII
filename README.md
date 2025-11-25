# Trabalho Prático — Microsserviços de Câmbio

Este projeto implementa dois microsserviços para consulta de dados de câmbio (report e histórico), integrados via Docker Compose e com pipeline de CI configurado.

## Tecnologias
- Python (FastAPI)
- Docker & Docker Compose
- GitHub Actions (CI)

## Passos para subir o ambiente

Certifique-se de ter o Docker e o Docker Compose instalados.

1. Na raiz do projeto, execute:
   ```bash
   docker compose up --build
   ```

2. Aguarde os logs indicarem que as aplicações iniciaram.

## Testar (Endpoints)

### Microsserviço A (Currency Report) - Porta 8100

* **Health Check:**
  ```bash
  curl http://localhost:8100/health
  # Resposta esperada: {"status": "UP"}
  ```

* **Obter Cotação:**
  ```bash
  curl "http://localhost:8100/quote?from=USD&to=BRL"
  ```

### Microsserviço B (Currency History) - Porta 8101

* **Health Check:**
  ```bash
  curl http://localhost:8101/health
  ```

* **Obter Histórico:**
  ```bash
  curl "http://localhost:8101/history?from=USD&to=BRL"
  ```

### Uso de IA Generativa

Foi utilizado o github copilot para realizar tarefas especialmente nos arquivvos .yaml nas aprtes de estrutura e os dockerfiles em geral.
O codigo foi revisado e testado pelos alunos