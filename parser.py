# read file and parse it

import os
import sys
import pandas as pd

rows = []

def parse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f'File not found: {file_path}')
        sys.exit(1)


def main():
    problems = []
    set_goals = []
    generate_solutions = []
    evaluate_solutions = []
    file_path = os.path.join('TRAIN_DATA.txt')
    content = parse_file(file_path)
    cases = content.split('Example Case')
    cases = cases[1:]
    for i, case in enumerate(cases):
        # get all text after Problem: until the next newline
        problem = case.split('Problem: ')[1].split('\n')[0]
        # get all text after Set Goals: until the Generate Solutions:
        set_goal = case.split('Set Goals:')[1].split('Generate Solutions:')[0].strip()
        # get all text after Generate Solutions: until the Evaluate Solutions:
        generate_solution = case.split('Generate Solutions:')[1].split('Evaluate Solutions:')[0].strip()
        # get all text after Evaluate Solutions: until the Choose & Implement a Solution:
        evaluate_solution = case.split('Evaluate Solutions:')[1].split('Choose & Implement a Solution:')[0].strip()
        problems.append(problem)
        set_goals.append(set_goal)
        generate_solutions.append(generate_solution)
        evaluate_solutions.append(evaluate_solution)

    df = pd.DataFrame({
        'Problem': problems,
        'Set Goals': set_goals,
        'Generate Solutions': generate_solutions,
        'Evaluate Solutions': evaluate_solutions
    })

    df.to_csv('TRAIN_DATA.csv', index=False)



main()

#%%
