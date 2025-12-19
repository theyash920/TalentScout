# TalentScout: AI-Powered Hiring Assistant 🤖💼

TalentScout is an automated recruitment chatbot designed to streamline the initial screening process. It engages candidates in a natural conversation, collects essential professional details, and generates dynamically tailored technical questions based on the candidate's specific tech stack.

---

## 🚀 Features

- **Conversational UI:** Built with Streamlit for a clean, professional user experience.
- **High-Speed Inference:** Powered by **Groq** (using the `llama-3.3-70b-versatile` model) for near-instant responses.
- **Context-Aware Memory:** Utilizes Streamlit Session State to manage multi-turn conversations without losing candidate data.
- **Dynamic Technical Screening:** Automatically detects the candidate's tech stack and generates 3-5 relevant technical questions.
- **Graceful Termination:** Recognizes exit intents and provides a professional closing.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM Provider:** [Groq Cloud](https://groq.com/)
- **Model:** Llama 3.3 70B Versatile
- **Language:** Python 3.9+
- **Environment Management:** Python-dotenv

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/theyash920/TalentScout.git