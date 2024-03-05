import inquirer

def get_dynamic_choices(selected_options):
    dynamic_choices = {
        "Option 1": ["Suboption 1-1", "Suboption 1-2"],
        "Option 2": ["Suboption 2-1", "Suboption 2-2"],
    }
    choices = []
    for option in selected_options:
        choices.extend(dynamic_choices.get(option, []))
    return choices

questions = [
    inquirer.Checkbox('options',
                      message="Select your options",
                      choices=['Option 1', 'Option 2']),
]

answers = inquirer.prompt(questions)

follow_up_questions = [
    inquirer.Checkbox('suboptions',
                      message="Select your suboptions",
                      choices=lambda answers: get_dynamic_choices(answers['options']),
                      ),
]

sub_answers = inquirer.prompt(follow_up_questions)

print(sub_answers)
