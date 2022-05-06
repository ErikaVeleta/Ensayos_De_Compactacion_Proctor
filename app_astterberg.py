import streamlit as st
st.title ("Software para el estudio de la composición del suelo fino")
INTRODUCCIÓN
st.image("https://concepto.de/wp-content/uploads/2021/11/tipos-de-suelos-e1637359333414.jpg")
LL=st.number_input("Escribe el Límite Líquido (%)",0)
st.write(LL)
plastico=st.number_input("Escribe el Límite Plástico (%)",0)
st.write(LP)
w=st.number_input("Escribe la Humedad Natural del suelo (%)",0)
st.write(w)
IP=LL-LP
IP=round(IP,3)
IL=(w-LP)/LP
IL=round(IL,3)
IC=(LL-w)/IP
IC=round(IL,3)
cal=st.button ("Calcular")
sr.write(cal)
if cal<1:
  st.write("# El Índice de Plasticidad(IP) es:",IP,"%")
  st.write("El material corresponde a los suelos friables o desmenuzables")
  st.write("# El Índice Líquido(IL) es:",IL,"%")
  st.write("# El Índice Consistencia(IC) es:",IC,"%")
elif 1<cal<7:
  st.write("# El Índice de Plasticidad(IP) es:",IP,"%")
  st.write("El material corresponde a los suelos débilmente plásticos")
  st.write("# El Índice Líquido(IL) es:",IL,"%")
  st.write("# El Índice Consistencia(IC) es:",IC,"%")
elif 7<cal<15:
  st.write("# El Índice de Plasticidad(IP) es:",IP,"%")
  st.write("El material corresponde a los suelos medianamente plásticos")
  st.write("# El Índice Líquido(IL) es:",IL,"%")
  st.write("# El Índice Consistencia(IC) es:",IC,"%")
else:
  st.write("# El Índice de Plasticidad(IP) es:",IP,"%")
  st.write("El material corresponde a los suelos altamente plásticos")
  st.write("# El Índice Líquido(IL) es:",IL,"%")
  st.write("# El Índice Consistencia(IC) es:",IC,"%")
