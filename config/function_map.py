from tools.parser import extract_text_from_pdf, extract_text_from_docx, read_text_from_file
from tools.keyword_matcher import match_keywords
from tools.save_data import save_candidate_data

from autogen import register_function

def register_functions(agents):
    """
    Register functions for different agents using a mapping approach.
    agents: dict containing agent instances with keys 'screening_assistant', 'data_manager', 'user_proxy'
    """
    # Define function mappings for each agent
    function_map = {
        'screening_assistant': [
            {
                'function': extract_text_from_pdf,
                'description': "Extract text from a PDF resume.",
                'name': "extract_text_from_pdf"
            },
            {
                'function': read_text_from_file,
                'description': "Read text from a file.",
                'name': "read_text_from_file"
            },
        ],
        'data_manager': [
            {
                'function': extract_text_from_pdf,
                'description': "Extract text from a PDF resume.",
                'name': "extract_text_from_pdf_data_manager"
            },
            {
                'function': save_candidate_data,
                'description': "Save candidate data to CSV file.",
                'name': "save_candidate_data"
            },
            {
                'function': match_keywords,
                'description': "Match keywords in a text.",
                'name': "match_keywords"
            }
        ]
    }

    # Register functions for each agent
    for agent_name, functions in function_map.items():
        for func_info in functions:
            register_function(
                func_info['function'],
                caller=agents[agent_name],
                executor=agents['user_proxy'],
                description=func_info['description'],
                name=func_info['name']
            ) 