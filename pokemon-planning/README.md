# Pokémon Card Storage Web App - Planning & Documentation

## Overview
This document outlines the design and planning for the Pokémon Card Storage Web App project (Diagrams). The app includes role-based access for users and admins, card/deck management, and an approval system for submitted cards.

---

## 1. Entity-Relationship Diagram (ERD)

```mermaid
erDiagram
    USER ||--o{ DECK : owns
    USER ||--o{ CARD_SUBMISSION : submits
    ADMIN ||--o{ CARD : manages

    DECK ||--o{ DECK_CARD : includes
    CARD ||--o{ DECK_CARD : appears_in

    USER {
        int user_id
        string username
        string email
        string role
    }

    CARD {
        int card_id
        string name
        string type
        string rarity
        int attack
        int defense
        boolean approved
    }

    DECK {
        int deck_id
        string name
        int user_id
    }

    DECK_CARD {
        int deck_id
        int card_id
    }

    CARD_SUBMISSION {
        int submission_id
        int user_id
        int card_id
        date submitted_at
        string status
    }
    
}

```
---

## 2. User Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B{Is User Logged In?}
    B -- No --> C[View Cards]
    B -- Yes --> D{User or Admin?}
    D -- User --> E[Submit New Card]
    E --> F[Pending Approval]
    D --> G[Create/Edit Deck]
    G --> H[Manage Deck (Add/Remove Cards)]
    D -- Admin --> I[Review Submissions]
    I --> J[Approve or Reject Cards]
    J --> K[Edit/Delete Existing Cards]
    C --> L[End]
    H --> L
    K --> L
    }

```

---

## 3. System Architecture Diagram

```mermaid
graph TD
    A[Frontend (React/HTML)] -->|HTTP Requests| B[Backend (Flask API)]
    B --> C[Database (PostgreSQL/MySQL)]

    subgraph Users
        U1[Regular User]
        U2[Admin User]
    end

    U1 --> A
    U2 --> A

    A -->|GET /cards| B
    A -->|POST /cards (submit)| B
    A -->|POST /decks| B
    A -->|PUT/DELETE decks| B
    U2 -->|POST /cards (add)| B
    U2 -->|PUT/DELETE cards| B
    U2 -->|GET /submissions| B
    B -->|SQL Queries| C
    }
```
---
## 4. API Endpoints

| Endpoint                | Method | Description                         | Auth Required | Role  |
| ----------------------- | ------ | ----------------------------------- | ------------- | ----- |
| `/cards`                | GET    | View all approved cards             | No            | All   |
| `/cards`                | POST   | Submit a new card                   | Yes           | User  |
| `/cards/:id`            | PUT    | Update existing card                | Yes           | Admin |
| `/cards/:id`            | DELETE | Delete a card                       | Yes           | Admin |
| `/submissions`          | GET    | View pending card submissions       | Yes           | Admin |
| `/submissions/:id`      | PUT    | Approve or reject a card submission | Yes           | Admin |
| `/decks`                | POST   | Create a new deck                   | Yes           | User  |
| `/decks/:id`            | PUT    | Edit an existing deck               | Yes           | User  |
| `/decks/:id`            | DELETE | Delete a deck                       | Yes           | User  |
| `/decks/:id/cards`      | POST   | Add a card to a deck                | Yes           | User  |
| `/decks/:id/cards/:cid` | DELETE | Remove a card from a deck           | Yes           | User  |

