import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.slidebar.title ("Software para el estudio del índice de plasticidad del suelo (IP)")
INTRODUCCIÓN

st.image ("https://concepto.de/wp-content/uploads/2021/11/tipos-de-suelos-e1637359333414.jpg")

capsula=st.number_input("Escribe el peso de cápsula (gr)",0)
st.write(capsula)
humedo=st.number_input("Escribe el peso de cápsula + suelo húmedo (gr)",0)
st.write(humedo)
seco=st.number_input("Escribe el peso de cápsula + suelo seco (gr)",0)
st.write(seca)
LL=
