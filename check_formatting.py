def check_file_formatting(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    issues_found = False
    
    for i in range(0, len(lines), 2):
        human_text = lines[i].strip()
        
        try:
            robot_text = lines[i+1].strip()
            if not human_text.startswith('HUMAN:') or not robot_text.startswith('ROBOT:'):
                print(f"Inconsistency at lines {i+1} and {i+2}.")
                issues_found = True
        except IndexError:
            print(f"Missing robot response at line {i+2}.")
            issues_found = True
            
    if not issues_found:
        print("No formatting issues found.")
    else:
        print("Some formatting issues were detected. Please check the specified lines.")

# Check the formatting of the train and test files
check_file_formatting('/Users/vaibhavreddy/Documents/Scripts/Conversational_Analysis/training_&_testing_data/train_pairs.txt')
