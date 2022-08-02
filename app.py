from slackbot import SlackBot
import streamlit as st


def check_password() -> bool:
    """Returns `True` if the user had the correct password."""

    def password_entered() -> None:
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True


slackbot = SlackBot(st.secrets["TOKEN"], st.secrets["CHANNEL_ID"])

if check_password():
    message = st.text_input("Message")
    if st.button("Send Slack message to #bot_lightning"):
        slackbot.send_message(message)
