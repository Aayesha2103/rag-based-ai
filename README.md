# 🎥 RAG-Based AI Video Knowledge Assistant

<p align="center">
  <b>Ask questions about long videos and find the exact place where the answer is explained.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/RAG-AI-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Whisper-large--v2-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Ollama-Local%20AI-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Llama%203.2-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/bge--m3-red?style=for-the-badge" />
</p>

---

## 📌 Overview

**RAG-Based AI Video Knowledge Assistant** is an AI-powered system that converts educational videos into a searchable knowledge base.

Instead of manually searching through long videos, users can ask a natural-language question and the system retrieves the most relevant part of the course and generates an answer using a local LLM.

### 💡 Example

> **"Where is Git branching explained?"**

The system finds the most relevant transcript segments, identifies the video and timestamp, and uses an LLM to generate the final response.

---

## 🚀 How It Works

```text
🎬 Video
   ↓
🎵 FFmpeg → Audio
   ↓
🎙️ Whisper large-v2
   ↓
📝 Timestamped Transcript
   ↓
🧠 bge-m3 Embeddings
   ↓
💾 Knowledge Base
   ↓
❓ User Question
   ↓
🧠 Query Embedding
   ↓
🔎 Cosine Similarity
   ↓
🏆 Top 5 Relevant Chunks
   ↓
📚 RAG Prompt
   ↓
🤖 Llama 3.2
   ↓
💬 Final Answer + Video Timestamp
✨ Key Features
🎬 Video-to-audio processing using FFmpeg
🎙️ Speech-to-text using OpenAI Whisper
🌍 Hindi speech → English translation
⏱️ Timestamp-aware transcript chunks
🧠 Semantic embeddings using bge-m3
🔎 Semantic search using Cosine Similarity
📚 Retrieval-Augmented Generation (RAG)
🤖 Local LLM inference using Llama 3.2
🦙 Local AI models served through Ollama
💾 Embedding persistence using Joblib
🛠️ Tech Stack
Technology	Purpose
🐍 Python	Core development
🎙️ Whisper large-v2	Speech-to-text & translation
🎬 FFmpeg	Audio extraction
🧠 bge-m3	Text embeddings
🤖 Llama 3.2	Answer generation
🦙 Ollama	Local AI model serving
🔎 Scikit-learn	Cosine similarity
📊 Pandas	Data processing
🔢 NumPy	Numerical operations
💾 Joblib	Embedding storage
🌐 Requests	Ollama API communication
📄 JSON	Transcript storage
📂 Project Structure
rag-based-ai/
│
├── videos/              # Original videos
├── audio/               # Extracted MP3 files
├── jsons/               # Timestamped transcripts
│
├── process_video.py     # Video → MP3
├── create_chunks.py     # Whisper transcription
├── speech_to_text.py    # Speech-to-text example
├── read_chunks.py       # Generate embeddings
├── process_incoming.py  # RAG question-answer pipeline
│
├── embeddings.joblib    # Stored embeddings
├── prompt.txt           # Generated RAG prompt
├── response.txt         # Generated response
└── README.md
🧠 RAG Pipeline

This project follows three main RAG stages:

1. 🔎 Retrieval

The user's question is converted into an embedding and compared with transcript embeddings using cosine similarity.

2. 📚 Augmentation

The top 5 relevant transcript chunks are added to the LLM prompt along with video and timestamp information.

3. 🤖 Generation

Llama 3.2 receives the retrieved context and generates the final answer.

⚙️ Installation
Clone the repository
git clone https://github.com/Aayesha2103/rag-based-ai.git
cd rag-based-ai
Install dependencies
pip install openai-whisper pandas numpy scikit-learn joblib requests
Install and prepare Ollama

The project uses:

bge-m3      → Embeddings
llama3.2    → Answer Generation

Make sure Ollama is running locally and the required models are available.

Run the pipeline
python process_video.py
python create_chunks.py
python read_chunks.py
python process_incoming.py
📖 Documentation

📄 Read the Complete Technical Documentation & Viva Guide

The documentation includes:

Complete project architecture
Detailed technology explanation
File-by-file explanation
RAG workflow
5-minute teacher explanation
Complete technical story
Interview & viva questions
Project limitations
Future improvements
🔮 Future Improvements
🌐 Build a web interface
⚡ Add FastAPI backend
🗄️ Use a dedicated vector database
🔍 Add hybrid search and reranking
📊 Add retrieval evaluation metrics
🎥 Add clickable video timestamps
💬 Add conversation history
🐳 Dockerize the application
☁️ Deploy the application
👩‍💻 Author
Aayesha Singh

AI / ML & Data Science Enthusiast

🔗 [GitHub Profile](https://github.com/Aayesha2103)

⭐ Project Repository
🚀 [View RAG-Based AI Project →](https://github.com/Aayesha2103/rag-based-ai)
