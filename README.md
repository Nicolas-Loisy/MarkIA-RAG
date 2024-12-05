# MarkIA-RAG

[![Python](https://img.shields.io/badge/Python-3.11.3-blue)](https://www.python.org/downloads/release/python-3113/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-green)](https://flask.palletsprojects.com/en/2.3.x/)
[![Koyeb](https://img.shields.io/badge/Hosting-Koyeb-orange)](https://www.koyeb.com/)

Une API Flask pour un chatbot, sécurisée et optimisée pour l'échange de texte en JSON. Hébergée sur [Koyeb](https://www.koyeb.com/) avec des configurations avancées de sécurité.

## 📖 Table des matières

- [Fonctionnalités](#✨-fonctionnalités)
- [Installation](#🚀-installation)
- [Commandes](#🛠️-commandes-à-exécuter)
- [Hébergement (Koyeb)](#🌐-hébergement-koyeb)
- [Commandes](#⚙️-commandes)

## ✨ Fonctionnalités

- **Échange JSON** : Permet de recevoir et d'envoyer des messages en JSON.
- **Sécurité avancée** :
  - Limitation des requêtes avec Flask-Limiter.
  - Configuration stricte de la politique de sécurité (CSP).
  - Support HTTPS (via Koyeb).
- **Facilement déployable** sur [Koyeb](https://www.koyeb.com/).

## 🚀 Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/Nicolas-Loisy/MarkIA-RAG.git
   cd MarkIA-RAG
   ```

2. **Créer un environnement virtuel :**

   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Commandes à exécuter

1. **Lancer le serveur en local :**

   ```bash
   flask run
   ```

   - L'API sera accessible par défaut sur `http://127.0.0.1:5000`.

2. **Tester avec `curl` ou un outil comme Postman**

## 🌐 Hébergement (Koyeb)

### Étapes pour déployer sur Koyeb

## ⚙️ Commandes

```
python -m eurelis_llmatoolkit.llamaindex.console -config="config.json" dataset cache
```

```
python -m eurelis_llmatoolkit.llamaindex.console -config="config.json" dataset ingest
```

```
python -m eurelis_llmatoolkit.llamaindex.console -config="config.json" dataset ingest --from_cache
```

```
python -m eurelis_llmatoolkit.llamaindex.console -config="config.json" chatbot --query="Tell me about Sage ERP" --id_conversation="test_conv" chat
```
