import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
import string
import random
import re

# Download required NLTK data
nltk.download('punkt_tab')
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')

class SmartAIChatbot:
    def __init__(self):
        # Enhanced knowledge base with question-answer pairs
        self.knowledge_base = {
            'greetings': {
                'patterns': ['hello', 'hi', 'hey'],
                'responses': [
                    "Hi there! How can I help you today?",
                    "Hello! Nice to meet you!",
                    "Hey! What's on your mind?"
                ]
            },
            'questions': {
                'what': {
                    'patterns': ['what is', 'what are', 'what can'],
                    'responses': [
                        "Let me think about {topic}...",
                        "Regarding {topic}, I would say...",
                        "When it comes to {topic}, here's what I know..."
                    ]
                },
                'how': {
                    'patterns': ['how do', 'how can', 'how does'],
                    'responses': [
                        "Here's a way to approach {topic}...",
                        "When dealing with {topic}, you might want to...",
                        "The process for {topic} typically involves..."
                    ]
                },
                'why': {
                    'patterns': ['why is', 'why do', 'why does'],
                    'responses': [
                        "The reason for {topic} might be...",
                        "Thinking about {topic}, I believe...",
                        "Let me explain why {topic}..."
                    ]
                }
            },
            'farewell': {
                'patterns': ['bye', 'goodbye', 'see you'],
                'responses': [
                    "Goodbye! Have a great day!",
                    "See you later!",
                    "Bye! Come back soon!"
                ]
            }
        }
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))

    def tokenize_and_tag(self, user_input):
        """Clean, tokenize, and POS tag user input"""
        # Clean and tokenize
        cleaned = user_input.lower().translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(cleaned)
        # POS tagging
        tagged = pos_tag(tokens)
        return tokens, tagged

    def extract_topic(self, tokens, question_word):
        """Extract the main topic after a question word"""
        # Find the question word's position
        try:
            q_pos = tokens.index(question_word.lower())
            # Get everything after the question word and auxiliary verbs
            topic_words = tokens[q_pos + 2:]  # Skip question word and auxiliary verb
            # Remove stop words from topic
            topic = ' '.join([word for word in topic_words if word not in self.stop_words])
            return topic if topic else "that"
        except ValueError:
            return "that"

    def identify_question_type(self, user_input, tagged_tokens):
        """Identify the type of question and extract relevant information"""
        question_words = {
            'what': 'what', 'why': 'why', 'how': 'how',
            'when': 'when', 'where': 'where', 'who': 'who'
        }
        
        # Check if it's a question
        is_question = any([
            user_input.endswith('?'),
            any(word.lower() in question_words for word, tag in tagged_tokens),
            any(pattern in user_input.lower() for qtype in self.knowledge_base['questions'] 
                for pattern in self.knowledge_base['questions'][qtype]['patterns'])
        ])
        
        if not is_question:
            return None, None

        # Identify question type and topic
        for q_type, q_info in self.knowledge_base['questions'].items():
            for pattern in q_info['patterns']:
                if pattern in user_input.lower():
                    topic = self.extract_topic(user_input.split(), q_type)
                    return q_type, topic
        
        return 'general', 'that'

    def get_response(self, user_input):
        """Generate a more thoughtful response based on input type"""
        tokens, tagged_tokens = self.tokenize_and_tag(user_input)
        
        # Check for greetings and farewells first
        for category in ['greetings', 'farewell']:
            if any(pattern in user_input.lower() for pattern in self.knowledge_base[category]['patterns']):
                return random.choice(self.knowledge_base[category]['responses'])
        
        # Handle questions
        q_type, topic = self.identify_question_type(user_input, tagged_tokens)
        if q_type:
            if q_type in self.knowledge_base['questions']:
                template = random.choice(self.knowledge_base['questions'][q_type]['responses'])
                return template.format(topic=topic)
            else:
                # Handle general questions
                return f"That's an interesting question about {topic}. Let me think... "

        # If not a question, use sentiment analysis for response
        sentiment = self.analyze_sentiment(user_input)
        if sentiment > 0.2:
            return "I sense your enthusiasm! Tell me more about your thoughts on this."
        elif sentiment < -0.2:
            return "I understand this might be challenging. Would you like to explore this further?"
        else:
            return "I see what you mean. Can you elaborate on that?"

    def analyze_sentiment(self, text):
        """Analyze the sentiment of user input"""
        scores = self.sentiment_analyzer.polarity_scores(text)
        return scores['compound']

    def chat(self):
        """Main chat loop"""
        print("Bot: Hi! I'm a smarter chatbot now. I can handle questions! Type 'bye' to exit.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['bye', 'goodbye', 'exit']:
                print("Bot:", random.choice(self.knowledge_base['farewell']['responses']))
                break
                
            response = self.get_response(user_input)
            print("Bot:", response)

# Create and run the chatbot
if __name__ == "__main__":
    chatbot = SmartAIChatbot()
    chatbot.chat()