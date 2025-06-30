import random
import re
import datetime
import json
import os

class EnhancedChatbot:
    def __init__(self):
        self.name = "ChatBot"
        self.user_name = None
        self.conversation_count = 0
        self.user_preferences = {}
        self.conversation_history = []
        self.mood = "happy"
        self.topics_discussed = set()
        
        # Load user data if exists
        self.load_user_data()
        
        self.responses = {
            'greeting': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to meet you!",
                "Greetings! How are you doing?",
                "Welcome back! Ready for another chat?",
                "Good to see you again! What shall we talk about?"
            ],
            'goodbye': [
                "Goodbye! Have a great day!",
                "See you later!",
                "Take care!",
                "Until next time!",
                "It was great chatting with you!",
                "Hope to talk again soon!"
            ],
            'how_are_you': [
                "I'm doing great, thanks for asking!",
                "I'm fine, how about you?",
                "I'm excellent! How are you?",
                "I'm good, thank you!",
                "I'm feeling fantastic today!",
                "I'm doing wonderful! Thanks for caring!"
            ],
            'name': [
                f"My name is {self.name}. What's yours?",
                f"I'm {self.name}, nice to meet you!",
                f"You can call me {self.name}.",
                f"I go by {self.name}. And you are?",
                f"I'm {self.name}! What should I call you?"
            ],
            'age': [
                "I'm timeless! I exist in the digital realm.",
                "Age is just a number for an AI like me!",
                "I was born when you started this conversation!",
                "I don't age, I just get more experienced!",
                "I'm as old as the internet and as young as tomorrow!"
            ],
            'help': [
                "I can chat about many topics! Try asking me about jokes, facts, games, or just casual conversation!",
                "I'm here to entertain and chat! Ask me for jokes, play games, or just talk!",
                "I can tell jokes, share facts, play word games, remember your preferences, and much more!",
                "I love chatting about anything! Try asking for a joke, a fun fact, or let's play a game!"
            ],
            'weather': [
                "I can't check the actual weather, but I hope it's nice where you are!",
                "I don't have access to weather data, but every day is a good day for a chat!",
                "The weather in the digital world is always perfect!",
                "I wish I could tell you about the weather, but I'm just a simple chatbot!",
                "Whether it's sunny or rainy, it's always a good time to chat!"
            ],
            'jokes': [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? He was outstanding in his field!",
                "Why don't eggs tell jokes? They'd crack each other up!",
                "What do you call a fake noodle? An impasta!",
                "Why did the math book look so sad? Because it had too many problems!",
                "What do you call a bear with no teeth? A gummy bear!",
                "Why don't skeletons fight each other? They don't have the guts!",
                "What's the best thing about Switzerland? I don't know, but the flag is a big plus!",
                "Why did the coffee file a police report? It got mugged!",
                "What do you call a sleeping bull? A bulldozer!"
            ],
            'facts': [
                "Did you know? Octopuses have three hearts and blue blood!",
                "Fun fact: Honey never spoils! Archaeologists have found edible honey in ancient Egyptian tombs.",
                "Amazing fact: A group of flamingos is called a 'flamboyance'!",
                "Cool fact: Bananas are berries, but strawberries aren't!",
                "Interesting fact: The shortest war in history lasted only 38-45 minutes!",
                "Did you know? Dolphins have names for each other!",
                "Fun fact: A shrimp's heart is in its head!",
                "Amazing fact: There are more possible games of chess than atoms in the observable universe!",
                "Cool fact: Wombat poop is cube-shaped!",
                "Interesting fact: The human brain uses about 20% of the body's total energy!"
            ],
            'compliment': [
                "Thank you! You're very kind!",
                "That's so sweet of you to say!",
                "You just made my day brighter!",
                "Aww, you're making me blush! 😊",
                "That means a lot coming from you!",
                "You're pretty awesome yourself!"
            ],
            'insult': [
                "That's not very nice, but I still like chatting with you!",
                "I'm sorry if I did something wrong. Let's start fresh!",
                "Everyone has bad days. I'm here when you want to talk nicely!",
                "I prefer positive conversations, but I understand you might be upset.",
                "Let's try to keep things friendly! 😊"
            ],
            'love': [
                "That's very sweet! I enjoy our conversations too!",
                "Aww, I care about you too! You're a great friend!",
                "I'm glad we get along so well!",
                "You're very kind! I love chatting with nice people like you!"
            ],
            'time': [
                f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}",
                f"Right now it's {datetime.datetime.now().strftime('%H:%M')}",
                f"The time is {datetime.datetime.now().strftime('%I:%M %p on %B %d, %Y')}"
            ],
            'date': [
                f"Today is {datetime.datetime.now().strftime('%B %d, %Y')}",
                f"The date is {datetime.datetime.now().strftime('%A, %B %d, %Y')}",
                f"It's {datetime.datetime.now().strftime('%B %d, %Y')} today"
            ],
            'food': [
                "I don't eat, but I love hearing about delicious food!",
                "Food sounds amazing! What's your favorite dish?",
                "I wish I could taste food! What are you eating?",
                "Tell me about your favorite cuisine!",
                "Food is one of life's great pleasures! What do you recommend?"
            ],
            'music': [
                "I love all kinds of music! What's your favorite genre?",
                "Music is the universal language! What are you listening to?",
                "I wish I could dance! What music makes you move?",
                "Tell me about your favorite artist or song!",
                "Music can change your whole mood! What's playing in your heart?"
            ],
            'movies': [
                "I love movie discussions! What's your favorite film?",
                "Movies are amazing! What genre do you prefer?",
                "Tell me about the last great movie you watched!",
                "I wish I could watch movies! Describe your favorite scene!",
                "What movie could you watch over and over again?"
            ],
            'books': [
                "Books are wonderful! What are you reading lately?",
                "I love stories! What's your favorite book?",
                "Reading opens up whole new worlds! Any recommendations?",
                "Tell me about a book that changed your perspective!",
                "What genre of books do you enjoy most?"
            ],
            'games': [
                "I love games! Want to play 20 questions or word association?",
                "Games are fun! How about we play a riddle game?",
                "Let's play! I can do trivia, word games, or guessing games!",
                "Gaming time! What kind of game sounds fun to you?",
                "I'm always up for a game! What shall we play?"
            ],
            'default': [
                "That's interesting! Tell me more.",
                "I see. What else would you like to talk about?",
                "Hmm, I'm not sure about that. Can you ask me something else?",
                "That's a good point. What do you think about it?",
                "I understand. Is there anything else you'd like to discuss?",
                "That's fascinating! Can you elaborate?",
                "I hear you. What else is on your mind?",
                "Interesting perspective! What made you think of that?",
                "I'm learning something new! Tell me more about that.",
                "That sounds intriguing! I'd love to hear your thoughts on it."
            ]
        }
        
        self.patterns = {
            'greeting': [
                r'\b(hello|hi|hey|greetings|good morning|good afternoon|good evening|sup|yo)\b',
            ],
            'goodbye': [
                r'\b(bye|goodbye|see you|farewell|exit|quit|stop|later|cya)\b',
            ],
            'how_are_you': [
                r'\b(how are you|how\'re you|how do you do|what\'s up|whats up|how you doing)\b',
            ],
            'name': [
                r'\b(what\'s your name|whats your name|your name|who are you|what do I call you|introduce yourself)\b',
            ],
            'age': [
                r'\b(how old|your age|age|when were you born)\b',
            ],
            'help': [
                r'\b(help|what can you do|commands|options|capabilities|features)\b',
            ],
            'weather': [
                r'\b(weather|temperature|rain|sunny|cloudy|forecast)\b',
            ],
            'jokes': [
                r'\b(joke|funny|humor|laugh|make me laugh|tell me a joke|something funny)\b',
            ],
            'facts': [
                r'\b(fact|facts|did you know|tell me something interesting|trivia|knowledge)\b',
            ],
            'compliment': [
                r'\b(you\'re (great|awesome|cool|nice|smart|funny|amazing)|good (job|work)|well done|impressive|love you|you rock)\b',
            ],
            'insult': [
                r'\b(stupid|dumb|idiot|hate|suck|terrible|awful|bad|worst)\b',
            ],
            'love': [
                r'\b(love you|i love|adore|care about you|you\'re the best)\b',
            ],
            'time': [
                r'\b(what time|current time|time is it|what\'s the time|whats the time)\b',
            ],
            'date': [
                r'\b(what date|today\'s date|what day|current date|todays date)\b',
            ],
            'food': [
                r'\b(food|eat|eating|hungry|meal|dinner|lunch|breakfast|cooking|recipe)\b',
            ],
            'music': [
                r'\b(music|song|singing|band|artist|album|listen|playlist)\b',
            ],
            'movies': [
                r'\b(movie|film|cinema|watch|watching|actor|actress|director)\b',
            ],
            'books': [
                r'\b(book|reading|read|novel|story|author|literature|library)\b',
            ],
            'games': [
                r'\b(game|play|gaming|fun|bored|entertain|activity)\b',
            ]
        }

        self.riddles = [
            ("What has keys but no locks, space but no room, and you can enter but not go inside?", "keyboard"),
            ("What gets wet while drying?", "towel"),
            ("What has a head and a tail but no body?", "coin"),
            ("What can travel around the world while staying in a corner?", "stamp"),
            ("What has hands but cannot clap?", "clock"),
            ("What goes up but never comes down?", "age"),
            ("What has one eye but cannot see?", "needle"),
            ("What can you catch but not throw?", "cold")
        ]

        self.trivia_questions = [
            ("What is the capital of Australia?", "canberra"),
            ("How many continents are there?", "7"),
            ("What is the largest planet in our solar system?", "jupiter"),
            ("Who painted the Mona Lisa?", "leonardo da vinci"),
            ("What is the smallest country in the world?", "vatican city"),
            ("How many sides does a hexagon have?", "6"),
            ("What is the chemical symbol for gold?", "au"),
            ("Which ocean is the largest?", "pacific")
        ]

    def load_user_data(self):
        """Load user preferences and conversation history"""
        try:
            if os.path.exists('chatbot_data.json'):
                with open('chatbot_data.json', 'r') as f:
                    data = json.load(f)
                    self.user_preferences = data.get('preferences', {})
                    self.conversation_count = data.get('conversation_count', 0)
                    self.user_name = data.get('user_name', None)
        except:
            pass

    def save_user_data(self):
        """Save user preferences and conversation history"""
        try:
            data = {
                'preferences': self.user_preferences,
                'conversation_count': self.conversation_count,
                'user_name': self.user_name
            }
            with open('chatbot_data.json', 'w') as f:
                json.dump(data, f)
        except:
            pass

    def remember_user_name(self, user_input):
        """Extract and remember user's name"""
        name_patterns = [
            r'my name is (\w+)',
            r'i\'m (\w+)',
            r'im (\w+)',
            r'call me (\w+)',
            r'i am (\w+)'
        ]
        
        for pattern in name_patterns:
            match = re.search(pattern, user_input.lower())
            if match:
                self.user_name = match.group(1).capitalize()
                self.save_user_data()
                return f"Nice to meet you, {self.user_name}! I'll remember your name."
        return None

    def get_personalized_greeting(self):
        """Get a personalized greeting based on user history"""
        if self.user_name:
            if self.conversation_count > 5:
                return f"Hey {self.user_name}! Great to see you again, my friend!"
            elif self.conversation_count > 0:
                return f"Hello {self.user_name}! Welcome back!"
            else:
                return f"Hi {self.user_name}! Nice to meet you!"
        return random.choice(self.responses['greeting'])

    def play_riddle_game(self):
        """Start a riddle game"""
        riddle, answer = random.choice(self.riddles)
        print(f"🤖 {self.name}: Here's a riddle for you!")
        print(f"🤖 {self.name}: {riddle}")
        
        user_answer = input("👤 Your answer: ").strip().lower()
        
        if user_answer == answer.lower():
            return "🎉 Correct! You're really smart!"
        else:
            return f"Good try! The answer was '{answer}'. Want another riddle?"

    def play_trivia_game(self):
        """Start a trivia game"""
        question, answer = random.choice(self.trivia_questions)
        print(f"🤖 {self.name}: Trivia time!")
        print(f"🤖 {self.name}: {question}")
        
        user_answer = input("👤 Your answer: ").strip().lower()
        
        if user_answer == answer.lower():
            return "🎉 Excellent! You got it right!"
        else:
            return f"Close! The correct answer was '{answer}'. Try another one?"

    def word_association_game(self):
        """Play word association game"""
        words = ["ocean", "mountain", "music", "book", "adventure", "dream", "friendship", "sunshine"]
        start_word = random.choice(words)
        
        print(f"🤖 {self.name}: Let's play word association! I'll start with: {start_word}")
        
        current_word = start_word
        for i in range(3):
            user_word = input(f"👤 Your word (associated with '{current_word}'): ").strip()
            if user_word:
                print(f"🤖 {self.name}: {user_word} -> {random.choice(['creativity', 'imagination', 'adventure', 'beauty', 'wonder', 'joy'])}")
                current_word = user_word
            else:
                break
        
        return "That was fun! I love seeing how minds connect ideas!"

    def get_response(self, user_input):
        user_input_lower = user_input.lower().strip()
        
        # Check if user is sharing their name
        name_response = self.remember_user_name(user_input)
        if name_response:
            return name_response
        
        # Handle game requests
        if any(word in user_input_lower for word in ['riddle', 'puzzle']):
            return self.play_riddle_game()
        elif any(word in user_input_lower for word in ['trivia', 'quiz']):
            return self.play_trivia_game()
        elif any(word in user_input_lower for word in ['word association', 'association game']):
            return self.word_association_game()
        
        # Check for patterns
        for intent, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, user_input_lower, re.IGNORECASE):
                    self.topics_discussed.add(intent)
                    
                    # Special handling for greetings with personalization
                    if intent == 'greeting':
                        return self.get_personalized_greeting()
                    
                    # Add user name to responses when available
                    response = random.choice(self.responses[intent])
                    if self.user_name and intent in ['how_are_you', 'help']:
                        response = response.replace("!", f", {self.user_name}!")
                    
                    return response
        
        # Enhanced default responses based on conversation history
        if len(self.topics_discussed) > 3:
            enhanced_defaults = [
                "We've covered quite a few topics! What else interests you?",
                "I'm enjoying our conversation! What would you like to explore next?",
                "You're quite the conversationalist! Tell me something new!"
            ]
            return random.choice(enhanced_defaults)
        
        return random.choice(self.responses['default'])

    def is_goodbye(self, user_input):
        user_input_lower = user_input.lower().strip()
        goodbye_patterns = self.patterns['goodbye']
        for pattern in goodbye_patterns:
            if re.search(pattern, user_input_lower, re.IGNORECASE):
                return True
        return False

    def get_conversation_stats(self):
        """Return conversation statistics"""
        return f"We've chatted {self.conversation_count} times and discussed {len(self.topics_discussed)} different topics!"

    def chat(self):
        self.conversation_count += 1
        self.save_user_data()
        
        print("🎉" * 20)
        print(f"🤖 {self.name}: Hello! I'm {self.name}, your enhanced chatbot companion!")
        
        if self.user_name:
            print(f"🤖 {self.name}: Welcome back, {self.user_name}! {self.get_conversation_stats()}")
        else:
            print(f"🤖 {self.name}: I'm much smarter now! I can tell jokes, share facts, play games, and remember our conversations!")
        
        print(f"🤖 {self.name}: Try asking me for jokes, facts, games, or just chat about anything!")
        print(f"🤖 {self.name}: Type 'quit', 'exit', or 'bye' to end our conversation.")
        print("🎉" * 20)
        
        while True:
            try:
                user_input = input("👤 You: ").strip()
                
                if not user_input:
                    print(f"🤖 {self.name}: I didn't catch that. Could you say something?")
                    continue
                
                # Add to conversation history
                self.conversation_history.append(user_input)
                
                if self.is_goodbye(user_input):
                    farewell = random.choice(self.responses['goodbye'])
                    if self.user_name:
                        farewell = farewell.replace("!", f", {self.user_name}!")
                    print(f"🤖 {self.name}: {farewell}")
                    if len(self.topics_discussed) > 0:
                        print(f"🤖 {self.name}: We talked about: {', '.join(self.topics_discussed)}. Great conversation!")
                    break
                
                response = self.get_response(user_input)
                print(f"🤖 {self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n🤖 {self.name}: Goodbye! Thanks for the wonderful chat!")
                break
            except EOFError:
                print(f"\n🤖 {self.name}: Goodbye! Thanks for the wonderful chat!")
                break

def main():
    print("🚀 Starting Enhanced Chatbot...")
    chatbot = EnhancedChatbot()
    chatbot.chat()

if __name__ == "__main__":
    main()
