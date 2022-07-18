from pathlib import Path

def token_config():

    path_to_file = 'txt_files/token.txt'
    path = Path(path_to_file)
    print("************ Checking for Token File ************")
    if path.is_file():
        print(f'The file {path_to_file} exists')
        return
    else:
        print(f'The file {path_to_file} does not exist so I am creating it\n')
        token_in = input("Please enter your TOKEN: ")
        with open(f'{path_to_file}', 'x') as f:
            f.write(token_in)

token_config()
file = open("txt_files/token.txt")
TOKEN = (file.read())
file.close()

file = open("txt_files/help.txt")
helptxt = (file.read())
file.close()



