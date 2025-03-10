import os
import time
from dotenv import load_dotenv
import groq

class LLMClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = groq.Client(api_key=self.api_key)
        self.model = "llama3-70b-8192"
    
    def complete(self, prompt, max_tokens=1000, temperature=0.6):
        """Handles completion requests with error handling and retries."""
        retries = 3
        for _ in range(retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=max_tokens,
                    temperature=temperature
                )
                return response.choices[0].message.content
            except groq.errors.RateLimitError:
                print("Rate limit exceeded. Retrying...")
                time.sleep(2)
            except Exception as e:
                print(f"Error: {e}")
        return None

# Structured Completion

def create_structured_prompt(text, question):
    return f"""
    # Analysis Report
    ## Input Text
    {text}
    ## Question
    {question}
    ## Analysis
    """

def extract_section(completion, section_start, section_end=None):
    start_idx = completion.find(section_start)
    if start_idx == -1:
        return None
    start_idx += len(section_start)
    if section_end is None:
        return completion[start_idx:].strip()
    end_idx = completion.find(section_end, start_idx)
    return completion[start_idx:end_idx].strip() if end_idx != -1 else completion[start_idx:].strip()

def stream_until_marker(client, prompt, stop_marker, max_tokens=1000):
    """Streams a completion and stops at a given marker."""
    response = ""
    for chunk in client.client.chat.completions.create(
        model=client.model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        stream=True
    ):
        response += chunk.choices[0].delta.content
        if stop_marker in response:
            break
    return response.split(stop_marker)[0]

# Classification with Confidence Analysis

def classify_with_confidence(client, text, categories, confidence_threshold=0.8):
    prompt = f"""
    Classify the following text into exactly one of these categories: {', '.join(categories)}.
    Response format:
    1. CATEGORY: [one of {', '.join(categories)}]
    2. CONFIDENCE: [high|medium|low]
    3. REASONING: [explanation]
    Text to classify:
    {text}
    """
    response = client.complete(prompt, max_tokens=500, temperature=0)
    if not response:
        return {"category": "error", "confidence": 0, "reasoning": "API failure"}
    
    category = extract_section(response, "1. CATEGORY: ", "\n")
    confidence_str = extract_section(response, "2. CONFIDENCE: ", "\n")
    reasoning = extract_section(response, "3. REASONING: ")
    
    confidence_mapping = {"high": 1.0, "medium": 0.7, "low": 0.4}
    confidence_score = confidence_mapping.get(confidence_str.lower(), 0.0)
    
    if confidence_score >= confidence_threshold:
        return {"category": category, "confidence": confidence_score, "reasoning": reasoning}
    return {"category": "uncertain", "confidence": confidence_score, "reasoning": "Confidence below threshold"}

# Prompt Strategy Comparison

def compare_prompt_strategies(client, texts, categories):
    strategies = {
        "basic": lambda text: f"Classify this text: {text}",
        "structured": lambda text: f"""
        Classification Task
        Categories: {', '.join(categories)}
        Text: {text}
        Classification:
        """,
        "few_shot": lambda text: f"""
        Here are examples:
        Text: "The product was damaged."
        Classification: Negative
        Text: "Service was excellent."
        Classification: Positive
        Now classify this text: {text}
        """
    }
    results = {}
    for strategy_name, prompt_func in strategies.items():
        strategy_results = []
        for text in texts:
            prompt = prompt_func(text)
            result = classify_with_confidence(client, text, categories)
            strategy_results.append(result)
        results[strategy_name] = strategy_results
    return results
