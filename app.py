import streamlit as st
import requests
import json

# --------- SYNC CLASS ---------
class SyncME:
    def __init__(self):
        self._token = None

    def register(self):
        params = {
            'phone': '351932123123',
            'APPLICATION_VERSION':'3.4.6',
            'version_number':215
        }

        r = self._call('register_2', params)
        self._token = r.get('token')

    def caller_id(self, phone):
        params = {
            "phone": phone,
            "ACCESS_TOKEN": self._token
        }

        return self._call('caller_id/caller_id/v2', params)

    def _call(self, method, params):
        try:
            r = requests.post(
                f'https://api.sync.me/api/{method}',
                data='params=%s' % json.dumps(params),
                headers={"User-Agent": 'Sync.ME Android'}
            )

            return r.json()

        except Exception as e:
            return {"error": str(e)}

# --------- UI ---------
st.title("📞 Ricerca numeri")

sync = SyncME()

# crea token
if not sync._token:
    sync.register()

numeri = st.text_area("Inserisci numeri (uno per riga)")

if st.button("Cerca"):

    lista = numeri.split("\n")

    for n in lista:
        n = n.strip()

        if n:
            risultato = sync.caller_id(n)

            st.write("###", n)
            st.json(risultato)
