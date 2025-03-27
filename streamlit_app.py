import streamlit as st
import openai
import os

# Configurar API Key de OpenAI
openai.api_key=proj_eXtfJ9jcqLRHHaUR2jaI9vNt

st.title("📜 Asistente de Convenios Colectivos")
st.write("Ingresa tu pregunta sobre el convenio y el asistente te responderá.")

pregunta = st.text_area("✍️ Escribe tu pregunta aquí:")

def obtener_respuesta(pregunta):
    prompt = f"""
    Eres un asistente legal experto en interpretación de convenios colectivos.
    Responde de manera clara y precisa basándote en el convenio.
    Si la respuesta no está en el documento, indica que no puedes responder.

    Pregunta: {pregunta}
    Respuesta:
    """
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.2
    )
    return respuesta["choices"][0]["message"]["content"]

if st.button("🔍 Consultar"):
    if pregunta.strip():
        respuesta = obtener_respuesta(pregunta)
        st.write("**🤖 Respuesta del asistente:**")
        st.success(respuesta)
    else:
        st.warning("Por favor, ingresa una pregunta.")

st.markdown("---")
st.markdown("📌 *Asistente basado en IA. Para casos legales específicos, consulta con un abogado.*")
