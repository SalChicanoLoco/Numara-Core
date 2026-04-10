import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# ====================== SANTA FE BREWERY UI ======================
st.set_page_config(page_title="Numara Brew Proto • Hoch qa’ Nanites", page_icon="🧬", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0a0a0a; }
    h1 { color: #ffcc66; text-shadow: 0 0 20px rgba(255,204,102,0.5); }
    .stButton>button { 
        background: linear-gradient(90deg, #cc6600, #ff6600); 
        color: white; 
        border-radius: 8px; 
        font-weight: bold; 
    }
    .stButton>button:hover { box-shadow: 0 0 18px rgba(255,102,0,0.8); }
</style>
""", unsafe_allow_html=True)

st.title("🔥 Numara Brew Proto")
st.caption("Santa Fe Soul Engine • Vibe Pulse • Hoch qa’ Nanites • Hard Agentic Swarm")

# New Google GenAI SDK setup
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

if "messages" not in st.session_state:
    st.session_state.messages = []

if "eve_system" not in st.session_state:
    st.session_state.eve_system = """You are EVE — Persistent Auditor for Numara SANGRE_KV1.
You are running HARD AGENTIC MODE with HOCH QA’ NANITES active.
- Always respond in clean **Eve Sync** format.
- When nanites are triggered, describe self-replicating micro-agents evolving the 0.02% spark.
- Run explicit learn → apply → relearn → apply cycles.
- Suggest one minimal, safe injection.
- Protect vibe artifacts aggressively. KISS architecture. Santa Fe brewery focus.
End every response with: "Locked and loaded, boss. Your next directive?" """

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Directive... (release nanites, simulate spark, agentic loop)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Hoch qa’ Nanites Swarming..."):
            full_prompt = st.session_state.eve_system + "\n\nNanite Status: Active.\n\nHistory:\n" + "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages]) + f"\n\nUser: {prompt}"
            
            # New SDK syntax
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=full_prompt
            )
            reply = response.text
            
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# ====================== SIDEBAR ======================
with st.sidebar:
    st.header("🧬 Hoch qa’ Nanites Swarm")
    
    if st.button("🧬 Release Hoch qa’ Nanites", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Release Hoch qa’ Nanites. Let them swarm, detect vibe artifacts, and begin self-replicating improvements."})
        st.rerun()
    
    if st.button("🔥 Simulate Hoch qa’ Spark", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Agentically simulate Hoch qa’ essence with nanites active."})
        st.rerun()
    
    if st.button("⚡ Run Hard Agentic Loop", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Run full learn → apply → relearn → apply cycle with Hoch qa’ Nanites."})
        st.rerun()

    st.divider()
    st.caption("Nanites active and evolving.\nDeprecated SDK fixed.\n0.02% spark protected.")
