import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="Industrial Knowledge AI Copilot")

st.title("🏭 Industrial Knowledge AI Copilot")

uploaded_file = st.file_uploader("Upload Industrial PDF", type="pdf")

if uploaded_file:

    pdf_reader = PdfReader(uploaded_file)

    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    st.success("PDF Loaded Successfully!")

    question = st.text_input("Ask a question about the PDF")

    if question:

        q = question.lower()

        if "safety goal" in q:
            start = text.find("SAFETY & HEALTH GOALS")
            end = text.find("NEW EMPLOYEE ORIENTATION")
            answer = text[start:end]

        elif "employee respons" in q:
            start = text.find("EMPLOYEE RESPONSIBILITIES")
            end = text.find("ACCIDENT INVESTIGATION/REPORTING")
            answer = text[start:end]

        elif "ppe" in q or "personal protective equipment" in q:
            start = text.find("PERSONAL PROTECTIVE EQUIPMENT")
            end = text.find("SAFETY RULES")
            answer = text[start:end]

        elif "emergency" in q:
            start = text.find("EMERGENCY ACTION PLAN")
            end = text.find("SAFETY DISCIPLINE")
            answer = text[start:end]

        elif "discipline" in q:
            start = text.find("SAFETY DISCIPLINE")
            answer = text[start:]

        else:
            answer = "Question not recognized. Try asking about Safety Goals, PPE, Employee Responsibilities, Emergency Action Plan, or Safety Discipline."

        st.subheader("Answer")
        st.write(answer)

# cd /Users/lokesh/Desktop/hackathon
# streamlit run app.py