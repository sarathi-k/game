import streamlit as st 
import os 
from PIL import Image 
import random

image_folder="images"
hash_map={"rock":"rock.jpg","paper":"paper.jpg","scissor":"scissor.jpg"}
st.title("Rock Paper Scissor Game 🪨 📄✂️")
choose=list(hash_map.keys())

player1=st.selectbox("player1",choose)
if st.button("play"):

    player1_img=Image.open(os.path.join(image_folder,hash_map[player1]))
    

    comp=random.choice(choose)
    comp1_img=Image.open(os.path.join(image_folder,hash_map[comp]))


    col1,col2=st.columns(2)
    with col1:
        st.image(player1_img,caption="player 1",use_column_width=True)
    with col2:
            st.image(comp1_img,caption="computer",use_column_width=True)
    if player1==comp:
         st.write("Draw")
    elif (player1=="rock" and comp=="scissor") or (player1=="paper" and comp=="rock") or (player1=="scissor" and comp=="paper"):
         st.write("player1 wins")
         st.success("playwer 1 wins")
    else:
         st.write("computer wins")

