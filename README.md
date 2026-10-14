## Hi, I'm Alif Tasbir 👋

**AI/ML Engineer · Deep Learning · LLMs & Agents · Healthcare AI**, based in Leicester, UK

I'm an MSc Artificial Intelligence candidate at De Montfort University. I build machine learning systems end to end, from deep learning research to deployed applications. My work covers biomedical signal models for EEG and ECG using CNNs, LSTMs and GNNs, as well as LLM fine-tuning, RAG, multi-agent systems and efficient edge inference. I've published three peer-reviewed papers in clinical AI, and I'm open to AI/ML Engineer roles.

🌐 **Portfolio:** [a1if.github.io](https://a1if.github.io)  
💼 **LinkedIn:** [alif-tasbir](https://www.linkedin.com/in/alif-tasbir-16365141b/)  
📫 **Email:** [aliftasbir@gmail.com](mailto:aliftasbir@gmail.com)  
📄 **CV:** [Download PDF](https://a1if.github.io/Alif_Tasbir_CV.pdf)

---

### 🔬 Featured: ECG Multi-Agent Triage

A two-agent ECG triage system. A CNN-LSTM perception agent classifies heartbeats and hands events to a frozen Gemma reasoning agent, either as text or as learned virtual tokens. It includes guardrails, an orchestrator and clinician Q&A. This is my MSc dissertation.

- **24–78%** faster LLM prompt processing, with balanced accuracy of **0.83 vs 0.73**
- **10–30%** higher throughput and **12–28%** less energy per decision on a 12 GB GPU

**[▶ Live demo](https://ecg-multi-agent-triage.streamlit.app/)** · [App code](https://github.com/a1if/ecg-multi-agent-triage) · [Research code](https://github.com/a1if/Heterogeneous-Multi-Agent-Edge-AI-for-Clinical-Decision-Support)

### 🛠 Other projects

| Project | What it does | Stack |
|---|---|---|
| [Fine-Tuned Small LLM for Multi-Hop RAG](https://github.com/a1if/qlora-multihop-rag) | LoRA fine-tuned Qwen3-1.7B that matches a 4.7× larger Qwen3-8B on HotpotQA (exact match 10.4 → 58.4) at ~8× the throughput; hybrid retrieval with reranking, an MCP server and a tool-use fine-tuned agent | PyTorch, PEFT, LangGraph, MCP, FAISS |
| [Multimodal RAG System](https://github.com/a1if/-RAG-System) | Bilingual (Bangla and English) RAG with web search, a deep-reasoning mode, and routing between Gemini and gpt-oss | FastAPI, Streamlit, FAISS |
| [AI Interior Visualizer](https://github.com/a1if/Nano-Banana-Hackathon) | Interior design visualizer built for the Nano Banana hackathon | TypeScript, Gemini 2.5 Flash Image |

### 📄 Publications

- [Parkinson's disease detection from EEG signal employing autoencoder and RBFNN-based hybrid deep learning framework utilizing power spectral density](https://doi.org/10.1177/20552076241297355), *Digital Health* (2024)
- [Graph attention network and radial basis function neural network-based hybrid framework for epileptic seizure detection from EEG signal](https://doi.org/10.32629/jai.v7i3.1149), *Journal of Autonomous Intelligence* (2023)
- [Epileptic seizure detection from EEG signals using linear graph convolutional network and DenseNet based hybrid framework](https://doi.org/10.1016/j.jrras.2023.100607), *Journal of Radiation Research and Applied Sciences* (2023)

### 🧰 Tech stack

**LLMs and RAG:** Hugging Face Transformers · LoRA / QLoRA / PEFT / TRL · LangChain · LangGraph · MCP · Ollama · FAISS · ChromaDB · Sentence Transformers · Gemini API  
**ML and DL:** PyTorch · TensorFlow · Keras · scikit-learn · Pandas · NumPy  
**APIs and apps:** FastAPI · Flask · Django · Streamlit · Gradio  
**MLOps:** Git · GitHub Actions · Docker · MLflow · DVC · OpenTelemetry  
**Languages:** Python · C · C++ · Java · JavaScript · SQL

<p>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="36" alt="Python"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg" width="36" alt="PyTorch"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" width="36" alt="TensorFlow"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg" width="36" alt="scikit-learn"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="36" alt="FastAPI"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="36" alt="Docker"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" width="36" alt="Streamlit"/>
</p>

### 🎓 Education

- **MSc Artificial Intelligence**, De Montfort University, Leicester (2025–2026)
- **BSc Computer Science and Engineering**, UITS, Dhaka (2018–2022), CGPA 3.74/4.00
