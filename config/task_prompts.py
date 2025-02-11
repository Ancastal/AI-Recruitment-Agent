class TaskPrompts:
    @staticmethod
    def get_screening_task():
        return """
        Evaluate whether the candidate has the skills and experience for the job. The resume is in the file assets/CV-English.pdf and the job description is in the file assets/job_description.txt.
        Use the match_keywords function to find matching keywords in the resume to the job description.
        """

    @staticmethod
    def get_data_task(screening_result):
        return f"""
        First, use extract_text_from_pdf function to read the resume from assets/CV-English.pdf.
        Then, from the extracted text, find the candidate's name and email address.

        From the screening results below, extract the matching keywords and decision:

        {screening_result.summary}

        Once you have all the information, use the save_candidate_data function with the following parameters:
        - candidate_name: The full name from the resume
        - email: The email address from the resume
        - phone number: The phone number from the resume
        - matching_keywords: The keywords that matched from the screening results
        - screening_result: The final decision (HIRE or PASS) from the screening results

        Make sure to extract and pass all required information correctly.
        """

    @staticmethod
    def get_interview_task(screening_result):
        return f"""
        Based on the previous screening conversation below, generate follow-up interview questions focusing on any identified skill gaps:

        {screening_result.summary}

        Generate 5 specific interview questions that will help assess the candidate's abilities in the areas where their resume showed potential gaps.
        """ 