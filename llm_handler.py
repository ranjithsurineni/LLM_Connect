import openai
import requests
import streamlit as st

def get_available_models(provider):
    if provider == 'OpenAI':
        # Updated with more current OpenAI models
        return [
            'gpt-3.5-turbo',
            'gpt-3.5-turbo-16k',
            'gpt-4',
            'gpt-4-32k',
            'gpt-4-turbo',
            'gpt-4o'  # Latest OpenAI flagship model
        ]
    elif provider == 'OpenRouter':
        # Example: Add popular OpenRouter models (update as needed)
        return [
            'openai/gpt-3.5-turbo',
            'openai/gpt-4',
            'meta-llama/llama-3-70b-instruct',
            'google/gemini-pro',
            'anthropic/claude-2',
            'anthropic/claude-3-5-sonnet',
            'mistralai/mistral-small-3.2-24b-instruct:free',
            'mistralai/mistral-7b-instruct:free',
            'mistralai/mistral-large-2407:free',
            'google/gemma-7b-it:free',
            'tiiuae/falcon-40b-instruct:free',
            'minimax/minimax-m1:extended',
            'deepseek/deepseek-r1-0528-qwen3-8b:free',
            'deepseek/deepseek-r1-0528:free',
            'sarvamai/sarvam-m:free',
            'mistralai/mistral-7b-instruct',
            'mistralai/mistral-large-2407',
            'google/gemma-7b-it',
            'tiiuae/falcon-40b-instruct',
            'xenova/llama-2-13b-chat-hf',
            'xenova/llama-2-70b-chat-hf',
            'xenova/llama-3-8b-instruct',
            'xenova/llama-3-70b-instruct',
            'xenova/llama-3-8b-chat',
            'xenova/llama-3-70b-chat',
            'xenova/llama-3-8b-chat-hf',
            'green-llama/llama-3-8b-chat-hf'
            

        ]
    elif provider == 'HuggingFace':
        # Example: Add popular HuggingFace models (update as needed)
        return [
            'meta-llama/Llama-2-70b-chat-hf',
            'mistralai/Mistral-7B-Instruct-v0.2',
            'google/gemma-7b-it',
            'tiiuae/falcon-40b-instruct',
            #hugging face free models
            'xenova/llama-2-13b-chat-hf',
            'xenova/llama-2-70b-chat-hf',
            'xenova/llama-3-8b-instruct',
            'sarvamai/sarvam-m:free',
            'mistralai/mistral-7b-instruct:free',
            'mistralai/mistral-large-2407:free',
            'google/gemma-7b-it:free',
            'Menlo/Jan-nano',
            'Menlo/Jan-1.5b',
            
        ]
    return ['default-model']  # Fallback/default


def generate_response(api_key, model, prompt, provider, base_url=None):
    if provider == 'OpenAI':
        openai.api_key = api_key
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"❌ Error: {e}"

    elif provider == 'OpenRouter':
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(base_url, headers=headers, json=payload)
            result = response.json()
            # Debug print
            print(result)
            # Try to extract the response in a more robust way
            if "choices" in result and result["choices"]:
                return result["choices"][0]["message"]["content"]
            elif "message" in result:
                return result["message"]
            elif "error" in result:
                return f"❌ OpenRouter API Error: {result['error']}"
            else:
                return f"❌ Unexpected OpenRouter response: {result}"
        except Exception as e:
            return f"❌ OpenRouter Error: {e}"

    elif provider == 'HuggingFace':
        try:
            headers = {
                "Authorization": f"Bearer {api_key}"
            }
            response = requests.post(
                f"{base_url}{model}",
                headers=headers,
                json={"inputs": prompt}
            )
            result = response.json()
            return result[0]['generated_text'] if isinstance(result, list) else str(result)
        except Exception as e:
            return f"❌ HuggingFace Error: {e}"

    return "❌ Unsupported provider"

