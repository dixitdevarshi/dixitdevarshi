# Hi there, I'm Devarshi 👋

Master's student in Intelligent Interactive Systems at Universität Bielefeld, with a B.Tech in AI and Data Science from Jabalpur Engineering College, India.

Over the past year I've built and shipped systems across computer vision, LLM engineering, speech AI, and ML pipelines. I care about making things that actually work end to end, not just in a notebook. Published at IEEE ICCCMLA 2025.

## A bit about me

- Currently doing my M.Sc. at Universität Bielefeld, focused on AI systems, NLP, and human-computer interaction
- Interned at DRDO's AI lab working on speech recognition with Wav2Vec 2.0
- Published research on conversational AI at IEEE ICCCMLA 2025

## Projects

**AI Ticket Triage System - n8n + FastAPI + Claude + PostgreSQL**
Automated support ticket pipeline: a real Gmail inbox is monitored via n8n, tickets are classified by topic and urgency independently, and attachments are routed intelligently, product photos through a self-trained anomaly detection model, screenshots through Claude's vision, PDFs extracted directly or OCR'd if scanned. Includes a confidence-based human review and correction loop, monitored with Prometheus and Grafana. 94% category accuracy and 84% urgency accuracy on a 50-ticket evaluation set, with a documented and fixed urgency-estimation bias.

**Visual Anomaly Detection - DINOv2 + PatchCore**
Unsupervised defect detection on industrial product images. No defect labels needed during training. 0.9781 mean AUROC across all 15 MVTec AD categories. Spatial localization with patch-level heatmaps.

**PaperMind - Multilingual Document Intelligence**
LangChain agentic RAG system with tool orchestration, conversation memory, and retrieval across 50+ languages. Built a custom evaluation framework measuring faithfulness (0.88) and context precision (1.0).

**RoboJEC - Voice AI System (IEEE ICCCMLA 2025)**
Real-time voice AI combining Whisper ASR, Claude dialogue generation, and speech synthesis. Cut transcription latency from 20-30s to 2-4s. 95.5% response relevance, 420ms response time.

**Deutsche Bahn Delay Risk Estimator**
LightGBM on 2M+ transport records. Deployed as Flask REST API on AWS EC2 with Docker and GitHub Actions CI/CD. ROC-AUC 0.7655.

## Tech Stack

Python, PyTorch, DINOv2, LangChain, ChromaDB, Claude API, Whisper, Wav2Vec 2.0, LightGBM, XGBoost, SHAP, FastAPI, Flask, PostgreSQL, SQLAlchemy, n8n, Docker, Prometheus, Grafana, AWS EC2, GitHub Actions, Streamlit, scikit-learn, HuggingFace Transformers

## Get in touch

devarshidixit01@gmail.com <br/>
[LinkedIn](https://www.linkedin.com/in/devarshi-dixit010/)
