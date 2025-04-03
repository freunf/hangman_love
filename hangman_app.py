import streamlit as st
import random

# 🔐 Geheime Nachricht
geheimes_wort = "Would you like to come over tonight? We could disappear into a fairy tale for a little while. I miss you and I would really love to see you."
wort = list(geheimes_wort)

# 🔁 Session-Variablen initialisieren
if "anzeige" not in st.session_state:
    st.session_state.anzeige = [b if not b.isalpha() else "_" for b in wort]
if "geraten" not in st.session_state:
    st.session_state.geraten = []
if "nachricht" not in st.session_state:
    st.session_state.nachricht = ""

# ✨ Einleitung
st.markdown("""
### 🧙‍♀️✨ The message is covered with a curse!

*Unfortunately, nobody can read this message since an evil witch was in **Ingolstadt**.*  
**Only your skill with words can still help us...**

💬 *Can you reveal the hidden message?*
""")

# 🎯 Titel & aktueller Stand
st.title("❤️ Hello my love")
st.write("📜 **Whispered hints**: " + ", ".join(st.session_state.geraten))
st.write("Note: You must first press Enter to confirm your entry and Abracadabra to display the entry")
st.text("".join(st.session_state.anzeige))
st.write("There is a slider with which you can hover over the message")

# ✍️ Eingabeformular
with st.form("eingabe_formular", clear_on_submit=True):
    eingabe = st.text_input("🔮 The quill is waiting... Which letter do you want to conjure up on the parchment?", key="eingabefeld")
    abgesendet = st.form_submit_button("Abracadabra✨!")

if abgesendet and eingabe:
    eingabe = eingabe.strip()

    # ✅ Ganze Nachricht erraten
    if eingabe.lower() == geheimes_wort.lower():
        st.session_state.anzeige = list(geheimes_wort)
        st.session_state.nachricht = "🎉 Du hast die ganze Nachricht entschlüsselt!"

    # ✅ Mehrere Buchstaben raten
    elif eingabe.isalpha():
        neue_buchstaben = [b for b in eingabe.lower() if b not in st.session_state.geraten]
        gefunden = False

        for buchstabe in neue_buchstaben:
            st.session_state.geraten.append(buchstabe)
            for index, original in enumerate(wort):
                if original.lower() == buchstabe:
                    st.session_state.anzeige[index] = original
                    gefunden = True

        if not gefunden:
            st.session_state.nachricht = f"❌ The witch's curse is stronger than you thought! Try it again."
        else:
            messages = [
                "✨ Your incantation revealed new letters!",
                "✨ Magical energies have unveiled hidden symbols!",
                "🔮 The enchanted parchment now glows with new revelations!"
            ]
            st.markdown(":heart: :heart: :heart:")
            st.session_state.nachricht = random.choice(messages)

    # ❌ Ungültige Eingabe
    else:
        st.session_state.nachricht = "❌ Enter only letters or the complete sentence."


# 🎉 Erfolg oder Nachricht anzeigen
if st.session_state.anzeige == wort:
    st.success("🎉 You have revealed the secret message!")
    st.balloons()
    st.markdown(":heart: :heart: :heart:")
else:
    st.info(st.session_state.nachricht)
