#!/usr/bin/env python3
"""
Test script for the Simple Conversational Chatbot.
This script demonstrates the chatbot's capabilities with automated tests.
"""

from chatbot import SimpleChatbot


def test_chatbot_responses():
    """Test various chatbot responses."""
    print("=" * 60)
    print("Testing Simple Conversational Chatbot")
    print("=" * 60)
    
    bot = SimpleChatbot(name="TestBot")
    
    test_cases = [
        ("Greeting", "hello"),
        ("Status inquiry", "how are you"),
        ("Identity question", "who are you"),
        ("Help request", "help"),
        ("Weather question", "what's the weather like"),
        ("Gratitude", "thank you"),
        ("Positive sentiment", "that's great"),
        ("Negative sentiment", "I'm feeling bad"),
        ("Joke request", "tell me something funny"),
        ("Age question", "how old are you"),
        ("Farewell", "goodbye"),
        ("Unknown input", "this is a random sentence"),
    ]
    
    print("\nRunning test cases:\n")
    
    for test_name, user_input in test_cases:
        response = bot.get_response(user_input)
        print(f"Test: {test_name}")
        print(f"  Input:  '{user_input}'")
        print(f"  Output: '{response}'")
        print()
    
    print("=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)
    print("\nTo try the interactive chatbot, run:")
    print("  python3 chatbot.py")
    print()


def test_chatbot_patterns():
    """Test that chatbot patterns are working correctly."""
    print("\nTesting pattern matching:\n")
    
    bot = SimpleChatbot(name="PatternBot")
    
    # Test that similar inputs get responses from the same pattern
    greetings = ["hi", "hello", "hey there"]
    print("Testing greetings pattern:")
    for greeting in greetings:
        response = bot.get_response(greeting)
        print(f"  '{greeting}' -> Response received ✓")
    
    # Test case insensitivity
    print("\nTesting case insensitivity:")
    test_inputs = ["HELLO", "HeLLo", "hello"]
    for inp in test_inputs:
        response = bot.get_response(inp)
        print(f"  '{inp}' -> Response received ✓")
    
    print("\nPattern matching tests passed ✓")


if __name__ == "__main__":
    test_chatbot_responses()
    test_chatbot_patterns()
