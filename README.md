# AI-powered-Skill-assessment-Personalized-Growth-Navigators


##Requirements Setting
Need to install VS Studio before installing the libraries


## 📁 Project Structure

intelligent-skill-assessment-system/
│
├── app/                        # 🎯 Frontend Streamlit app
│   ├── main.py                 # Entry point (Streamlit UI)
│   ├── pages/                  # Additional Streamlit pages
│   │   └── dashboard.py
│   └── components/             # Custom UI components (buttons, cards, etc.)
│
├── agents/                     # 🤖 Agent & LLM Orchestration logic
│   ├── skill_evaluator.py      # CrewAI/LangGraph/SmolAgents agent definition
│   └── prompt_templates.py     # Prompt templates for different skills
│
├── data/                       # 📊 Datasets and test data
│   ├── raw/                    # Original unprocessed data
│   ├── processed/              # Cleaned, filtered data
│   └── sample_inputs/          # Example questions, answers, etc.
│
├── notebooks/                  # 📒 Jupyter notebooks for data exploration
│   └── analysis.ipynb          # Exploratory skill metrics or model testing
│
├── logic/                      # 🧠 Core business logic
│   ├── evaluation.py           # Skill scoring/ranking logic
│   └── utils.py                # Common utilities
│
├── configs/                    # ⚙️ YAML/JSON config files
│   ├── app_config.yaml         # App-level settings
│   └── prompts_config.yaml     # Prompt parameters and roles
│
├── assets/                     # 🖼️ Static assets (images, logos, icons)
│   └── logo.png
│
├── tests/                      # ✅ Unit and integration tests
│   └── test_skill_eval.py
│
├── .env                        # 🔐 Environment variables (API keys etc.)
├── requirements.txt            # 📦 Python dependencies
├── README.md                   # 📘 Project overview
└── run.sh                      # 🚀 Script to launch the system

##Notes:
- No needs to use Vector Database as there are no millions of documents -- Source: RAG Course Coursera (Deepmind.ai) with Weviate -> Module 2 or Module 3

