from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

config_list = [
    {
        "model":"deepseek-ai_deepseek-coder-6.7b-instruct",
        "base_url": "http://localhost:1234/v1",
        "api_key":"NULL"
    }
]

llm_config={
    "timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = AssistantAgent(
    name="Assistant",
    llm_config=llm_config,
    system_message="You are a coder specializing in Python."
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task1 = """
Write python code to convert an input in roman numerals to decimal output.
"""

user_proxy.initiate_chat(
    assistant,
    message=task1
)
