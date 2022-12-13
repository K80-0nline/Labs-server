# after changing it type in cmd >git add . < then >git commit -m "(what changed)" then git push -u origin master
#to run this, in cmd prompt type cd [file location]. then streamlit run [file name].py

import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Labs", page_icon=":space_invader:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return none
    return r.json()

#-------------header section ----------------

with st.container():
    st.subheader("Welcome to Labs!")
    st.title("A Retro Style, story based Game!")
    st.write("We are currently looking for a team to help us develop a game! ")
    st.write("if u are  looking for a fun place to gain experience of how games are made and learn among the rest of the team, please contact us at, [our discord >](https://discord.gg/ttckuQcG37) ")
    

#---------Load assets----------

lottie_GIF1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_w51pcehl.json")

#-------GENERAL SUMMERY OF THE GAME ----------------

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is Labs?")
        st.write("Labs is a 2D, Retro Style game which has taken insperation from game genres similar to [StarDew Valley](https://www.stardewvalley.net). ")
        st.write("Labs is about a creature who had been kept in containment for his whole life, during this time it had come to like its care taker, jack. unfortunately, this has come to an end... his creator was 'fired' out of the blue after a new species has been discovered and contained, unknown to the organization that funded it all... Follow along as we try to find out what had happend to Jack, learning new things about yourself, finding out what u are capable of and uncovering the truth. ")

    with right_column:
        st_lottie(lottie_GIF1, height=300, key="GUI1")

#-----------Main--------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Dev Team Application!")
        st.write(
            """
            looking to apply for dev team? follow the steps bellow to join!

            * click this link to join the discord [discord server](https://discord.gg/ttckuQcG37)

            * go to #📢ʃsubmit-forms-hereʃ 

            * type %apply

            * fill out the questions the BOT sends to u in DMS

            * and your done!

            * forms may take a couple days to be gone over so please be patient

            """
        )
        
