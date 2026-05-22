import streamlit as st

st.title("📞 Ricerca numeri")

numeri = st.text_area("Inserisci numeri (uno per riga)")

if st.button("Cerca"):
    lista = numeri.split("\n")

    for n in lista:
        n = n.strip()
        if n:
            st.write("Numero:", n)
