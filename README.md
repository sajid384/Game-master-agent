"""
==========================================================
GAME MASTER AGENT (CHAINLIT + GEMINI API)
==========================================================

✅ WHAT IT DOES:
- Starts a fantasy adventure story.
- Simulates a monster battle with a dice roll.
- Gives a reward item after the battle.

==========================================================
1) PREREQUISITES (RUN THESE IN CMD ONE BY ONE)
==========================================================
# Check Python version (3.9 recommended)
python --version

# Install uv (fast package manager)
pip install uv

# Go to the folder where this file is saved
cd "D:\Agentic Ai\Game Master Agent"

# Install requirements using uv
uv pip install chainlit google-generativeai --system

# (If uv gives errors, use pip instead)
pip install chainlit google-generativeai

==========================================================
2) RUN THE AGENT
==========================================================
# Start Chainlit server
chainlit run game_master_agent_complete.py -w

# Open the URL shown in the terminal, e.g.:
http://localhost:8000

==========================================================
3) HOW TO USE
==========================================================
Type anything in the chat, for example:
- start game
- begin adventure
- fight monster

You will get:
✔ A fantasy adventure story
✔ Monster battle result (dice rolled)
✔ Reward item after battle

==========================================================
4) IF PORT 8000 IS BUSY
==========================================================
chainlit run game_master_agent_complete.py -w --port 8080

Then open:
http://localhost:8080

==========================================================
5) MAKE IT PUBLIC (OPTIONAL)
==========================================================
# Install localtunnel (Node.js required)
npm install -g localtunnel

# After running the agent
npx localtunnel --port 8000

You will get a public URL like:
https://cool-game-master.loca.lt

==========================================================
6) STOP THE SERVER
==========================================================
Press CTRL + C in terminal.

==========================================================

