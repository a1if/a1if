## Hi, I'm Alif Tasbir 👋

**AI/ML Engineer · Deep Learning · LLMs & Agents · Healthcare AI**, based in Leicester, UK

I'm a recent MSc Artificial Intelligence graduate from De Montfort University. My work covers deep learning for biomedical signals such as EEG and ECG, using CNNs, LSTMs and graph neural networks. It also covers LLM fine-tuning, retrieval-augmented generation and multi-agent systems, as well as efficient inference on edge hardware. I take models from experiment to product with PyTorch, FastAPI, Docker and MLflow, and I've published three peer-reviewed papers in clinical AI. I'm looking for an AI/ML Engineer role building machine learning solutions for real-world problems.

🌐 **Portfolio:** [a1if.github.io](https://a1if.github.io)  
📄 **CV:** [Download PDF](https://a1if.github.io/Alif_Tasbir_CV.pdf)  
📫 **Email:** [aliftasbir@gmail.com](mailto:aliftasbir@gmail.com)  
💼 **LinkedIn:** [linkedin.com/in/alif-tasbir-16365141b](https://www.linkedin.com/in/alif-tasbir-16365141b/)  
𝕏 **X:** [x.com/tasbir_alif](https://x.com/tasbir_alif)  
🆔 **ORCID:** [0000-0001-6697-8974](https://orcid.org/0000-0001-6697-8974)

---

### 🔬 Featured: ECG Multi-Agent Triage: Heterogeneous Edge AI for Clinical Decision Support

<a href="https://ecg-multi-agent-triage.streamlit.app/"><img src="https://a1if.github.io/images/ecg-triage-demo.webp" alt="Demo of the ECG triage app: analysing a recording, the two agents' conversation, adapter vs text charts, and clinician Q&A" width="100%"></a>

A two-agent ECG triage system. A CNN-LSTM perception agent classifies heartbeats and passes events to a frozen Gemma reasoning agent, either as text or as learned virtual tokens. It includes guardrails, an orchestrator and clinician Q&A. This is a research prototype.

- **24–78%** faster LLM prompt processing than compact text, with balanced accuracy of **0.83 vs 0.73** at 10 and 20 events.
- **10–30%** higher throughput and **12–28%** less energy per decision on a 12 GB GPU, measured with NVML at 100 Hz.

**[▶ Try the live demo](https://ecg-multi-agent-triage.streamlit.app/)** · [App code](https://github.com/a1if/ecg-multi-agent-triage) · [Research code](https://github.com/a1if/Heterogeneous-Multi-Agent-Edge-AI-for-Clinical-Decision-Support)

### 🛠 Other projects

| Project | What it does | Stack |
|---|---|---|
| [Fine-Tuned Small LLM for Multi-Hop RAG](https://github.com/a1if/qlora-multihop-rag) | LoRA fine-tuned Qwen3-1.7B: exact match **10.4 → 58.4** on HotpotQA, matching a **4.7× larger** Qwen3-8B with ~5× smaller weights at ~8× the throughput.<br>Hybrid retrieval (BM25 + FAISS, reranking) with multi-hop search: evidence recall **54% → 89%**, with citations and abstention.<br>MCP server with typed tools and OpenTelemetry tracing; tool-use fine-tuned LangGraph agent (+19.7 F1). | PyTorch, PEFT, LangGraph, MCP, FAISS |
| [Multimodal RAG Application](https://github.com/a1if/multimodal-rag-system) | Bilingual (Bangla & English) RAG over PDFs, scans, Office files and images, with Tesseract OCR, answering in the user's language with page-level citations.<br>Hybrid retrieval: BM25 plus multilingual-e5 embeddings in FAISS, merged with reciprocal rank fusion, in per-session document stores.<br>LLM-routed web search: the model decides when fresh information is needed, rewrites the query and sizes the Tavily search. Streams answers from Gemini or Groq (gpt-oss-20b) via FastAPI + Streamlit. | FastAPI, Streamlit, FAISS |
| [AI Interior Visualizer](https://github.com/a1if/Nano-Banana-Hackathon) | An interior design visualizer built for the Nano Banana hackathon, powered by Gemini 2.5 Flash Image. | TypeScript |

### 📄 Publications

- [Parkinson's disease detection from EEG signal employing autoencoder and RBFNN-based hybrid deep learning framework utilizing power spectral density](https://doi.org/10.1177/20552076241297355), *Digital Health* (2024)
- [Graph attention network and radial basis function neural network-based hybrid framework for epileptic seizure detection from EEG signal](https://doi.org/10.32629/jai.v7i3.1149), *Journal of Autonomous Intelligence* (2023)
- [Epileptic seizure detection from EEG signals using linear graph convolutional network and DenseNet based hybrid framework](https://doi.org/10.1016/j.jrras.2023.100607), *Journal of Radiation Research and Applied Sciences* (2023)

### 🧰 Tech stack

**LLMs & RAG:** LoRA/QLoRA, PEFT, TRL, Hugging Face Transformers, LangChain, LangGraph, Model Context Protocol (MCP), Ollama, FAISS, ChromaDB, hybrid search & reranking, Sentence Transformers, Gemini API, LLM evaluation (EM/F1, faithfulness, BLEU/ROUGE/BERTScore)  
**ML & DL:** PyTorch, TensorFlow, Keras, scikit-learn, Pandas, NumPy, CNNs, LSTMs  
**APIs & apps:** FastAPI, Flask, Django, Streamlit, Gradio  
**MLOps:** Git, GitHub Actions, Docker, MLflow, DVC, OpenTelemetry  
**Languages:** Python, C, C++, Java, JavaScript, SQL, HTML, CSS

<p>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="36" alt="python"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg" width="36" alt="pytorch"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" width="36" alt="tensorflow"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg" width="36" alt="scikitlearn"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="36" alt="fastapi"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="36" alt="docker"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" width="36" alt="streamlit"/>
</p>

### 🎓 Education

- **MSc Artificial Intelligence**, De Montfort University, Leicester, United Kingdom (2025–2026), **Distinction (80%)**
- **BSc Computer Science & Engineering**, University of Information Technology and Sciences (UITS), Dhaka, Bangladesh (2018–2022), **CGPA 3.74/4.00**

<sub>This README is generated from my portfolio's content and updates automatically.</sub>
