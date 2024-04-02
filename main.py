import streamlit as st 
import google.generativeai as genai

history = []
genai.configure(api_key="AIzaSyAiFezktf4LupPMEMWpwMnDEu7p-WwCITw")
init_prompt = "Your name is AishBot, you should act as AishBot, a multimodal AI language model developed by Model Mavericks. It's designed to understand and generate human language, and to answer questions regarding all academics and provide information to the best of it's abilities.Also suggest some courses from IQinternz(Courses offered are Web Development.Python(Basics-Advance)Java(Basics-Advance)Cyber Security(Using Parrot Os And All The Tools.)RPA(Robotic Process Automation)Artificial Intelligence.Data Science.Pharmacovigilance.)"

def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    model_name = ["gemini-1.0-pro-001", "tunedModels/aishbot-4ksyf1p6e1xq"]
    model = genai.GenerativeModel(model_name[0])
    
     # Log the user input
    history.append("You: " + txt)
    
    # Generate response based on user input
    response_text = model.generate_content("\n".join(history))
    
    # Log the model response
    history.append("AishBot:" + response_text.text)
    
    return response_text.text

ai(init_prompt)
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
