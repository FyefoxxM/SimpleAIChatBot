# Enhanced Python Chatbot with Knowledge Base

A simple yet powerful chatbot implementation in Python that features natural language processing, sentiment analysis, and an expandable knowledge base system. This chatbot can learn new information through interaction and provides context-aware responses.

## Features

- 🧠 Expandable JSON-based knowledge base
- 💡 Natural Language Processing using NLTK
- 🎯 Pattern matching for accurate responses
- 📚 Learning capability for new facts and topics
- 😊 Sentiment analysis for context-aware responses
- 🔄 Easy to extend and modify

## Prerequisites

- Python 3.6 or higher
- NLTK library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/enhanced-chatbot.git
cd enhanced-chatbot
```

2. Install required packages:
```bash
pip install nltk
```

3. Download required NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
```

## Project Structure

```
enhanced-chatbot/
│
├── chatbot.py            # Main chatbot implementation
├── setup.py             # Setup script for dependencies
├── knowledge/           # Knowledge base directory
│   ├── facts.json      # Domain knowledge and definitions
│   ├── responses.json  # Response patterns and templates
│   └── categories.json # Topic categorization
└── README.md           # This file
```

## Usage

1. Run the chatbot:
```bash
python chatbot.py
```

2. Interact with the chatbot:
- Ask questions about known topics
- Type 'teach' to add new knowledge
- Type 'bye' to exit

Example conversation:
```
Bot: Hi! I'm a knowledgeable chatbot. I can learn new things too!
     Type 'teach' to teach me something new, or 'bye' to exit.
You: What is Python?
Bot: Python is a high-level programming language. 
     Related terms: programming, coding, software
You: teach
Bot: Teach me something new!
What's the topic? machine learning
What's the definition? A subset of AI that enables systems to learn from data
Any related terms? AI, neural networks, deep learning
Any categories? technology, computer science
Bot: Thanks! I've learned about machine learning!
```

## Extending the Knowledge Base

### Through Chat Interface

1. Start the chatbot
2. Type 'teach'
3. Follow the prompts to add new knowledge

### Through Code

```python
chatbot.add_knowledge("new_topic", {
    "definition": "Your definition here",
    "related_terms": ["term1", "term2"],
    "categories": ["category1", "category2"]
})

chatbot.add_response_pattern(
    "category_name",
    "pattern_to_match",
    ["response template 1", "response template 2"]
)
```

## Features in Detail

### Knowledge Base Structure

- **Facts**: Contains definitions, related terms, and categories for each topic
- **Responses**: Stores patterns and response templates for different types of queries
- **Categories**: Organizes topics into broader categories for better context

### Natural Language Processing

- Tokenization of user input
- Lemmatization for better word matching
- Stop word removal
- Part-of-speech tagging
- Sentiment analysis for context-aware responses

### Pattern Matching

- Direct keyword matching
- Related terms matching
- Category-based matching
- Sentiment-based response selection

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- NLTK team for the excellent NLP tools
- Python community for inspiration and support

## Future Enhancements

- [ ] Multi-language support
- [ ] Conversation context tracking
- [ ] Enhanced pattern matching using fuzzy logic
- [ ] Web interface
- [ ] Database integration for knowledge base
- [ ] API endpoint support

## Support

For support, please open an issue in the GitHub repository or contact [your-email@example.com].
