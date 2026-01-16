#!/usr/bin/env python3
"""
Simple Conversational Chatbot
A basic chatbot that can engage in simple conversations using pattern matching.
"""

import re
import random


class SimpleChatbot:
    """A simple rule-based chatbot that responds to user inputs."""
    
    def __init__(self, name="ChatBot"):
        self.name = name
        self.patterns = {
            r'\b(hi|hello|hey)\b': [
                f"Hello! I'm {name}. How can I help you today?",
                f"Hi there! Nice to meet you!",
                f"Hey! What's on your mind?"
            ],
            r'\bhow are you\b': [
                "I'm doing great, thank you for asking!",
                "I'm just a bot, but I'm functioning perfectly!",
                "All systems operational! How are you?"
            ],
            r'\b(what is your name|who are you)\b': [
                f"I'm {name}, a simple conversational chatbot!",
                f"My name is {name}. I'm here to chat with you!",
                f"I go by {name}. Nice to meet you!"
            ],
            r'\b(help|what can you do)\b': [
                "I can chat with you! Try asking me about myself, the weather, or just say hello!",
                "I'm a simple chatbot. I can respond to greetings, questions about myself, and general conversation.",
                "I can answer basic questions and have a simple conversation with you!"
            ],
            r'\b(weather|temperature)\b': [
                "I don't have access to weather data, but I hope it's nice where you are!",
                "I'm not connected to weather services, but I hope you're enjoying good weather!",
                "As a simple chatbot, I can't check the weather, but I hope it's pleasant outside!"
            ],
            r'\b(thank you|thanks)\b': [
                "You're welcome!",
                "Happy to help!",
                "My pleasure!",
                "Anytime!"
            ],
            r'\b(bye|goodbye|see you)\b': [
                "Goodbye! It was nice chatting with you!",
                "See you later! Have a great day!",
                "Bye! Come back anytime!"
            ],
            r'\b(good|great|awesome|excellent)\b': [
                "That's wonderful to hear!",
                "Glad things are going well!",
                "Awesome!"
            ],
            r'\b(bad|sad|terrible|awful)\b': [
                "I'm sorry to hear that. I hope things get better!",
                "That's unfortunate. Is there anything I can help with?",
                "Sorry you're having a tough time."
            ],
            r'\b(joke|funny)\b': [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What do you call a bear with no teeth? A gummy bear!",
                "Why did the scarecrow win an award? He was outstanding in his field!"
            ],
            r'\b(age|old)\b': [
                "I'm timeless! I exist only when you run this program.",
                "Age is just a number, and for a bot, it's always zero!",
                "I was just created, so I'm brand new!"
            ],
        }
        
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I see. Can you elaborate on that?",
            "Hmm, I'm not sure I understand completely, but I'm listening!",
            "That's a good point!",
            "I'm a simple chatbot, so I might not understand everything, but I'm here to chat!",
            "Interesting! What else would you like to talk about?",
        ]
    
    def get_response(self, user_input):
        """
        Generate a response based on the user's input.
        
        Args:
            user_input (str): The user's message
            
        Returns:
            str: The chatbot's response
        """
        user_input = user_input.lower().strip()
        
        # Check if the input matches any patterns
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        # If no pattern matches, return a default response
        return random.choice(self.default_responses)
    
    def chat(self):
        """Start an interactive chat session with the user."""
        print(f"\n{self.name}: Hello! I'm a simple conversational chatbot.")
        print(f"{self.name}: Type 'quit' or 'exit' to end the conversation.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit']:
                    print(f"\n{self.name}: Goodbye! Thanks for chatting with me!\n")
                    break
                
                response = self.get_response(user_input)
                print(f"{self.name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! Thanks for chatting with me!\n")
                break
            except EOFError:
                print(f"\n\n{self.name}: Goodbye! Thanks for chatting with me!\n")
                break


def main():
    """Main function to run the chatbot."""
    chatbot = SimpleChatbot(name="ChatBot")
    chatbot.chat()


if __name__ == "__main__":
    main()
