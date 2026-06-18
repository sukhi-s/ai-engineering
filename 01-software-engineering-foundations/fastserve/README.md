# FastServe

## Overview

FastServe is a FastAPI-based backend service that exposes a REST API for managing prompts.

The project is designed to teach the foundations of backend engineering that are commonly used in AI systems and developer platforms.

Instead of building a simple "Hello World" API, FastServe implements a Prompt Vault where prompts can be created, retrieved, updated, listed, and deleted through HTTP endpoints.

The project introduces the architecture patterns found in production systems, including routing, validation, service layers, and storage layers.

---

## Learning Objectives

This project introduces:

* FastAPI
* REST APIs
* HTTP requests and responses
* CRUD operations
* Pydantic validation
* Route design
* Service layer architecture
* Storage abstraction
* API documentation
* Backend application structure

These concepts form the foundation of:

* AI APIs
* RAG services
* Agent platforms
* Evaluation systems
* Prompt management systems
* Internal developer tooling

---

## Project Structure

```text
fastserve/
│
├── README.md
├── requirements.txt
│
└── fastserve/
    ├── __init__.py
    ├── main.py
    ├── routes.py
    ├── models.py
    ├── service.py
    └── storage.py
```

---

## Architecture

```text
Client
  │
  ▼
HTTP Request
  │
  ▼
Route Layer
  │
  ▼
Validation Layer
  │
  ▼
Service Layer
  │
  ▼
Storage Layer
  │
  ▼
HTTP Response
```

Each layer has a single responsibility.

---

## File Responsibilities

### main.py

Application entry point.

Responsibilities:

* Create FastAPI application
* Register routes
* Start API service

---

### routes.py

API endpoint definitions.

Responsibilities:

* Receive requests
* Validate incoming data
* Call service functions
* Return responses

Example endpoints:

```http
POST /prompts
GET /prompts
GET /prompts/{prompt_id}
PUT /prompts/{prompt_id}
DELETE /prompts/{prompt_id}
```

---

### models.py

Pydantic data models.

Responsibilities:

* Request validation
* Response validation
* Type safety

Example models:

```text
PromptCreate
PromptUpdate
PromptResponse
```

---

### service.py

Business logic layer.

Responsibilities:

* Create prompts
* Retrieve prompts
* Update prompts
* Delete prompts

The service layer contains application behaviour and business rules.

---

### storage.py

Storage abstraction layer.

Responsibilities:

* Persist data
* Retrieve stored data

For Version 1, prompts are stored in memory using a Python dictionary.

Future versions may use:

* SQLite
* PostgreSQL
* DynamoDB
* Redis

without changing the service layer.

---

## API Endpoints

### Create Prompt

```http
POST /prompts
```

Creates a new prompt.

---

### List Prompts

```http
GET /prompts
```

Returns all prompts.

---

### Get Prompt

```http
GET /prompts/{prompt_id}
```

Returns a specific prompt.

---

### Update Prompt

```http
PUT /prompts/{prompt_id}
```

Updates an existing prompt.

---

### Delete Prompt

```http
DELETE /prompts/{prompt_id}
```

Removes a prompt.

---

## Execution Flow

Creating a prompt:

```text
Client
  │
  ▼
POST /prompts
  │
  ▼
Route
  │
  ▼
Pydantic Validation
  │
  ▼
Service Layer
  │
  ▼
Storage Layer
  │
  ▼
Response
```

---

## Running The Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn fastserve.main:app --reload
```

---

## Interactive API Documentation

FastAPI automatically generates API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

The documentation allows every endpoint to be tested directly from the browser.

---

## Key Takeaway

FastServe demonstrates how modern backend services are structured.

The project introduces layered architecture where responsibilities are separated into routes, models, services, and storage.

This same pattern appears in production AI systems, including RAG applications, agent platforms, model gateways, and evaluation frameworks.
