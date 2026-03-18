import streamlit as st
from vector_db import VectorDB
from endee_db import EndeeVectorDB
from chatbot import generate_answer

# Load dataset
with open("data/medical_data.txt", "r") as f:
    texts = [line.strip() for line in f.readlines() if line.strip()]

# Initialize DBs
faiss_db = VectorDB(texts)
endee_db = EndeeVectorDB()

# Add data to Endee (only once ideally)
try:
    endee_db.data_loaded = False
    endee_db.add_data(texts)
except Exception as e:
    print("Endee add_data error:", e)

# UI
st.set_page_config(page_title="Medical AI Assistant", layout="centered")

st.title(" AI Medical Assistant")
st.markdown(" Not medical advice")

query = st.text_input("Ask your question:")

if query:
    with st.spinner("Processing..."):

        st.info("🔗 Using Endee Vector Database...")

        try:
            results = endee_db.search(query)
            st.success(" Retrieved using Endee Vector DB")

        except Exception as e:
            st.warning(" Endee failed → using FAISS")
            print(e)
            results = faiss_db.search(query)

        context = "\n".join(results)
        answer = generate_answer(context, query)

    st.success("Answer ready")

    st.subheader(" Answer")
    st.write(answer)

    st.subheader(" Context")
    for r in results:
        st.write("- " + r)