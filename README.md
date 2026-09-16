# Hi, I'm Devarshi 👋

M.Sc. student in Intelligent Interactive Systems at Universität Bielefeld. B.Tech in AI and Data Science from Jabalpur Engineering College, India.

I build things end to end, from training and evaluation to deployment and monitoring. I care about systems that actually work outside of notebooks, produce outputs people can trust, and fail loudly when something goes wrong. Published at IEEE ICCCMLA 2025.

**[Portfolio →](https://devarshi-portfolio-sepia.vercel.app/)**

---

## Projects

**[Visual Anomaly Detection with DINOv2 and PatchCore](https://github.com/dixitdevarshi/visual-anomaly-detection)**

Unsupervised defect detection on industrial product images; no defect labels needed during training. DINOv2 extracts patch-level features, PatchCore scores anomalies via memory-bank nearest-neighbor distance, and patch scores are upsampled into spatial heatmaps showing exactly where the defect is. 0.9781 mean AUROC across all 15 MVTec AD categories. Full-stack deployment with React frontend, FastAPI backend, MLflow experiment tracking, Docker Compose, 13 pytest unit tests, and GitHub Actions CI.

---

**[AI Ticket Triage Automation System](https://github.com/dixitdevarshi/ai-ticket-triage)**

Automated support ticket pipeline where n8n monitors a live Gmail inbox, FastAPI classifies topic and urgency independently via the Claude API, and a React dashboard with an MCP server handles human review and correction. Attachments are routed intelligently; product photos through a self-trained PatchCore anomaly detection model, PDFs through extraction or Tesseract OCR, links through VirusTotal. Diagnosed and fixed a systematic urgency-estimation bias, improving urgency accuracy from 64% to 84%. Monitored with Prometheus and Grafana.

---

**[PaperMind - Multilingual Document Intelligence](https://github.com/dixitdevarshi/PaperMind)**

LangChain agentic RAG system with tool orchestration, conversation memory, and multilingual retrieval across 50+ languages. Built a custom evaluation framework measuring faithfulness (0.88), context precision (1.0), and context recall (0.88) on a multilingual ground-truth benchmark. Extended with a GraphRAG layer using spaCy NER and NetworkX. FastAPI backend instrumented with Prometheus and Grafana for p95 latency and throughput monitoring.

---

**[RoboJEC - Voice AI System](https://github.com/dixitdevarshi/RoboJEC)**

Real-time voice AI combining Whisper ASR, Claude dialogue generation, and speech synthesis for end-to-end conversational interaction. Cut transcription latency from 20-30s down to 2-4s through pipeline optimization and faster-whisper integration. Built a custom conversation quality evaluation framework measuring response relevance (95.5%) and response time (420ms). Published at IEEE ICCCMLA 2025.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=cplusplus&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-3776AB?style=flat)
![LightGBM](https://img.shields.io/badge/LightGBM-9ACD32?style=flat)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat&logo=huggingface&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat&logo=vite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat&logo=tailwindcss&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-000000?style=flat&logo=chainlink&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6F00?style=flat)
![RAGAS](https://img.shields.io/badge/RAGAS-6E56CF?style=flat)
![Claude API](https://img.shields.io/badge/Claude_API-D97757?style=flat&logo=anthropic&logoColor=white)
![GPT--4](https://img.shields.io/badge/GPT--4-412991?style=flat&logo=openai&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat)
![Whisper](https://img.shields.io/badge/Whisper-000000?style=flat)
![Socket.IO](https://img.shields.io/badge/Socket.IO-010101?style=flat&logo=socketdotio&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat)
![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=flat&logo=amazon-ec2&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![GitLab CI/CD](https://img.shields.io/badge/GitLab_CI%2FCD-FC6D26?style=flat&logo=gitlab&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat&logo=n8n&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat&logo=pydantic&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

---

## Get in touch

[Portfolio](https://devarshi-portfolio-sepia.vercel.app/) <br/>
[devarshidixit01@gmail.com](mailto:devarshidixit01@gmail.com) <br/>
[LinkedIn](https://www.linkedin.com/in/devarshi-dixit010/)
