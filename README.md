# La Copa del Mundo de Diego 🏆⚽

An interactive 2026 FIFA World Cup bracket game made for a 6-year-old. It shows
all 48 teams, who advanced through the group stage and Round of 32 (real
results), and then lets you **click the winners** from the Round of 16 all the
way to the champion — drawn as one visual bracket with connecting lines, plus
each match's date, kickoff time, city, and stadium.

Group stage, Round of 32, and the July 4 Round-of-16 matches use **real results**
(source: Wikipedia). Every match from **July 5 onward is interactive** — nothing
is pre-filled, you play it.

## Run locally

Just open `index.html` in any browser — it's a self-contained static page.

Or run it through Streamlit:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Cloud

1. Push this repo to GitHub.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. **New app** → pick this repo, branch `main`, main file `streamlit_app.py`.
4. Deploy.

`streamlit_app.py` renders `index.html` full-page inside the Streamlit app.
