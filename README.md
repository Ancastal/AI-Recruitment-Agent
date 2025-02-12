
A multi-agent recruitment assistant that leverages Microsoft AutoGen framework to streamline hiring processes. The system employs specialized AI agents working in concert to automate resume screening, candidate evaluation, and interview preparation.

## Overview

This application uses multiple AI agents to automate different aspects of the recruitment process:
- Screening resumes against job descriptions
- Extracting and managing candidate data
- Generating relevant interview questions based on identified skill gaps

## Features

- **Automated Resume Screening**: Analyzes resumes (PDF format) against job descriptions using keyword matching and AI evaluation
- **Smart Data Extraction**: Automatically extracts candidate information including name, email, and phone number
- **Interview Question Generation**: Creates targeted interview questions based on identified skill gaps
- **Data Management**: Saves candidate information and screening results to a structured CSV database
- **Multi-Agent System**:
    - Screening Agent: Evaluates resumes against job descriptions using keyword matching
    - Interview Agent: Generates interview questions based on identified skill gaps
    - Data Management Agent: Saves candidate information and screening results to a structured CSV database
    - User Proxy Agent: Manages the overall flow of the application
    
## Technical Stack

- Python 3.x
- AutoGen framework for multi-agent AI interactions
- GPT-4o-mini for natural language processing
- spaCy for text processing
- PDF handling: pdfplumber
- DOCX handling: docx2txt

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-recruitment-assistant.git
cd ai-recruitment-assistant
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

2. Create a `.env` file in the root directory with your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key
```

## Usage

1. Place the candidate's resume in PDF format in the `assets/CV-English.pdf` file
2. Add the job description in the `assets/job_description.txt` file
3. Run the application:

```bash
python app.py
```

The application will:
1. Screen the resume against the job description
2. Extract and save candidate information
3. Use keyword matching for the initial screening
4. Generate relevant interview questions, based on the identified skill gaps
5. Output results to console and save to CSV `(assets/candidate_data.csv)`

![image](https://github.com/user-attachments/assets/b5bed411-c34a-4e14-8c26-5e4a4906e50e)

## Project Structure

- `app.py`: Main application file
- `assets/`: Directory for input files (resume, job description)
- `config/`: Configuration files for agents
- `utils/`: Utility functions

## Acknowledgments

- Built with [AutoGen](https://github.com/microsoft/autogen)
- Uses OpenAI's GPT-4o-mini for agent orchestration, text generation and function calling.
