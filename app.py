import streamlit as st
from reply_engine import extract_text, generate_emotion_reply_llm

st.set_page_config(page_title="Emotion-Aware OCR Reply", layout="centered")

st.title("📷 VISHAKHA APP (OCR + Emotion-based Reply)")

uploaded_file = st.file_uploader("Upload an image with text", type=["png", "jpg", "jpeg"])

tone = st.selectbox(
    "Choose the emotion/tone for your reply:",
    ["Neutral", "Friendly", "Formal", "Sarcastic", "Excited", "Apologetic"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    image_bytes = uploaded_file.read()

    with st.spinner("🔍 Extracting text from image..."):
        extracted_text = extract_text(image_bytes)

    if extracted_text:
        original_text = " ".join(extracted_text)
        st.markdown("### 🧾 Extracted Text")
        st.write(original_text)

        with st.spinner("✍️ Generating emotional reply using OpenAI..."):
            styled_reply = generate_emotion_reply_llm(original_text, tone)

        st.markdown("### 💬 Emotion-Toned Reply")
        st.success(styled_reply)

    else:
        st.warning("⚠️ No readable text found in the image.")
