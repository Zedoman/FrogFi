# 🐸 FrogFi

The **Efrog Community Hub** is an AI-powered, interactive meme token and trading ecosystem built with **Streamlit, Groq LLaMA, and Python**. It offers simulated token launches, AI-driven trading insights, a meme-generating chatbot, onchain-style games, and community leaderboards.

## 🚀 Features

### **1. Simulated Token Launch**
- Generate a **fun token description** inspired by a chosen **theme and meme.**
- Uses **Groq LLaMA AI** to create unique tokenomics descriptions.

### **2. AI Trading Bot**
- Get **real-time meme token insights** based on AI-generated predictions.
- Uses random market sentiment generation for a **playful trading experience.**

### **3. Croak Royale (Battle Game)**
- Choose an **Efrog Warrior** and battle against AI-powered opponents.
- Features **health bars, battle cries, and turn-based mechanics.**
- Tracks leaderboard stats for the top warriors.

### **4. Leaderboard**
- **Tracks and displays** top warriors in Croak Royale.
- Updates rankings dynamically after each battle.

### **5. Efrog TV (AI-Powered News & Memes)**
- Displays **trending meme token news** (randomized headlines).
- Generates **AI-powered meme captions** on demand.

### **6. CroakGPT (AI Chatbot for Memes & Trading)**
- A chatbot that **provides humorous market insights** on meme tokens.
- Uses **Groq LLaMA-3.3-70B** to generate responses.

### **7. Efrog Avatar Creator**
- Generates a **custom Efrog avatar** based on personality traits.
- Uses **Dicebear API** for fun and unique frog-themed avatars.

---

## 🛠️ Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/Zedoman/FrogFi
cd FrogFi
```

### **2. Set Up Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up API Keys**
- Create a `.env` file in the project root and add your **Groq API key:**
  ```env
  GROQ_API_KEY=your_groq_api_key_here
  ```

### **5. Run the Streamlit App**
```bash
streamlit run efrog_hub.py
```

---

## 🎮 Usage Guide

### **Launching a Meme Token**
1. Navigate to **"Simulated Token Launch"** from the sidebar.
2. Enter the **Token Name, Theme, and Meme Inspiration.**
3. Click **"Generate Tokenomics & Description"** to get AI-generated results.

### **Getting AI Trading Insights**
1. Go to **"AI Trading Bot"** section.
2. Enter a token symbol (e.g., `$CROAK`).
3. Click **"Get AI Prediction"** to receive a trading insight.

### **Battling in Croak Royale**
1. Select **"Croak Royale Game"** from the sidebar.
2. Pick an **Efrog warrior** and start a battle.
3. The game will run an AI-driven battle sequence with health bars and actions.
4. The winner is updated on the **Leaderboard**.

### **Viewing the Leaderboard**
1. Go to **"Leaderboard"** to see the top warriors and their win counts.

### **Watching Efrog TV (Meme Token News & Memes)**
1. Select **"Efrog TV"** from the sidebar.
2. View the latest **randomized AI-powered meme news** and memes.

### **Chatting with CroakGPT**
1. Go to **"CroakGPT"** section.
2. Enter a question about **meme trading, AI insights, or anything fun.**
3. Get a **witty AI-generated response!**

### **Creating Your Efrog Avatar**
1. Select **"Efrog Avatar Creator"** from the sidebar.
2. Enter a **name** and choose a **frog type.**
3. Click **"Generate Avatar"** to receive a custom **Dicebear-generated** Efrog avatar.

---

## 📜 Technologies Used
- **Streamlit** – Web app framework for interactive UI
- **Python** – Core backend logic
- **Groq LLaMA-3.3-70B** – AI-powered responses & insights
- **Random module** – Simulated market trends & battles
- **Dicebear API** – Avatar generation
- **Dotenv** – Secure environment variable management



