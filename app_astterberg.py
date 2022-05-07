import streamlit as st
st.title("Software para el estudio del índice de composición del suelo fino")
st.header("""
INTRODUCCIÓN:
La presencia del agua en los vacíos de un suelo afecta el comportamiento de los suelos finos, por lo cual es importante conocer su cantidad. Si conocemos el contenido de agua del suelo relativo a los límites de Atterberg tendremos una idea acerca de su comportamiento en el área de ingeniería.""")
st.image("https://concepto.de/wp-content/uploads/2021/11/tipos-de-suelos-e1637359333414.jpg")
LL=st.number_input("Escribe el Límite Líquido (%)")
st.write(LL)
LP=st.number_input("Escribe el Límite Plástico (%)")
st.write(LP)
w=st.number_input("Escribe la Humedad Natural del suelo (%)")
st.write(w)
IP=LL-LP
#IP=round(IP,3)
IP=st.button ("Calcular")
#st.write(cal).
if (IP<1):
  st.write("# El Índice de Plasticidad (IP) es:",IP,"%")
  st.write("El material corresponde a los suelos friables o desmenuzables")
  st.header("""
  CARACTERÍSTICAS:""")
  st.write("1.Son suelos limosos.")
  st.write("2.Tienen gránulos de tamaño intermedio.")
  st.write("3.Son fértiles y Fáciles de trabajar.")
  st.write("4.Suave y sedoso al tacto.")
  st.write("5.Forman terrones fáciles de desagregar cuando están secos.")
  IL=(w-LP)/LP
  st.write("# El Índice Líquido (IL) es:",IL,"%")
  IC=(LL-w)/IP
  st.write("# El Índice Consistencia (IC) es:",IC,"%")
  st.image("https://www.labsalaboratorio.com.mx/wp-content/uploads/2020/03/suelo-limoso.jpg")
else:
  if (IP>=1) and (IP<7):
    st.write("# El Índice de Plasticidad (IP) es:",IP,"%")
    st.write("El material corresponde a los suelos débilmente plásticos")
    st.header("""
    CARACTERÍSTICAS:""")
    st.write("1.Son suelos arcillosos.")
    st.write("2.Predomina el mineral caolinita.")
    st.write("3.Baja permeabilidad.")
    st.write("4.Los suelos con caolinita como mineral de arcilla presentan un comportamiento normal en los ensayos.")
    st.write("5.El efecto del aumento de humedad sobre las propiedades del suelo generalmente, no es importante.")
    IL=(w-LP)/LP
    st.write("# El Índice Líquido (IL) es:",IL,"%")
    IC=(LL-w)/IP
    st.write("# El Índice Consistencia (IC) es:",IC,"%")
    st.image("https://outletminero.org/content/images/2019/12/Caol-n-3.jpg")
  else:
    if (cal>=7) and (cal<15):
      st.write("# El Índice de Plasticidad (IP) es:",IP,"%")
      st.write("El material corresponde a los suelos medianamente plásticos")
      st.header("""
      CARACTERÍSTICAS:""")
      st.write("1.Son suelos arcillosos.")
      st.write("2.Constituida por los minerales illita y mica.")
      st.write("3.Son dioctaédricas (presencia en la capa octaédrica de cationes trivalentes).")
      st.write("4.Posibilidad de retener y liberar iones que pueden ser utilizados por las plantas para su alimento.")
      IL=(w-LP)/LP
      st.write("# El Índice Líquido (IL) es:",IL,"%")
      IC=(LL-w)/IP
      st.write("# El Índice Consistencia (IC) es:",IC,"%")
      st.image("https://http2.mlstatic.com/D_NQ_NP_688137-MLM27875076928_072018-O.jpg")
    else:
      st.write("# El Índice de Plasticidad (IP) es:",IP,"%")
      st.write("El material corresponde a los suelos altamente plásticos")
      st.header("""
      CARACTERÍSTICAS:""")
      st.write("1.Son suelos arcillosos.")
      st.write("2.Materiales con contenidos apreciables de Montmorillonita.")
      st.write("3.Baja permeabilidad.")
      st.write("4.El efecto del aumento de humedad puede resultar en una disminución importante de la resistencia al cortante.")
      st.write("5.La Montmorillonita tiene un alto nivel de reacción con el cemento y la cal.")
      IL=(w-LP)/LP
      st.write("# El Índice Líquido (IL) es:",IL,"%")
      IC=(LL-w)/IP
      st.write("# El Índice Consistencia (IC) es:",IC,"%")
      st.image("https://image.made-in-china.com/155f0j00fUvYPMzrjpgR/High-Quality-Montmorillonite-Bentonite-Clay-for-Metallurgy.jpg")
