# 🩺 AI Medical Assistant (RAG + Endee)

🚀 A Retrieval-Augmented Generation (RAG) based AI Medical Assistant that answers health-related queries using a vector database and LLM.

---

## 🌐 Live Demo

👉 https://ai-medical-assistant101.streamlit.app

---

## 📌 Overview

This project is an AI-powered medical assistant that:

* Retrieves relevant medical information using a vector database
* Generates structured answers using a language model
* Ensures responses are grounded in actual data (no hallucination)

---

## ⚙️ Tech Stack

* **Frontend**: Streamlit
* **Vector Database**: Endee (Local), FAISS (Fallback)
* **Embeddings**: Sentence Transformers (`all-MiniLM-L6-v2`)
* **LLM**: HuggingFace FLAN-T5
* **Backend**: Python

---

## 🧠 How It Works

1. User enters a medical query
2. Query is converted into embeddings
3. Vector database retrieves similar medical records
4. Retrieved context is passed to the LLM
5. LLM generates a structured response

---

## 🔥 Features

* ✅ RAG-based architecture
* ✅ Endee vector database integration
* ✅ FAISS fallback for cloud deployment
* ✅ Structured medical responses
* ✅ Clean Streamlit UI
* ✅ Works even if Endee is offline

---

## ⚠️ Note on Deployment

* Endee runs locally via Docker
* Streamlit Cloud does not support Docker
* Therefore:

  * **Local → Endee is used**
  * **Cloud → FAISS fallback is used**

---

## 📂 Project Structure

```
AI-Medical-Assistant/
│── app.py
│── chatbot.py
│── endee_db.py
│── vector_db.py
│── embeddings.py
│── requirements.txt
│── data/
│   └── medical_data.txt
```

---

## 🚀 How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/Ambar103/AI-Medical-Assistant.git
cd AI-Medical-Assistant
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. (Optional) Run Endee via Docker

```
docker run --ulimit nofile=100000:100000 -p 8080:8080 endeeio/endee-server:latest
```

### 4. Run the app

```
streamlit run app.py
```

---

## 🧪 Example Query

```
high fever
```

### Output:

* Possible causes: infections, flu, dengue
* Symptoms: high temperature, chills, sweating
* Related conditions: malaria, typhoid

---

## 🧠 Key Learning

* Implemented a real-world **RAG pipeline**
* Integrated **vector databases (Endee + FAISS)**
* Handled **deployment constraints with fallback architecture**
* Improved response quality using **prompt engineering + structured extraction**

---

## 📌 Future Improvements

* Add chat memory
* Integrate real medical APIs
* Improve dataset quality
* Add multi-language support

---

## ⚠️ Disclaimer

This project is for educational purposes only and should not be used as medical advice.

---

## 👨‍💻 Author

**Ambar S**
🔗 https://github.com/Ambar103
