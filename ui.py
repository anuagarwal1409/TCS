import streamlit as st
import os
import subprocess 
import time
import random
import plotly.express as px
import pandas as pd

def radar_chart():  
    df = pd.DataFrame(dict(
    r=[random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22)],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    placeholder.write(fig)


placeholder = st.empty()
start_button = st.empty()

st.title('Video Summarizer App')
input_url = st.text_input("Youtube Video Link")
os.system("python sum.py -u "+input_url)


latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
# Update the progress bar with each iteration.
    latest_iteration.text(f'## Finishing..{i+1}')
    bar.progress(i + 1)
    time.sleep(1)


video_file = open('1_1.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)