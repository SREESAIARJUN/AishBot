import streamlit as st 
import google.generativeai as genai


genai.configure(api_key="AIzaSyAiFezktf4LupPMEMWpwMnDEu7p-WwCITw")
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    model_name = ["gemini-1.0-pro-001", "tunedModels/aishbot-4ksyf1p6e1xq"]
    model = genai.GenerativeModel(model_name[0])
    model.generate_content(f"You are a chatbot named AishBot, a multimodal AI language model developed by Model Mavericks. I am designed to understand and generate human language, and to answer questions regarding all your academics and provide information to the best of my abilities.Also suggest some courses from IQinternz(Courses offered are)")
    response = model.generate_content(txt)
    return response.text

st.title("AishBot")

command = st.chat_input("Enter your Query...")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])

if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":command})
   
    with st.chat_message("BOT"):
        data = ai(command)
        st.write(data)
        st.session_state.message.append({"role":"BOT","message":data})

print(st.session_state.message)
