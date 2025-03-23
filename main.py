import argparse
from agent_v1.agent import DataAnalysisAgent
from agent_v1.models import UserRequest

def main():
    """Main entry point for the data analysis agent."""
    
    # Create agent
    agent = DataAnalysisAgent()
    
    while True:
        # Get user input
        print("\n=== Data Analysis Agent ===")
        query = input("What would you like to analyze? (type 'exit' to quit): ")
        
        if query.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get data path if provided
        data_path = input("Enter path to data file (leave empty if not applicable): ")
        data_path = data_path if data_path else None
        
        # Create request
        request = UserRequest(
            query=query,
            data_path=data_path
        )
        
        # Process request
        print("\nAnalyzing...")
        result = agent.process_request(request)
        
        # Display result
        print("\n=== Analysis Result ===")
        print(result)

if __name__ == "__main__":
    main()