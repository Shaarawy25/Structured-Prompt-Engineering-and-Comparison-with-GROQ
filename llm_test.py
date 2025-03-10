from taming_llm import *

# Part 1: Normal Completion testing
"""
client = LLMClient()
prompt = "Explain the significance of Newton's laws in physics."
response = client.complete(prompt)
print("Completion Response:\n", response)
"""

# Part 2: Structured Completion and Section Extraction
"""
client = LLMClient()
text = "Machine learning is a field of artificial intelligence focused on building systems that learn from data."
question = "What are the main applications of machine learning?"
structured_prompt = create_structured_prompt(text, question)

completion = client.complete(structured_prompt)
analysis = extract_section(completion, "## Analysis", None)
print("Extracted Analysis:\n", analysis)
"""

#Part 3: Streaming Completion with Stop Marker
"""
client = LLMClient()
prompt = "Summarize the history of the Internet. End your response with 'END'."
stop_marker = "END"
response = stream_until_marker(client, prompt, stop_marker)
print("Streamed Response:\n", response)
"""
#Part 4:  Classification with Confidence Analysis
"""
client = LLMClient()
categories = ["Positive", "Negative", "Neutral"]
text = "The product quality is terrible, and customer service was not helpful."
result = classify_with_confidence(client, text, categories)

print("Classification Result:\n", result)
"""
#Part 5: Prompt Strategy Comparison
"""
client = LLMClient()
texts = [
    "I absolutely love this product! It works perfectly.",
    "The battery life is too short, I'm disappointed.",
    "It's okay, but I expected better performance."
]
categories = ["Positive", "Negative", "Neutral"]

results = compare_prompt_strategies(client, texts, categories)
for strategy, outputs in results.items():
    print(f"Strategy: {strategy}")
    for i, res in enumerate(outputs):
        print(f"  Text: {texts[i]}")
        print(f"  Category: {res['category']}, Confidence: {res['confidence']}")
"""
