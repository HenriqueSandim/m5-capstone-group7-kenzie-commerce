
def choices_error_message(choices_class):
    valid_choices = [key[0] for key in choices_class.choices]
    last_choice = valid_choices.pop()

    choices_string = "Valid choices for this field are "

    for choice in valid_choices: 
        choices_string += f"{choice}, "

    choices_string = f"{choices_string[0:-2]} or {last_choice}"

    choices_string += ", please use one."

    return choices_string