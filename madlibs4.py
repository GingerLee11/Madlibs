#! python3
# madlibs.py - Mad Libs program that reads in text files and then prints 
# a list of madlib words to an excel file for users to fill out before it is 
# read back into python

# I'll probably need to write one function that creates the excel files with all
# the words and another that reads in the user input

import os
import re
import pyinputplus as pyip
import pandas as pd
import openpyxl

# Example madlib
text = 'The ADJECTIVE ANIMAL PAST-TENSE-VERB into the ADJECTIVE bar, and PAST-TENSE-VERB a(n) NOUN.'

path_prompt = 'Please input in the path where your madlibs are located:\n'
team_num_prompt = 'Please input the number of teams:\n'

# Asks users which path the matlibs are in
#path = pyip.inputFilepath(path_prompt)
path = r'C:\Users\Cleme\Practice_Code\Automate_The_Boring_Stuff\ATBS_side_projects'

os.chdir(path)


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
        theme = pyip.inputMenu(themes, theme_prompt)

        # Text file to be opened (should this be hard coded in or generated based off of the themes)
        filename = theme.lower() + '.txt'

        # Tries to open the file correlating to the theme and recalls the function
        # recursively if there is no file
        try: 
            with open(filename, 'r', encoding="latin-1") as madlibs: 
                read_madlibs = madlibs.read()
            return read_madlibs, theme

        except FileNotFoundError:
            print('Sorry that theme is not available, please pick a different one.\n')
            return choosing_madlib_theme(madlib_themes)

    madlibs_text, theme = choosing_madlib_theme(madlib_themes)

    def madlib_generator(text_file):

        # Define words that would be used in madlibs
        madlib_words = [
            'ADJECTIVE',
            "FRIEND'S NAME",
            r"(?<!FRIEND'S\s)NAME",
            "CELEBRITY",
            # The same matching problem with verbs is going to occur with 
            # nouns and plural nouns
            'NOUN \(PLURAL\)',
            r'NOUN(?!\s[(])',
            'FOOD',
            'ADVERB',
            'PAST TENSE VERB',
            'VERB ENDING IN ING',
            'PRESENT TENSE VERB',
            'ANIMAL',
            'EXCLAMATION',
            'SILLY WORD',
            'LOCATION',
            'CITY',
            'DAY OF THE WEEK',
            'TIME',
            'NUMBER',
            'BODY PART \(PLURAL\)',
            r'BODY PART(?!\s[(])',

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
        # Define a list that contains all the matches for easy iteration
        all_matches = []
        for regex, matches in regex_matches.items():
            # Skips the word if there are no matches
            if len(matches) == 0:
                continue

            else:
                
                # Loops through each match in range of the total matches for each madlib word
                for match in range(len(matches)):
                    all_matches.append(matches[match])
        print(all_matches)

        # Open excel file to input values
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = 'Madlibs Inputs'
        sheet['A1'] = 'Team:'
        sheet['B1'] = team + 1
        sheet['A2'] = 'Theme:'
        sheet['B2'] = theme
        
        # Loop through values to be written to excel file
        row_num = 3
        for match in all_matches:
            sheet.cell(row=row_num, column=1).value = match
            row_num += 1
        # Save the workbook with theme and team number 
        sheet.column_dimensions['A'].width = 20
        sheet.column_dimensions['B'].width = 20
        wb.save(f'Madlibs_theme_{theme}_team_{team + 1}.xlsx')
                            

    madlib_generator(madlibs_text)
