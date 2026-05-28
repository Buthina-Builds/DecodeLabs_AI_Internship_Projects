# Project 1: Rule-Based AI Chatbot
# Powered by DecodeLabs

def start_chatbot():
    print("==================================================")
    print("Welcome to DecodeLabs AI Chatbot! (Type 'exit' or 'bye' to quit)")
    print("==================================================")
    
    while True:
        # 1. Input Capture & Sanitization / Normalization
        user_input = input("You: ")
        clean_input = user_input.lower().strip() 
        # 2. Process (The Logic Skeleton - If/Else Guards)
        if clean_input in ['exit', 'bye', 'quit']:
            print("Chatbot: Goodbye! Good luck with your DecodeLabs internship! 🚀")
            break 
        elif clean_input in ['hello', 'hi', 'hey', 'greetings']:
            print("Chatbot: Hello! Step into the role of an Artificial Intelligence Engineer at DecodeLabs. How can I help you today?")
            
        elif 'project' in clean_input:
            print("Chatbot: In this training, you have Project 1 (Chatbot), Project 2 (Classification), and Project 3 (Recommendation Engine). Make sure to complete them all!")
            
        elif 'decodelabs' in clean_input:
            print("Chatbot: DecodeLabs is an advanced industrial training provider helping you build real-world AI engineering skills.")
            
        elif clean_input in ['how are you', 'status']:
            print("Chatbot: I am operating at 100% efficiency, tracking deterministic rules perfectly without hallucination risk!")
            
        elif 'help' in clean_input:
            print("Chatbot: Sure! You can ask me about 'DecodeLabs', 'projects', or type 'exit' to close the chat.")
            
        else:
           
            print("Chatbot: I understood your input, but it doesn't match my current predefined rules. Let's try another topic!")

if __name__ == "__main__":
    start_chatbot()