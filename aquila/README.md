# 🦅 Aquila — AI Agent for Food Receipt Analysis

Aquila is an AI Agent designed to analyze and extract insights from food receipts using computer vision and natural language processing.

It provides an interactive Streamlit dashboard for users to chat, upload receipts, and visualize extracted data.

The system integrates local database storage and modular AI tools for extensibility.

## 📁 Project Structure
```bash
.
├── Dockerfile
├── README.md
├── aquila
│   ├── __init__.py
│   ├── agent
│   │   ├── agent.py           # Core AI agent logic
│   │   └── helper.py          # Agent utilities and support functions
│   ├── config.py              # Configuration and environment variables
│   ├── dashboard
│   │   ├── Welcome.py         # Dashboard landing page
│   │   └── pages
│   │       ├── 1_Chat.py      # Chat interface with AI agent
│   │       ├── 2_Upload.py    # Upload and process receipt images
│   │       └── 3_Data.py      # Data preview
│   ├── data
│   │   ├── food_receipts.db   # Local SQLite database
│   │   └── sample             # Example receipt images
│   │       ├── IMG_3594.PNG
│   │       ├── IMG_3614.PNG
│   │       └── IMG_3627.PNG
│   ├── logging.py             # Custom logging setup
│   └── tools
│       ├── database.py        # Database interactions
│       ├── extract.py         # text extraction utilities
│       └── helper.py          # Shared helper functions
├── poetry.lock
├── pyproject.toml             # Project dependencies and build metadata
└── scripts
    └── init.sh                # Initialization or setup script
```

## ⚙️ Installation
1. Clone the Repository
```bash
git clone <this-repo-url>
cd SHOPEE_AI_ENGINEER_CASE_STUDY/aquila/
conda create -n aquila python=3.10 -y
conda activate aquila
```
2. Install Dependencies (using Poetry)
```
pip install poetry==2.2.1
poetry install
```
3. Environment Variables
Create a .env file in the project root:
```
GOOGLE_API_KEY=your_api_key
MODEL_NAME=gemini-2.5-flash
MODEL_PROVIDER=google_genai

DB_NAME=food_receipts.db
DB_PATH=./aquila/data/food_receipts.db
```

## 🚀 Run the Application
Run Locally via Poetry
```bash
poetry run streamlit run aquila/dashboard/Welcome.py
```
Or Use Docker

Build and run the containerized version:
```bash
docker build -t aquila .
docker run -p 8501:8501 aquila
```
Then open your browser at http://localhost:8501

## 🧠 Features
- 💬 Chat Interface — Interact with an AI Agent to ask questions about your spending.
- 🗂️ Upload Receipts — Upload food receipt images for extraction.
- 📊 Data View — Explore parsed data stored in SQLite.

## 🧱  Modules Overview
| Module                 | Description                                         |
| ---------------------- | --------------------------------------------------- |
| `agent/agent.py`       | Defines the AI agent logic and reasoning flow       |
| `tools/extract.py`     | Handles OCR and text extraction from receipt images |
| `tools/database.py`    | Connects to SQLite DB and manages CRUD              |
| `tools/retrieve.py`    | Performs local search and data retrieval            |
| `dashboard/pages/*.py` | Streamlit UI for chat, upload, and data preview     |

## 🧭 Future Improvements
- Integrate semantic search for similar receipts
- Connect to cloud-based vector database
- Enhanced dashboard with user login and analytics
- User & Agent History Trackingz