# CodeAlpha_Chatbot
# Enhanced Python Chatbot 🤖

A feature-rich conversational chatbot built with Python using only the standard library. This enhanced version includes personality, memory, games, and much more!

## ✨ Features

### 🧠 **Smart Conversation**
- **Advanced Pattern Matching**: Recognizes many conversation topics and contexts
- **Personality & Mood**: Dynamic responses with emotional intelligence
- **Memory System**: Remembers your name and conversation history
- **Personalized Responses**: Tailored interactions based on your preferences

### 🎮 **Interactive Games**
- **Riddle Game**: Challenge yourself with brain teasers
- **Trivia Quiz**: Test your knowledge on various topics
- **Word Association**: Creative word connection game
- **20 Questions**: Classic guessing game (coming soon!)

### 🎭 **Entertainment**
- **Joke Collection**: 10+ built-in jokes with more variety
- **Fun Facts**: Interesting trivia and amazing facts
- **Story Mode**: Interactive storytelling (coming soon!)
- **Mood Detection**: Responds appropriately to your emotions

### 💾 **Persistence**
- **User Data Storage**: Remembers your name and preferences
- **Conversation Tracking**: Keeps track of topics discussed
- **Session History**: Maintains conversation statistics
- **Automatic Save**: Preserves data between sessions

### 🌟 **Enhanced Topics**
- **Personal Questions**: Name, age, preferences
- **Entertainment**: Movies, music, books, games
- **Daily Life**: Food, weather, time, date
- **Emotional Support**: Compliments, encouragement
- **Learning**: Facts, trivia, educational content

## 🚀 How to Run

```bash
python chatbot.py
```

## 🎯 How to Use

### Basic Conversation
- **Greetings**: "hello", "hi", "hey", "good morning"
- **Personal**: "what's your name?", "how old are you?", "tell me about yourself"
- **Casual**: "how are you?", "what's up?", "how's it going?"

### Entertainment Commands
- **Jokes**: "tell me a joke", "make me laugh", "something funny"
- **Facts**: "fun fact", "did you know", "tell me something interesting"
- **Games**: "let's play", "riddle", "trivia", "word association"

### Topic Discussions
- **Movies**: "favorite movie", "what to watch", "cinema"
- **Music**: "favorite song", "what music", "artist"
- **Books**: "reading", "favorite book", "recommend"
- **Food**: "hungry", "cooking", "favorite dish"

### Utility Commands
- **Time**: "what time is it?", "current time"
- **Date**: "what's the date?", "today's date"
- **Help**: "help", "what can you do?", "commands"
- **Exit**: "bye", "quit", "exit", "goodbye"

## 🎪 Game Examples

### Riddle Game
```
👤 You: riddle
🤖 ChatBot: Here's a riddle for you!
🤖 ChatBot: What has keys but no locks, space but no room, and you can enter but not go inside?
👤 Your answer: keyboard
🤖 ChatBot: 🎉 Correct! You're really smart!
```

### Trivia Quiz
```
👤 You: trivia
🤖 ChatBot: Trivia time!
🤖 ChatBot: What is the largest planet in our solar system?
👤 Your answer: jupiter
🤖 ChatBot: 🎉 Excellent! You got it right!
```

## 💬 Conversation Examples

```
👤 You: Hello!
🤖 ChatBot: Hi there! What's on your mind?

👤 You: My name is Alex
🤖 ChatBot: Nice to meet you, Alex! I'll remember your name.

👤 You: Tell me a joke
🤖 ChatBot: Why don't scientists trust atoms? Because they make up everything!

👤 You: Fun fact
🤖 ChatBot: Did you know? Octopuses have three hearts and blue blood!

👤 You: Let's play a game
🤖 ChatBot: I love games! Want to play 20 questions or word association?

👤 You: How are you?
🤖 ChatBot: I'm doing great, thanks for asking, Alex!
```

## 🛠️ Customization

### Adding New Responses
```python
self.responses['new_topic'] = [
    "Response 1",
    "Response 2",
    "Response 3"
]
```

### Adding New Patterns
```python
self.patterns['new_topic'] = [
    r'\b(keyword1|keyword2|keyword3)\b'
]
```

### Adding New Games
```python
def new_game(self):
    # Game logic here
    return "Game response"
```

### Adding New Facts/Jokes
Simply add to the respective lists in the `responses` dictionary.

## 📁 File Structure

- `chatbot.py` - Main chatbot application
- `chatbot_data.json` - User data storage (auto-created)
- `README.md` - This documentation

## 🔧 Technical Details

- **Language**: Python 3.6+
- **Dependencies**: Standard library only
- **Storage**: JSON file for persistence
- **Pattern Matching**: Regular expressions
- **Error Handling**: Comprehensive exception management
- **Memory Management**: Efficient data structures

## 🎨 Features in Detail

### Memory System
- Remembers your name across sessions
- Tracks conversation topics
- Maintains session statistics
- Personalizes responses based on history

### Game System
- Multiple game types with scoring
- Randomized questions and riddles
- Interactive gameplay
- Expandable game framework

### Personality Engine
- Mood-based responses
- Emotional intelligence
- Context-aware conversations
- Dynamic interaction styles

## 🚀 Future Enhancements

- [ ] More interactive games
- [ ] Story generation mode
- [ ] Advanced AI responses
- [ ] Voice interaction
- [ ] Web interface
- [ ] Multi-language support
- [ ] Learning from conversations
- [ ] Custom user profiles

## 🤝 Contributing

Feel free to extend this chatbot by:
1. Adding new conversation topics
2. Creating more games
3. Improving the personality system
4. Adding new features
5. Enhancing the user interface

---

**Enjoy chatting with your enhanced AI companion!** 🎉
