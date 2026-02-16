import streamlit as st

st.title(" Ejercicios de practica")
st.divider()

st.title(" Ejercicio 1: Saludo Simple")
st.caption("Crea un campo de entrada de texto para que el usuario escriba su nombre.")

nombre = st.text_input("Digita tu nombre: ")
if nombre:
    st.write(f"¡Hola, {nombre}!")

st.divider()

st.title(" Ejercicio 2: Calculadora de multi")
st.caption("Pide al usuario dos números, multiplícalos y muestra el resultado. Si alguno de los números es mayor a 100, muestra una advertencia.")

num1 = st.number_input("Digita el primer número: ",value=0)
num2 = st.number_input("Digita el segundo número: ",value=0)

if num1 and num2:
    multi = num1 * num2
    st.write(f"El multi de {num1} y {num2} es: {multi}")

    if num1 > 100 or num2 > 100:
        st.warning("Números grandes")

st.divider()

st.title("  Ejercicio 3: Convertidor de Temperatura (Radio Buttons)")
st.caption("Permite al usuario seleccionar si la temperatura que va a convertir es en Celsius o Fahrenheit, luego ingresa la temperatura y muestra el resultado convertido.")

tempIni = st.radio("Seleccione la temperatura inicial:", ("Celsius", "Fahrenheit"))
temp = st.number_input("Digita la temperatura a convertir: ",value=0)

if  tempIni == "Celsius":
    fahrenheit = (temp * 9/5) + 32
    st.write(f"{temp}°C es igual a {fahrenheit}°F")
else:
    celsius = (temp - 32) * 5/9
    st.write(f"{temp}°F es igual a {celsius}°C")


st.divider()

st.title(" Ejercicio 4: Galeria de Mascotas (Tabs)")
st.caption("*   Crea 3 pestañas: Gatos, Perros, Aves. En cada pestaña muestra una imagen diferente (puedes usar URLs públicas) y un botón de Me gusta que, al ser presionado, muestre un `st.toast` diciendo Te gusta esta mascota.")

st.subheader("Galeria de Mascotas")
tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])
with tab1:
    st.image("https://polymarket-upload.s3.us-east-2.amazonaws.com/OfGD4Mb__400x400_bf0465af-9ec9-49a2-8ba4-1d972f93634a_1721985313247.jpg", caption="Gato")
    if st.button("Me gusta este gato"):
        st.toast("💕 Te gusta esta mascota")
with tab2:
     st.image("https://preview.redd.it/i-weird-dog-i-sculpted-and-printed-v0-k6xwga18enfe1.jpg?width=640&crop=smart&auto=webp&s=ec660d19dee734d9804fe358eeb4f9216ed9cdc5", caption="Perro")
     if st.button("Me gusta este perro"):
        st.toast("💕 Te gusta esta mascota")
with tab3:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG0dTNN-Kz9W06sgvR0cPAlo9MXDWgAA0RDw&s", caption="Ave")
    if st.button("Me gusta esta ave"):
        st.toast("💕 Te gusta esta mascota") 

st.divider()

st.title(" Ejercicio 5: Caja de Comentarios (Formulario)")

with st.form("my_form"):
    st.write("Caja de Comentarios")
    
    asunto = st.text_input("Asunto")
    comentario = st.text_area("Comentario")

    submitted = st.form_submit_button("Enviar Comentario")
    
if submitted:
    st.toast("Comentario enviado con éxito!") 
    st.json({
        "asunto": asunto,
        "comentario": comentario})    
    
    
  
st.divider()