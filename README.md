# **Prompt Engineering with Groq API**

This project implements various **prompt engineering techniques** using the **Groq API**. It includes functionalities for **text completion, structured responses, classification with confidence analysis, and prompt strategy comparison**.

## **Features**
- **Basic Completion**: Generates responses to user prompts with proper API handling.  
- **Structured Completion**: Formats responses in a structured way and extracts relevant sections.  
- **Streaming Response Handling**: Streams responses and stops at a specific marker.  
- **Classification with Confidence Analysis**: Classifies text into categories and calculates model confidence.  
- **Prompt Strategy Comparison**: Tests different prompting methods and compares their effectiveness.  

## **Setup & Installation**
1. **Clone the repository**  
   ```bash
   git clone [https://github.com/yourusername/prompt-engineering-groq](https://github.com/Shaarawy25/Structured-Prompt-Engineering-and-Comparison-with-GROQ).git
   cd prompt-engineering-groq
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**  
   - Create a `.env` file in the project directory.  
   - Add your Groq API key:  
     ```
     GROQ_API_KEY=your_api_key_here
     ```

## **Usage**
- Run `llm_test.py` to test the implementation.  
- Modify `taming_llm.py` to experiment with different models and configurations.

## **Testing**
Run all tests using:
```bash
python llm_test.py
```

## **License**
This project is open-source under the **MIT License**.

