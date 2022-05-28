from pathlib import Path

def installer():

    path_to_file = 'token.txt'
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

installer()
file = open("token.txt")
TOKEN = (file.read())
file.close()

