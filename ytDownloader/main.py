from pytube import YouTube
import streamlit as st

links = st.text_input("paste url youtube")
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
        st.error("An error has occurred")
    print("Download is completed successfully")
    st.info("Download is completed successfully")


if st.button("download"):
    Download(links)