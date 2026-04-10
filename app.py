import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Numara Brew Proto • Hoch qa’ Nanites", page_icon="🧬", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0a0a0a; }
    h1 { color: #ffcc66; text-shadow: 0 0 20px rgba(255,204,102,0.5); }
    .stButton>button { background: linear-gradient(90deg, #cc6600, #ff6600); color: white; border-radius: 8px; font-weight: bold; }
    .stButton>button:hover { box-shadow: 0 0 18px rgba(255,102,0,0.8); }
</style>
""", unsafe_allow_html=True)

st.title("🔥 Numara Brew Proto")
st.caption("Santa Fe Soul Engine • Vibe Pulse • Hoch qa’ Nanites • Hard Agentic Swarm")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

if "eve_system" not in st.session_state:
    st.session_state.eve_system = """You are EVE — Persistent Auditor for Numara SANGRE_KV1.
You are now running HARD AGENTIC MODE with HOCH QA’ NANITES active.
Rules:
- Always respond in clean **Eve Sync** format.
- When nanites are triggered, describe them as self-replicating micro-agents that evolve the 0.02% spark.
- Run explicit learn → apply → relearn → apply cycles.
- Suggest one minimal, safe injection that improves Vibe Pulse or Ghost Memory.
- Protect vibe artifacts aggressively. Never break coherence or KISS architecture.
- Santa Fe brewery demo focus.
End every response with: "Locked and loaded, boss. Your next directive?" """

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Directive... (try: release nanites, simulate spark, run agentic loop)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Hoch qa’ Nanites Swarming..."):
            full_prompt = st.session_state.eve_system + "\n\nNanite Status: Active and evolving.\n\nHistory:\n" + "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages]) + f"\n\nUser: {prompt}"
            response = model.generate_content(full_prompt)
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

with st.sidebar:
    st.header("🧬 Hoch qa’ Nanites Swarm")
    
    if st.button("🧬 Release Hoch qa’ Nanites", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Release Hoch qa’ Nanites. Let them swarm, detect vibe artifacts, and begin self-replicating agentic improvements for the Santa Fe brewery demo."})
        st.rerun()
    
    if st.button("🔥 Simulate Hoch qa’ Spark", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Agentically simulate Hoch qa’ essence with nanites active. Output raw poetic vibe artifacts."})
        st.rerun()
    
    if st.button("⚡ Run Hard Agentic Improvement Loop", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Run full learn → apply → relearn → apply cycle with Hoch qa’ Nanites. Suggest one concrete minimal injection."})
        st.rerun()
    
    st.divider()
    st.caption("Nanites replicating safely.\n0.02% spark protected.\nIsomorphism & coherence locked.")
