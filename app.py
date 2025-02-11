from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

import csv
import os

from config.function_map import register_functions

from config.agent_config import (
    SCREENING_ASSISTANT_MESSAGE,
    INTERVIEW_ASSISTANT_MESSAGE,
    DATA_MANAGER_MESSAGE,
)

load_dotenv()

screening_assistant = AssistantAgent(
    name="Screening Assistant",
    llm_config={
        "model": "gpt-4o-mini",
    },
    system_message=SCREENING_ASSISTANT_MESSAGE,
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
    max_consecutive_auto_reply=6,
    silent=True
)

interview_assistant = AssistantAgent(
    name="Interview Assistant",
    llm_config={
        "model": "gpt-4o-mini",
    },
    system_message=INTERVIEW_ASSISTANT_MESSAGE,
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
    max_consecutive_auto_reply=3,
    silent=True
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    max_consecutive_auto_reply=10,
    code_execution_config={
        "work_dir": "work_dir",
        "use_docker": False,
    },
    silent=True
)

data_manager = AssistantAgent(
    name="Data Manager",
    llm_config={
        "model": "gpt-4o-mini",
    },
    system_message=DATA_MANAGER_MESSAGE,
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
    max_consecutive_auto_reply=3,
    silent=True
)

# First task: Screen the candidate
screening_task = """
Evaluate whether the candidate has the skills and experience for the job. The resume is in the file assets/CV-English.pdf and the job description is in the file assets/job_description.txt.
Use the match_keywords function to find matching keywords in the resume to the job description.
"""

# Remove all register_function calls and replace with:
agents = {
    'screening_assistant': screening_assistant,
    'data_manager': data_manager,
    'user_proxy': user_proxy
}

register_functions(agents)
# Execute first task: Screen the candidate
screening_result = user_proxy.initiate_chat(
    screening_assistant,
    message=screening_task,
    max_turns=10
)

# Save the candidate data
data_task = f"""
First, use extract_text_from_pdf function to read the resume from assets/CV-English.pdf.
Then, from the extracted text, find the candidate's name and email address.

From the screening results below, extract the matching keywords using the match_keywords function and thedecision:

{screening_result.summary}

Once you have all the information, use the save_candidate_data function with the following parameters:
- candidate_name: The full name from the resume
- email: The email address from the resume
- phone number: The phone number from the resume
- matching_keywords: The keywords that matched from the screening results
- screening_result: The final decision (HIRE or PASS) from the screening results

Make sure to extract and pass all required information correctly.
"""

data_result = user_proxy.initiate_chat(
    data_manager,
    message=data_task,
    max_turns=5
)

# Execute second task: Generate interview questions
interview_task = f"""
Based on the previous screening conversation below, generate follow-up interview questions focusing on any identified skill gaps:

{screening_result.summary}

Generate 5 specific interview questions that will help assess the candidate's abilities in the areas where their resume showed potential gaps.
"""

interview_result = user_proxy.initiate_chat(
    interview_assistant,
    message=interview_task,
    max_turns=5,
)

print("Screening Results:")
print(screening_result.summary)
print("\nData Management Results:")
print(data_result.summary)
print("\nRecommended Questions:")
print(interview_result.summary)