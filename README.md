# 🤖 AI Chatbot Auto Reply (Python)

This project is an **AI-powered auto-reply chatbot** that reads chat messages from your screen and automatically generates replies using OpenAI.

It uses GUI automation to copy chat text, analyze it, and send a smart response — making it useful for fun, automation, and experimentation.

---

## 🚀 Features

* 💬 Automatically reads chat messages from screen
* 🤖 Generates AI-based replies using OpenAI
* 🔁 Continuous chat monitoring
* 😂 Fun roasting-style responses
* 📋 Clipboard-based text handling
* ⚡ Fully automated reply system

---

## 🛠️ Technologies Used

* Python
* PyAutoGUI (for screen automation)
* Pyperclip (clipboard handling)
* OpenAI API
* Time module

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-chatbot-auto-reply.git
cd ai-chatbot-auto-reply
```

### 2. Install dependencies

```bash
pip install pyautogui pyperclip openai
```

---

## 🔑 Setup

### 1. Add your OpenAI API Key

Replace this line in the code:

```python
client = OpenAI(api_key="<Your Key Here>")
```

### 2. Adjust Screen Coordinates

Update these coordinates according to your screen:

* Chat window area (for selecting text)
* Input box (for typing reply)
* Browser/app position

Example:

```python
pyautogui.click(831, 140)
```

---

## ▶️ How It Works

1. Script opens the chat window
2. Selects chat messages using mouse drag
3. Copies chat text to clipboard
4. Sends chat to OpenAI for response
5. Copies AI reply
6. Pastes and sends message automatically

---

## ▶️ How to Run

```bash
python chatbot.py
```

---

## 💬 Behavior

* Detects if last message is from a specific sender
* Generates a reply only when needed
* Uses a **funny roasting tone** (customizable)

---

## ⚠️ Important Notes

* Works based on **fixed screen coordinates**
* Requires proper screen resolution setup
* Do not move mouse while script is running ⚠️
* May not work on all chat platforms

---

## 🔮 Future Improvements

* GUI for easy setup
* Dynamic screen detection
* Multi-platform support (WhatsApp, Telegram, etc.)
* Better message parsing
* Custom personality modes

---



## ⭐ Contribute

Feel free to fork this repo and improve the project!

---

## 📜 License

This project is open-source and available under the MIT License.
