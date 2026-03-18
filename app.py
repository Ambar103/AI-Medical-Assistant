import streamlit as st
from vector_db import VectorDB
from endee_db import EndeeVectorDB
from chatbot import generate_answer

with open("data/medical_data.txt", "r") as f:
    texts = [line.strip() for line in f.readlines() if line.strip()]

faiss_db = VectorDB(texts)

try:
    endee_db = EndeeVectorDB()
    endee_available = True

    try:
        endee_db.add_data(texts)
    except:
        pass

except Exception as e:
    print("Endee not available:", e)
    endee_available = False

try:
    endee_db.data_loaded = False
    endee_db.add_data(texts)
except Exception as e:
    print("Endee add_data error:", e)

st.set_page_config(page_title="Medical AI Assistant", layout="centered")

st.title(" AI Medical Assistant")
st.markdown(" Not medical advice")

query = st.text_input("Ask your question:")

if query:
    with st.spinner("Processing..."):

        if endee_available:
            st.info(" Using Endee Vector Database...")
            try:
                results = endee_db.search(query)
                st.success(" Retrieved using Endee Vector DB")
            except:
                st.warning(" Endee failed → using FAISS")
                results = faiss_db.search(query)
        else:
            st.warning(" Endee offline → using FAISS")
            results = faiss_db.search(query)

        
        if not results:
            st.error("No relevant data found.")
        else:
            context = "\n".join(results)
            answer = generate_answer(context, query)

            st.success("Answer ready")

            st.subheader(" Answer")
            st.write(answer)

            st.subheader(" Context")
            for r in results:
                st.write("- " + r)
