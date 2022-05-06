import streamlit as st
st.title("Software para el estudio de la composición del suelo fino")
st.header("""
INTRODUCCIÓN:""")
st.image("https://concepto.de/wp-content/uploads/2021/11/tipos-de-suelos-e1637359333414.jpg")
LL=st.number_input("Escribe el Límite Líquido (%)")
st.write(LL)
LP=st.number_input("Escribe el Límite Plástico (%)")
st.write(LP)
w=st.number_input("Escribe la Humedad Natural del suelo (%)")
st.write(w)
IP=LL-LP
IP=round(IP,3)
cal=st.button ("Calcular")
sr.write(cal)
if cal==True:
elif cal<1:
  st.write("# El Índice de Plasticidad(IP) es:",IP,"%")
  st.write("El material corresponde a los suelos friables o desmenuzables")
  IL=(w-LP)/LP
  st.write("# El Índice Líquido(IL) es:",IL,"%")
  IC=(LL-w)/IP
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
