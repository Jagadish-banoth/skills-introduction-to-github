#!/usr/bin/env python3
"""
Example usage demonstrations for the Simple Conversational Chatbot.
This script shows different ways to use the chatbot.
"""

from chatbot import SimpleChatbot


def example_1_basic_usage():
    """Example 1: Basic usage - Single responses"""
    print("=" * 60)
    print("Example 1: Getting Single Responses")
    print("=" * 60)
    
    bot = SimpleChatbot(name="Helper")
    
    # Get individual responses
    print(f"\nUser: Hello!")
    print(f"Bot: {bot.get_response('Hello!')}")
    
    print(f"\nUser: What can you do?")
    print(f"Bot: {bot.get_response('What can you do?')}")
    
    print(f"\nUser: Tell me a joke")
    print(f"Bot: {bot.get_response('Tell me a joke')}")
    
    print()


def example_2_custom_bot():
    """Example 2: Creating a custom named bot"""
    print("=" * 60)
    print("Example 2: Custom Named Bot")
    print("=" * 60)
    
    # Create a bot with a custom name
    custom_bot = SimpleChatbot(name="Buddy")
    
    print(f"\nUser: Who are you?")
    print(f"Bot: {custom_bot.get_response('Who are you?')}")
    
    print()


def example_3_conversation_flow():
    """Example 3: Simulating a conversation flow"""
    print("=" * 60)
    print("Example 3: Conversation Flow Simulation")
    print("=" * 60)
    
    bot = SimpleChatbot(name="ConvoBot")
    
    conversation = [
        "Hi there!",
        "How are you doing today?",
        "That's great to hear!",
        "Can you tell me a joke?",
        "Haha, that's funny!",
        "Thanks for chatting!",
        "Goodbye!"
    ]
    
    print("\nSimulated conversation:\n")
    for message in conversation:
        response = bot.get_response(message)
        print(f"User: {message}")
        print(f"Bot:  {response}")
        print()


def example_4_pattern_testing():
    """Example 4: Testing different patterns"""
    print("=" * 60)
    print("Example 4: Testing Various Patterns")
    print("=" * 60)
    
    bot = SimpleChatbot(name="PatternBot")
    
    patterns_to_test = {
        "Greetings": ["hi", "hello", "hey"],
        "Questions": ["who are you", "what is your name", "how are you"],
        "Requests": ["help", "tell me a joke", "what can you do"],
        "Sentiments": ["that's good", "I'm sad", "awesome"],
        "Farewells": ["bye", "goodbye", "see you later"]
    }
    
    for category, messages in patterns_to_test.items():
        print(f"\n{category}:")
        for msg in messages:
            response = bot.get_response(msg)
            print(f"  '{msg}' -> '{response}'")


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("Simple Conversational Chatbot - Usage Examples")
    print("=" * 60 + "\n")
    
    example_1_basic_usage()
    example_2_custom_bot()
    example_3_conversation_flow()
    example_4_pattern_testing()
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
    print("\nTo start an interactive chat session, run:")
    print("  python3 chatbot.py")
    print("\nTo run tests, use:")
    print("  python3 test_chatbot.py")
    print()


if __name__ == "__main__":
    main()
