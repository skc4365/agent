from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "샌프란시스코 날씨는 어때?"}]}
)
# print(result["messages"][-1].content_blocks)
# (ex1006) D:\han_skc1001\agent\ex1006>uv run src\ex1006\doc_agent.py       
# [{'type': 'text', 'text': "It's currently sunny in San Francisco."}]

# print(result)
# (ex1006) D:\han_skc1001\agent\ex1006>uv run src\ex1006\doc_agent.py  
# {'messages': [HumanMessage(content='샌프란시스코 날씨는 어때?', additional_kwargs={}, response_metadata={}, id='892684b6-a9d1-4508-9ec9-582f4e39cdf2'), AIMessage(content='', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 147, 'total_tokens': 165, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0, 'text_tokens': None}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0, 'image_tokens': None, 'text_tokens': None}}, 'model_provider': 'openai', 'model_name': 'gpt-5.5-2026-04-23', 'system_fingerprint': None, 'id': 'chatcmpl-EVoSjWXMcE9uGM3E9wpJtmSWn0NlZ', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--01a10ede-ea82-7f12-9c7b-36cd36366b4b-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'San Francisco'}, 'id': 'call_pfJoEnPWzDZYxTZhiCazimss', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 147, 'output_tokens': 18, 'total_tokens': 165, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(content="It's always sunny in San Francisco!", name='get_weather', id='9ce92d92-8278-4473-b45f-5a2d29700dea', tool_call_id='call_pfJoEnPWzDZYxTZhiCazimss'), AIMessage(content='샌프란시스코 날씨는 맑습니다! ☀️', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 183, 'total_tokens': 203, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0, 'text_tokens': None}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0, 'image_tokens': None, 'text_tokens': None}}, 'model_provider': 'openai', 'model_name': 'gpt-5.5-2026-04-23', 'system_fingerprint': None, 'id': 'chatcmpl-EVoSkxW8AxJNpoAnr9qv8MoLmDG9w', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--01a10ede-ef71-7f81-b901-b4e7f42f9300-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 183, 'output_tokens': 20, 'total_tokens': 203, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}

print(result["messages"][-1].content)
# (ex1006) D:\han_skc1001\agent\ex1006>uv run src\ex1006\doc_agent.py
# 샌프란시스코는 현재 항상 맑은 날씨라고 합니다! ☀️