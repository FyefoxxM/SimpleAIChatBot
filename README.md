# Smart Python Chatbot (v2)

A Python-based chatbot that demonstrates basic artificial intelligence concepts through question handling and thoughtful response patterns. This chatbot can identify different types of questions and provide context-aware responses.

## Features

- 🤔 Question type recognition (what, why, how)
- 💭 Topic extraction from questions
- 🎯 Pattern-based response generation
- 😊 Basic sentiment analysis
- 💡 POS (Part of Speech) tagging

## Prerequisites

- Python 3.6 or higher
- NLTK library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smart-chatbot.git
cd smart-chatbot
```

2. Install required packages:
```bash
python setup.py
```

3. If you encounter NLTK errors, run Python and download required data:
```python
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
```

## Project Structure

```
smart-chatbot/
│
├── chatbot.py         # Main chatbot implementation
├── setup.py          # Setup script for dependencies
└── README.md        # This file
```

## Usage

Run the chatbot:
```bash
python chatbot.py
```

Example interactions:
```
Bot: Hi! I'm a smarter chatbot now. I can handle questions! Type 'bye' to exit.

You: What is machine learning?
Bot: Let me think about machine learning... 

You: How does a computer work?
Bot: Here's a way to approach computer operation...

You: Why is the sky blue?
Bot: The reason for sky color might be...
```

## How It Works

### Question Recognition
The chatbot identifies different types of questions:
- What questions (definitions and explanations)
- How questions (processes and methods)
- Why questions (reasons and causes)

### Response Generation
- Templates based on question type
- Topic extraction from user queries
- Sentiment analysis for emotional context
- Fallback responses for unknown queries

### Natural Language Processing
- Tokenization
- POS tagging
- Stop word removal
- Basic sentiment analysis

## Common Issues & Solutions

### Windows Users
- If 'python' is not recognized:
  - Add Python to PATH or use `py` instead of `python`
  - Use full path: `C:\Users\YourName\AppData\Local\Programs\Python\Python3x\python.exe`

### NLTK Errors
- Run the NLTK downloads manually in Python console
- Ensure internet connection for downloading NLTK data

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Improvements

- [ ] Expanded knowledge base
- [ ] More sophisticated question patterns
- [ ] Conversation context tracking
- [ ] Better natural language understanding
- [ ] Custom response templates

## Support

For support, please open an issue in the GitHub repository.
