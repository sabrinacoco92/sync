import streamlit as st
import requests
import json

# ---- API ----
def cerca_numero(numero):
    try:
        r = requests.post(
            "https://api.sync.me/api/caller_id/caller_id/v2",
            data="params=" + json.dumps({
                "phone": numero
            }),
        )
        return r.json()
    except:
        return {"errore": "request fallita"}

# ---- UI ----
st.title("📞 Ricerca numeri")

numeri = st.text_area("Inserisci numeri (uno per riga)")

if st.button("Cerca"):
    lista = numeri.split("\n")

    for n in lista:
        n = n.strip()

        if n:
            risultato = cerca_numero(n)

            st.write("###", n)
            st.json(risultato)
