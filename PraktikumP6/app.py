import streamlit as st

st.title("Audio Playback Demo - Modul Praktikum")

st.subheader("🎧 Fade In")
st.audio("podcast_intro_fadein.wav")

st.subheader("🎧 Fade Out")
st.audio("podcast_outro_fadeout.wav")

st.subheader("⏩ Tempo + Fade")
st.audio("tempo_fadeinout.wav")

st.write("Antarmuka ini menyajikan tiga jenis hasil manipulasi audio: fade in, fade out, dan kombinasi tempo + fade. Pengguna dapat memutar dan membandingkan hasil efek audio langsung melalui Streamlit.")
