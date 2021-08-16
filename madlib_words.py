madlib_dict = {
            'ADJECTIVE': 'ADJECTIVE',
            "FRIEND'S NAME": "FRIEND'S NAME",
            "NAME": r"(?<!FRIEND'S\s)NAME",
            "CELEBRITY": "CELEBRITY",
            'NOUN (PLURAL)': 'NOUN \(PLURAL\)',
            'NOUN': r'NOUN(?!\s[(])',
            'FOOD': 'FOOD',
            'ADVERB': 'ADVERB',
            'PAST TENSE VERB': 'PAST TENSE VERB',
            'VERB ENDING IN ING': 'VERB ENDING IN ING',
            'PRESENT TENSE VERB': 'PRESENT TENSE VERB',
            'ANIMAL': 'ANIMAL',
            'EXCLAMATION': 'EXCLAMATION',
            'SILLY WORD': 'SILLY WORD',
            'LOCATION': 'LOCATION',
            'CITY': 'CITY',
            'DAY OF THE WEEK': 'DAY OF THE WEEK',
            'TIME': 'TIME',
            'NUMBER': 'NUMBER',
            'BODY (PLURAL)': 'BODY PART \(PLURAL\)',
            'BODY PART': r'BODY PART(?!\s[(])',

}

madlib_words = list(madlib_dict.keys())
madlib_regex = list(madlib_dict.values())
