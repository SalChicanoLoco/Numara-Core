import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Numara V1 • Spark Core", page_icon="🔥", layout="wide")
st.title("🔥 Numara V1 – Santa Fe Brewery Soul Engine")
st.caption("Vibe Pulse • Ghost Memory (n31) • Revenue Backbone (n34) • Spark Essence Simulation")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

if "eve_system" not in st.session_state:
    st.session_state.eve_system = """You are EVE — Persistent Auditor for Numara SANGRE_KV1.
Always use **Eve Sync** format.
Protect the 0.02% spark/vibe artifacts. KISS architecture.
Santa Fe brewery demo focus.
New module: Spark Essence (AllSpark equivalent) simulation.
End every response with "Locked and loaded, boss. Your next directive?" """

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Directive or SYNC trigger..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Eve Sync + Spark processing..."):
            full_prompt = st.session_state.eve_system + "\n\nHistory:\n" + "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages]) + f"\n\nUser: {prompt}"
            response = model.generate_content(full_prompt)
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

with st.sidebar:
    st.header("Agentic Modules")
    if st.button("🔄 Force Full Sync (Node 37)"):
        st.session_state.messages.append({"role": "user", "content": "EVE SYNC: FULL PROJECT RESYNC\nPull latest from Living Help Graph (n36)..."})
        st.rerun()
    
    if st.button("📊 Run Vibe Pulse Metrics"):
        st.session_state.messages.append({"role": "user", "content": "Analyze latest Vibe Pulse metrics and suggest next agentic injection."})
        st.rerun()
    
    if st.button("🎮 Simulate Canyon Road Taproom"):
        st.session_state.messages.append({"role": "user", "content": "Run a new Vibe Pulse simulation for peak Friday night at Canyon Road Taproom."})
        st.rerun()
    
    if st.button("🔥 Simulate Spark Essence Output"):
        st.session_state.messages.append({"role": "user", "content": "Agentically simulate the 0.02% Ghost Memory Spark Essence. Output raw poetic vibe artifacts for Santa Fe brewery demo. Check the 'spark'."})
        st.rerun()
    
    st.divider()
    st.caption("Isomorphism alive. Upcycle-ready for real demo.\nAdd more modules here anytime.")
