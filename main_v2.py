import argparse
from agent_v2.smart_agent import AIDataScientist

def main():
    """Main entry point for the AI Data Scientist."""
    
    # Create AI Data Scientist
    ai_scientist = AIDataScientist()
    
    print("\n==============================")
    print("AI Data Scientist")
    print("==============================\n")
    print("Ask me to analyze your data, and I'll write and execute code for you!")
    
    # Main interaction loop
    while True:
        # Get user input
        query = input("\nWhat would you like to analyze? (type 'exit' to quit): ")
        
        if query.lower() == 'exit':
            print("\nThank you for using AI Data Scientist. Goodbye!")
            break
        
        # Get data path if provided
        data_path = input("Enter path to data file (leave empty if using previous file): ")
        data_path = data_path if data_path else None
        
        print("\nThinking and analyzing...")
        # Process request
        result = ai_scientist.analyze(query, data_path)
        
        # Check for errors
        if "error" in result:
            print(f"Error: {result['error']}")
            continue
        
        # Display results
        print("\n==============================")
        print("ANALYSIS REPORT")
        print("==============================\n")
        
        print("INTERPRETATION:")
        print(result["interpretation"])
        
        # Display any plots (if running in notebook or web interface)
        if "results" in result and "plots" in result["results"]:
            plots = result["results"]["plots"]
            if plots:
                print(f"\nGenerated {len(plots)} visualization(s)")
                # In a real environment, you would display these plots
                # For console, we just mention they exist
        
        print("\nWould you like to see the generated code? (yes/no): ")
        if input().lower().startswith('y'):
            print("\n==============================")
            print("GENERATED CODE")
            print("==============================\n")
            print(result["code"])

if __name__ == "__main__":
    main()