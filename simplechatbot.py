import re
from datetime import datetime

class SimpleChatbot:
    def __init__(self):
        self.chat_history = []
        
        # Knowledge Base (Domain-Specific)
        self.knowledge_base = {
            "ai": "Artificial Intelligence is the simulation of human intelligence in machines.",
            "machine learning": "Machine Learning is a subset of AI that enables systems to learn from data.",
            "deep learning": "Deep Learning is a subset of ML using neural networks with many layers.",
            "python": "Python is a popular programming language used in AI and web development.",
            "internship": "An internship is a short-term work experience opportunity for students."
        }

    # Log conversation
    def log_conversation(self, user_input, bot_response):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.chat_history.append(f"[{timestamp}] You: {user_input}")
        self.chat_history.append(f"[{timestamp}] Bot: {bot_response}")

    # Intent Matching
    def get_response(self, user_input):
        user_input = user_input.lower()

        # Greeting Intent
        if re.search(r"\b(hi|hello|hey)\b", user_input):
            return "Hello! How can I help you today?"

        # Help Intent
        elif "help" in user_input:
            return "I can answer questions about AI, ML, Python, internships, or just chat with you!"

        # Small Talk Intent
        elif "how are you" in user_input:
            return "I'm just a bot, but I'm doing great! 😊"

        elif "your name" in user_input:
            return "I am a Simple Rule-Based Chatbot."

        # Exit
        elif user_input in ["bye", "exit", "quit"]:
            return "Goodbye! Have a great day!"

        # Knowledge Base Matching
        else:
            for key in self.knowledge_base:
                if key in user_input:
                    return self.knowledge_base[key]

        # Default Response
        return "Sorry, I don't understand that. Type 'help' to see what I can do."

    # Run chatbot
    def run(self):
        print("🤖 Simple Rule-Based Chatbot")
        print("Type 'exit' to quit.\n")

        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)
            print("Bot:", response)

            self.log_conversation(user_input, response)

            if user_input.lower() in ["bye", "exit", "quit"]:
                break

        self.save_chat_history()

    # Save chat history to file
    def save_chat_history(self):
        with open("chat_history.txt", "w") as file:
            for line in self.chat_history:
                file.write(line + "\n")
        print("\nConversation saved to chat_history.txt")

# Run the chatbot
if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.run()