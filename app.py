import streamlit as st
import random
import groq
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq LLaMA API
# groq.api_key = "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"

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.warning("Please set your GROQ_API_KEY in the environment variables.")

# Initialize Groq Client
client = groq.Client(api_key=groq_api_key)

def generate_token_description(name, theme, meme):
    prompt = f"""
    Create a fun token description for {name}, inspired by {theme} and {meme}:
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Using Groq's latest LLaMA model
        messages=[
            {"role": "system", "content": "You are an AI that generates fun token descriptions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=256
    )
    return response.choices[0].message.content

def generate_trading_insight(token):
    insights = [
        f"{token} is mooning! Frogs are taking over. 🚀",
        f"{token} is dipping! Time to buy the dip, legend. 🐸",
        f"{token} is croaking loudly—expect some volatility! 📈"
    ]
    return random.choice(insights)

def generate_meme_caption(topic):
    prompt = f"Generate a funny meme caption about {topic}."
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an AI that generates meme captions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=50
    )
    return response.choices[0].message.content

def get_frog_news():
    # Simulated frog-related news, can be expanded with real API scraping
    news = [
        "🐸 New meme token $CROAK surges 300% overnight!",
        "🌿 Swamp Kings unite! Community rallies for Efrog dominance.",
        "🎮 Onchain gaming heats up with Croak Royale battles!"
    ]
    return random.choice(news)

def generate_avatar(name, frog_type):
    """Generate a unique Efrog avatar with random traits and a valid image URL."""
    
    # Define frog traits with HEX color codes
    traits = {
        "Swamp King": {
            "powers": "Commands the murky depths with an iron croak!",
            "colors": ["4F7942", "2E4E1E", "6B4226"],  # Green, Dark Green, Brown
            "accessories": ["crown", "cape", "scepter"],
            "expression": ["smug", "proud", "mysterious"]
        },
        "Lily Jumper": {
            "powers": "Leaps across lily pads with lightning speed!",
            "colors": ["D4AF37", "76D7C4", "20B2AA"],  # Gold, Teal, Light Aqua
            "accessories": ["bandana", "goggles", "jetpack"],
            "expression": ["happy", "excited", "determined"]
        },
        "Tadpole Titan": {
            "powers": "Tiny but mighty, strikes fear into bigger frogs!",
            "colors": ["4682B4", "6A5ACD", "00FFFF"],  # Steel Blue, Slate Blue, Cyan
            "accessories": ["spiked collar", "tiny sword", "eye patch"],
            "expression": ["angry", "focused", "playful"]
        },
        "Croak Master": {
            "powers": "A sage of the swamp, wise in the ways of the Croak!",
            "colors": ["808080", "556B2F", "C0C0C0"],  # Gray, Olive, Silver
            "accessories": ["wizard hat", "scroll", "glowing eyes"],
            "expression": ["serene", "wise", "calm"]
        }
    }

    # Pick a random trait
    selected = traits.get(frog_type, traits["Swamp King"])  # Default to Swamp King if invalid type
    color = random.choice(selected["colors"])  # Valid hex color
    accessory = random.choice(selected["accessories"])
    expression = random.choice(selected["expression"])

    # Generate a fun description
    description = f"{name} the {frog_type} is a legendary Efrog warrior! {selected['powers']} Known for their {accessory} and a {expression} expression."

    # Generate a valid Dicebear avatar URL
    avatar_url = f"https://api.dicebear.com/7.x/bottts/svg?seed={name}&backgroundColor={color}&accessories[]={accessory}&mood[]={expression}"

    return description, avatar_url


if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = {}

# Frog attributes (Health & Power levels)
frogs = {
    "Swamp King": {"health": 120, "power": 15},
    "Lily Jumper": {"health": 100, "power": 18},
    "Tadpole Titan": {"health": 90, "power": 20},
    "Croak Master": {"health": 110, "power": 16},
}

# Battle cries to add personality
battle_cries = {
    "Swamp King": "For the Swamp! 🏞️",
    "Lily Jumper": "Jump to Victory! 🌿",
    "Tadpole Titan": "Tiny but Mighty! ⚡",
    "Croak Master": "Croak and Conquer! 🐸",
}

def battle(user_frog, opponent_frog):
    """Simulate a turn-based battle with real-time visuals."""
    user_stats = frogs[user_frog].copy()
    opponent_stats = frogs[opponent_frog].copy()

    st.write(f"**{user_frog} shouts:** {battle_cries[user_frog]}")
    st.write(f"**{opponent_frog} shouts:** {battle_cries[opponent_frog]}")
    
    # Health bars
    user_health_bar = st.progress(1.0)
    opponent_health_bar = st.progress(1.0)

    # Battle Loop
    round_num = 1
    while user_stats["health"] > 0 and opponent_stats["health"] > 0:
        st.subheader(f"⚔️ Round {round_num} ⚔️")
        time.sleep(1)

        # User attacks opponent
        user_damage = random.randint(5, user_stats["power"])
        opponent_stats["health"] = max(0, opponent_stats["health"] - user_damage)
        st.write(f"💥 {user_frog} attacks {opponent_frog} for **{user_damage}** damage!")
        opponent_health_bar.progress(opponent_stats["health"] / 120)
        time.sleep(1)

        # Check if opponent is defeated
        if opponent_stats["health"] <= 0:
            st.success(f"🎉 **{user_frog} wins the battle!** 🏆")
            return user_frog

        # Opponent attacks user
        opponent_damage = random.randint(5, opponent_stats["power"])
        user_stats["health"] = max(0, user_stats["health"] - opponent_damage)
        st.write(f"💥 {opponent_frog} strikes back, dealing **{opponent_damage}** damage!")
        user_health_bar.progress(user_stats["health"] / 120)
        time.sleep(1)

        # Check if user is defeated
        if user_stats["health"] <= 0:
            st.error(f"💀 **{opponent_frog} wins the battle!** 🏆")
            return opponent_frog

        round_num += 1  # Increase round count


def update_leaderboard(winner):
    if winner in st.session_state.leaderboard:
        st.session_state.leaderboard[winner] += 1
    else:
        st.session_state.leaderboard[winner] = 1

def display_leaderboard():
    """Show the leaderboard in a sorted order."""
    sorted_leaderboard = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1], reverse=True)
    
    st.write("## 🏆 Efrog Warriors Leaderboard")
    for idx, (name, wins) in enumerate(sorted_leaderboard, 1):
        medal = "🥇" if idx == 1 else "🥈" if idx == 2 else "🥉" if idx == 3 else "🎖️"
        st.write(f"{medal} **{name}**: {wins} wins")


# Streamlit UI
st.title("🐸 Efrog Community Hub")
tabs = st.sidebar.radio("Select an AI Feature", ["Simulated Token Launch", "AI Trading Bot", "Croak Royale Game", "Leaderboard", "Efrog TV", "CroakGPT", "Efrog Avatar Creator"])
leaderboard = {}


if tabs == "Simulated Token Launch":
    st.header("🚀 Launch Your Own Token!")
    name = st.text_input("Token Name")
    theme = st.text_input("Token Theme")
    meme = st.text_input("Meme Inspiration")
    if st.button("Generate Tokenomics & Description"):
        description = generate_token_description(name, theme, meme)
        st.success(description)

elif tabs == "AI Trading Bot":
    st.header("📈 AI Trading Insights")
    token = st.text_input("Enter Token Name (e.g., $CROAK)")
    if st.button("Get AI Prediction"):
        insight = generate_trading_insight(token)
        st.success(insight)

elif tabs == "Croak Royale Game":
    st.header("🎮 Battle in Croak Royale!")
    user_frog = st.selectbox("Choose your Efrog warrior:", list(frogs.keys()))
    opponent_frog = random.choice(list(frogs.keys()))
    
    if st.button("Start Battle!"):
        winner = battle(user_frog, opponent_frog)
        update_leaderboard(winner)

elif tabs == "Leaderboard":
    display_leaderboard()


elif tabs == "Efrog TV":
    st.header("📺 Efrog TV - AI-Powered News & Highlights")
    st.write(get_frog_news())
    st.write("Trending Meme:", generate_meme_caption("Frog Memes"))

elif tabs == "CroakGPT":
    st.header("🤖 CroakGPT - AI Meme & Trading Chatbot")
    user_input = st.text_input("Ask CroakGPT anything about meme tokens!")
    if st.button("Get Response"):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a wise meme frog giving market insights humorously."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.8,
            max_tokens=256
        )
        st.write(response.choices[0].message.content)

elif tabs == "Efrog Avatar Creator":
    st.header("🎨 Efrog Avatar Creator")
    name = st.text_input("Enter Your Name")
    frog_type = st.selectbox("Choose Your Frog Type", ["Swamp King", "Lily Jumper", "Tadpole Titan", "Croak Master"])
    if st.button("Generate Avatar"):
        avatar = generate_avatar(name, frog_type)
        st.success(avatar)