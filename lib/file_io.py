from pathlib import Path

def write_file(file_name, file_content):
    file_name = Path(file_name)
    if not file_name.suffix == '.txt':
        file_name = file_name.with_suffix('.txt')
    with open(file_name, mode='w', encoding='utf-8') as file:
        file.write(file_content)   

def append_file(file_name, file_content):
    file_name = Path(file_name)
    if not file_name.suffix == '.txt':
        file_name = file_name.with_suffix('.txt')
    with open(file_name, mode='a', encoding='utf-8') as file:
        file.write(file_content)

def read_file(file_name):
    file_name = Path(file_name)
    if not file_name.suffix == '.txt':
        file_name = file_name.with_suffix('.txt')
    
    if file_name.exists():
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        return "File not found."