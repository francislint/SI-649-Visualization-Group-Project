import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError

st.markdown("### Influencer Distribution")

# st.sidebar.header("Mapping Demo")
st.write(
    """To view the dynamic visualization, please visit [INS and YOTUBE INFLUENCERS DISTRIBUTION](https://public.tableau.com/app/profile/tong.lin/viz/audiencemapsforinsandyoutube/Dashboard1)"""
)

st.image('imgs/map.jpeg')
