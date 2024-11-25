from pathlib import Path

def read_question(file_name):
   
       # Specify the path to your text file
    file_path = Path(__file__).parent / file_name

    result = ''
    # Open the file in read mode and read its content
    try:
        with open(file_path, 'r') as file:
            result= file.read()
        
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return result