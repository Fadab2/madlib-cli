import argparse
import re

# Print a welcome message to the user, explaining the Madlib process and command line interactions
# Read a template Madlib file (Example), and parse that file into usable parts.
# Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
# With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
# After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
# Write the completed text (Example)to a new file on your file system (in the repo).
# Note: A smaller example file is included as well which can be handy when developing/testing.



def read_template():
    '''
    A function to read a file and return the result
    '''
    template = "madlib_cli/assets/dark_and_stormy_night_template.txt"
   
    with open(template, 'r') as reader:  
        read_file = reader.read()  
        return read_file

        
    

#******************************************************************************
user_responses = []
get_place_holders = []
def parse_template(text):
    '''
    A function to extract place holders from the passed text file.
    By finding the opening and closing curly braces and then prompting the user for an input for each place holder
    Store user response in a list and then return the list
    '''

    get_place_holders = re.findall(r'\{.*?\}', text) 
    # use the list of placeholders iterate through the list and with every placeholder display an input request.
    # display a prompt using the indexes
    for prompt in get_place_holders:
        # remove curl braces 
        prompt = prompt[1:-1]
       
        user_input = input(f'Enter: {prompt} ')
        user_responses.append(user_input)
    print(user_responses)



#******************************************************************************
def merge(text, response):
    
    '''
A function to merge the user responses into the corresponding place holders
and write the result into a file and then display the results to the user
'''
    # file to store the final results
    output_file =  "madlib_cli/assets/output_file.txt" 
    
    for place_holder in text:
        if place_holder[1:-1] == "{}":
            place_holder.replace


    pass

if __name__=="__main__":
    
    file_read = read_template()
    parse_template(file_read)
    #merge(file_read, user_responses)

