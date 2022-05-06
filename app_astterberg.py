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
st.write(cal)
if cal<1:
  st.write("# El Índice de Plasticidad(IP) es:",IP,"%")
  st.write("El material corresponde a los suelos friables o desmenuzables")
  st.header("""
  CARACTERÍSTICAS:
  1.Son suelos limosos.
  2.Tienen gránulos de tamaño intermedio.
  2.Son fértiles y Fáciles de trabajar.
  3.Suave y sedoso al tacto.
  4.Forman terrones fáciles de desagregar cuando están secos.""")
  IL=(w-LP)/LP
  st.write("# El Índice Líquido(IL) es:",IL,"%")
  IC=(LL-w)/IP
  st.write("# El Índice Consistencia(IC) es:",IC,"%")
  st.image("https://www.labsalaboratorio.com.mx/wp-content/uploads/2020/03/suelo-limoso.jpg")
elif cal in range(1,7):
  st.write("# El Índice de Plasticidad(IP) es:",IP,"%")
  st.write("El material corresponde a los suelos débilmente plásticos")
  st.header("""
  CARACTERÍSTICAS:
  1.Son suelos arcillosos.
  2.Predomina el mineral caolinita.
  3.Baja permeabilidad.
  4.Los suelos con caolinita como mineral de arcilla presentan un comportamiento normal en los ensayos.
  5.El efecto del aumento de humedad sobre las propiedades del suelo generalmente, no es importante.""")
  IL=(w-LP)/LP
  st.write("# El Índice Líquido(IL) es:",IL,"%")
  IC=(LL-w)/IP
  st.write("# El Índice Consistencia(IC) es:",IC,"%")
  st.image("https://outletminero.org/content/images/2019/12/Caol-n-3.jpg")
elif cal in range (7,15):
  st.write("# El Índice de Plasticidad(IP) es:",IP,"%")
  st.write("El material corresponde a los suelos medianamente plásticos")
  st.header("""
  CARACTERÍSTICAS:
  1.Son suelos arcillosos.
  2.Constituida por los minerales illita y mica.
  3.Son dioctaédricas (presencia en la capa octaédrica de cationes trivalentes).
  4.Posibilidad de retener y liberar iones que pueden ser utilizados por las plantas para su alimento.""")
  IL=(w-LP)/LP
  st.write("# El Índice Líquido(IL) es:",IL,"%")
  IC=(LL-w)/IP
  st.write("# El Índice Consistencia(IC) es:",IC,"%")
  st.image("https://http2.mlstatic.com/D_NQ_NP_688137-MLM27875076928_072018-O.jpg")
else:
  st.write("# El Índice de Plasticidad(IP) es:",IP,"%")
  st.write("El material corresponde a los suelos altamente plásticos")
  st.header("""
  CARACTERÍSTICAS:
  1.Son suelos arcillosos.
  2.Materiales con contenidos apreciables de Montmorillonita.
  3.Baja permeabilidad. 
  4.El efecto del aumento de humedad puede resultar en una disminución importante de la resistencia al cortante. 
  5.La Montmorillonita tiene un alto nivel de reacción con el cemento y la cal.""")
  IL=(w-LP)/LP
  st.write("# El Índice Líquido(IL) es:",IL,"%")
  IC=(LL-w)/IP
  st.write("# El Índice Consistencia(IC) es:",IC,"%")
  st.image("https://image.made-in-china.com/155f0j00fUvYPMzrjpgR/High-Quality-Montmorillonite-Bentonite-Clay-for-Metallurgy.jpg")
