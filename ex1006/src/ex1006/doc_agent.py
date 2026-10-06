from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
# print(result["messages"][-1].content_blocks)
# (ex1006) D:\han_skc1001\agent\ex1006>uv run src\ex1006\doc_agent.py       
# [{'type': 'text', 'text': "It's currently sunny in San Francisco."}]

print(result)

# (ex1006) D:\han_skc1001\agent\ex1006>uv run src\ex1006\doc_agent.py
# {'messages': [HumanMessage(content="What's the weather in San Francisco?", additional_kwargs={}, response_metadata={}, id='4257fc02-29c0-4aa8-9a3d-642f53529fa8'), AIMessage(content='', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 141, 'total_tokens': 159, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0, 'text_tokens': None}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0, 'image_tokens': None, 'text_tokens': None}}, 'model_provider': 'openai', 'model_name': 'gpt-5.5-2026-04-23', 'system_fingerprint': None, 'id': 'chatcmpl-EVoHc6pQqdDhp0T4ypgubjNGvxpaD', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--01a10ed4-687b-7100-8daa-4a317d4732bf-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'San Francisco'}, 'id': 'call_nkXmPw5WNHO2iCJf7hrfYaGP', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 141, 'output_tokens': 18, 'total_tokens': 159, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(content="It's always sunny in San Francisco!", name='get_weather', id='07385226-06e0-4254-851a-820fbd7ea1e9', tool_call_id='call_nkXmPw5WNHO2iCJf7hrfYaGP'), AIMessage(content='It’s currently sunny in San Francisco.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 11, 'prompt_tokens': 177, 'total_tokens': 188, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0, 'text_tokens': None}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0, 'image_tokens': None, 'text_tokens': None}}, 'model_provider': 'openai', 'model_name': 'gpt-5.5-2026-04-23', 'system_fingerprint': None, 'id': 'chatcmpl-EVoHdJSgK8BukmcUMYksXr3S89cnl', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--01a10ed4-6d46-70a3-9ea3-01d470763d37-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 177, 'output_tokens': 11, 'total_tokens': 188, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}
