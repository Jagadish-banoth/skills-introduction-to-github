# Simple Conversational Chatbot

A lightweight, rule-based chatbot built with Python that can engage in simple conversations using pattern matching.

## Features

- **Pattern-based responses**: Recognizes common greetings, questions, and conversation patterns
- **Randomized responses**: Provides varied responses to keep conversations interesting
- **Interactive mode**: Engages in real-time conversations with users
- **Simple and extensible**: Easy to understand and modify for learning purposes

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation

No installation required! The chatbot uses only Python's standard library.

Simply clone this repository or download the `chatbot.py` file:

```bash
git clone https://github.com/Jagadish-banoth/skills-introduction-to-github.git
cd skills-introduction-to-github
```

## Usage

### Interactive Mode

To start a conversation with the chatbot, run:

```bash
python3 chatbot.py
```

or

```bash
python chatbot.py
```

Then simply type your messages and press Enter. The chatbot will respond to your input.

To exit the conversation, type `quit` or `exit`, or press `Ctrl+C`.

### Example Conversation

```
ChatBot: Hello! I'm a simple conversational chatbot.
ChatBot: Type 'quit' or 'exit' to end the conversation.

You: hello
ChatBot: Hi there! Nice to meet you!

You: what is your name?
ChatBot: I'm ChatBot, a simple conversational chatbot!

You: tell me a joke
ChatBot: Why don't scientists trust atoms? Because they make up everything!

You: thanks
ChatBot: You're welcome!

You: bye
ChatBot: Goodbye! It was nice chatting with you!
```

### Using as a Module

You can also import and use the chatbot in your own Python scripts:

```python
from chatbot import SimpleChatbot

# Create a chatbot instance
bot = SimpleChatbot(name="MyBot")

# Get a single response
response = bot.get_response("Hello!")
print(response)

# Start an interactive chat session
bot.chat()
```

## What the Chatbot Can Do

The chatbot can respond to various types of input:

- **Greetings**: "hi", "hello", "hey"
- **Asking about itself**: "what is your name?", "who are you?"
- **Status inquiries**: "how are you?"
- **Help requests**: "help", "what can you do?"
- **Weather questions**: "what's the weather?"
- **Thanks**: "thank you", "thanks"
- **Goodbyes**: "bye", "goodbye", "see you"
- **Jokes**: "tell me a joke", "something funny"
- **General conversation**: Various positive/negative sentiment expressions

## Customization

You can easily customize the chatbot by modifying the `patterns` dictionary in the `SimpleChatbot` class:

```python
self.patterns = {
    r'your_regex_pattern': [
        "Response 1",
        "Response 2",
        "Response 3"
    ],
    # Add more patterns here
}
```

Each pattern is a regular expression that will be matched against user input (case-insensitive). When a match is found, the chatbot randomly selects one of the associated responses.

## How It Works

The chatbot uses a simple rule-based approach:

1. **Pattern Matching**: User input is matched against predefined regex patterns
2. **Response Selection**: When a pattern matches, a random response from that pattern's list is selected
3. **Default Responses**: If no pattern matches, a generic response is returned
4. **Case Insensitive**: All matching is done in a case-insensitive manner

## Limitations

This is a simple educational chatbot with several limitations:

- No natural language understanding (NLP)
- No learning or memory between sessions
- No context awareness beyond the current message
- Limited to predefined patterns and responses
- Cannot access external data or services

## Learning and Extending

This chatbot is designed as a learning tool. Here are some ideas for extending it:

- Add more patterns and responses
- Implement conversation context/memory
- Add logging of conversations
- Create a web interface using Flask
- Integrate with APIs (weather, news, etc.)
- Add sentiment analysis
- Implement machine learning for better responses

## License

MIT License - See LICENSE file for details

## Contributing

This is an educational project. Feel free to fork and experiment with your own improvements!

## Author

Created as part of the GitHub Skills introduction exercise.
