#! python3
# madlibs.py - Mad Libs program that reads in text files and lets users 
# add input anywhere any of the madlib words show up in the text

import os
from pathlib import Path
import re
import pyinputplus as pyip
from datetime import datetime

# Example madlib
text = 'The ADJECTIVE ANIMAL PAST-TENSE-VERB into the ADJECTIVE bar, and PAST-TENSE-VERB a(n) NOUN.'

path_prompt = 'Please input in the path where your madlibs are located:\n'
team_num_prompt = 'Please input the number of teams:\n'

# Asks users which path the matlibs are in
path = pyip.inputFilepath(path_prompt)

os.chdir(path)

# C:\Users\Cleme\Practice_Code\Automate_The_Boring_Stuff\ATBS_side_projects

# Prompts user for the number of teams competing
num_of_teams = pyip.inputInt(team_num_prompt)

# TODO: Write several madlibs based on different themes or different stories
# Bonus: Write one madlib in Japanese!

# Loop through the whole madlib game for each team
for team in range(num_of_teams):
        
    # Madlib themes that will correlate to a text file of the same name
    madlib_themes = [
        'Summer',
        'Halloween',
        'Food',
        'Madlibs',

    ]

    def choosing_madlib_theme(themes):

        # Theme prompt for input menu
        theme_prompt = 'Please choose from one of the following madlib themes:\n'

        # Asks user which madlib theme they want to use
        theme = pyip.inputMenu(madlib_themes, theme_prompt)

        # Text file to be opened (should this be hard coded in or generated based off of the themes)
        filename = theme.lower() + '.txt'

        # Tries to open the file correlating to the theme and recalls the function
        # recursively if there is no file
        try: 
            with open(filename, 'r', encoding="latin-1") as madlibs: 
                read_madlibs = madlibs.read()
            return read_madlibs

        except FileNotFoundError:
            print('Sorry that theme is not available, please pick a different one.\n')
            return choosing_madlib_theme(madlib_themes)

    madlibs_text = choosing_madlib_theme(madlib_themes)

    def madlib_generator(text_file):

        # Define words that would be used in madlibs
        madlib_words = [
            'ADJECTIVE',
            'NAME',
            "CELEBRITY",
            # The same matching problem with verbs is going to occur with 
            # nouns and plural nouns
            'PLURAL NOUN',
            'NOUN',
            'FOOD',
            'ADVERB',
            'PAST-TENSE-VERB',
            '-ING-VERB',
            # Verb still matches to the Past Tense Verbs
            # When spaces are used to specify the verb match then the spaces are 
            # matched and there are not spaces when printed
            'PRESENT-TENSE-VERB',
            'ANIMAL',
            'EXCLAMATION',
            'SILLY WORD',
            'LOCATION',
            'CITY',
            'DAY OF THE WEEK',
            'TIME',
            'NUMBER',
            'BODY PART (PLURAL)'
            'BODY PART',

                ]

        vowels = (
            'A', 'I', 'E', 'O', 'U'
                )

        # Create a dictionary that has the regex as keys and the matches as values
        regex_matches = {}
        sub_text = text_file
        for word in madlib_words:
            regex = re.compile(word)
            regex_matches[regex] = regex.findall(sub_text)
        # Loop through the dictionary so that the user can input their values for the madlib words
        for regex, matches in regex_matches.items():
            # Skips the word if there are no matches
            if len(matches) == 0:
                continue
            # Loops through each match in range of the total matches for each madlib word
            for match in range(len(matches)):
                # 'a' for words that start with a consonant 
                # 'an for words that start with a vowel
                vowel_prompt = f'Enter an {(matches[match].lower().strip())}:\n'
                non_vowel_prompt = f'Enter a {(matches[match].lower().strip())}:\n'
                # Vowel and non-vowel logic
                if matches[match].startswith(vowels, 0, 2):
                    matches[match] = input(vowel_prompt)
                    sub_text = regex.sub(matches[match], sub_text, count=1)
                else:
                    matches[match] = input(non_vowel_prompt)
                    sub_text = regex.sub(matches[match], sub_text, count=1)
        
        try:
            # If the file already exists (i.e. If it's not the first team) 
            # open the file in append mode to add text
            with open('finished_madlib.txt', 'a') as madlib:
                # Adds time and date if it's the first team for organizational purposes
                if team == 0:
                    madlib.write('\n')
                    current_time = datetime.now().isoformat(timespec='seconds')
                    madlib.write(f"Date and Time: {current_time}\n")
                madlib.write(f"Team {team + 1}'s madlib:\n")
                for line in sub_text:
                    madlib.write(line)
                madlib.write('\n')
            return print(sub_text)  

        except FileNotFoundError:
            with open('finished_madlib.txt', 'w') as madlib: 
                current_time = datetime.now.isoformat(timespec='minutes')
                madlib.write(f"Date and Time: {current_time}\n")
                madlib.write(f"Team {team + 1}'s madlib:\n")
                for line in sub_text:
                    madlib.write(line)
                madlib.write('\n')
            print('')
            return print(sub_text)   

    # Example madlib
    #madlib_generator(text)

    # Takes in text files and returns madlibs  
    madlib_generator(madlibs_text)
