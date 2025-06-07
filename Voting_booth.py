import streamlit as st
import pandas as pd

# ------------------ Candidate Class ------------------
class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def add_vote(self):
        self.votes += 1

# ------------------ Setup Session State ------------------
if "candidates" not in st.session_state:
    st.session_state.candidates = [
        Candidate("🧑 Hassan"),
        Candidate("👨‍🦱 Nadeem"),
        Candidate("🧔 Usman")
    ]

# ------------------ App Title ------------------
st.title("🗳️ Voting Booth by Hassan Nadeem")
st.markdown("Welcome! Cast your vote and then view the results below.")
st.divider()

# ------------------ Voting Buttons ------------------
st.header("🔘 Cast Your Vote")

cols = st.columns(3)
for i, candidate in enumerate(st.session_state.candidates):
    if cols[i].button(f"✅ Vote for {candidate.name}"):
        candidate.add_vote()
        st.success(f"You voted for {candidate.name}!")

st.divider()

# ------------------ Show Current Votes ------------------
if st.checkbox("📊 Show Vote Counts"):
    st.subheader("Live Vote Count")
    for c in st.session_state.candidates:
        st.write(f"{c.name}: **{c.votes}** votes")

# ------------------ Show Results ------------------
if st.button("🏆 Show Winner"):
    winner = max(st.session_state.candidates, key=lambda c: c.votes)
    st.success(f"🏅 **Winner is {winner.name}** with **{winner.votes} votes**!")

    # Optional bar chart for results
    df = pd.DataFrame({
        "Candidate": [c.name for c in st.session_state.candidates],
        "Votes": [c.votes for c in st.session_state.candidates]
    })
    st.bar_chart(df.set_index("Candidate"))

# ------------------ Reset Button ------------------
if st.button("🔄 Reset Votes"):
    for c in st.session_state.candidates:
        c.votes = 0
    st.warning("All votes have been reset!")

