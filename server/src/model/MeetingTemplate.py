from typing import List

class MeetingTemplate:
    """Template for meeting outcomes"""

    def __init__(self, org_name: str, outcomes: List[str], glossary: List[str]):
        self.org_name = org_name
        self.outcomes = outcomes
        self.glossary = glossary

    def generate_prompt(self, additional_information: str=None) -> str:
        outcomes_str = '\n'.join(self.outcomes)
        glossary_terms_str = '\n'.join(self.glossary)
        return f"""
You will be provided with a meeting transcript, and your task is to answer the following:
{outcomes_str}
Here are some company specific definitions:
{glossary_terms_str}
{additional_information}
        """