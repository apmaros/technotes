import os
from pathlib import Path

BASE_PATH = Path(os.getcwd()).parent

_SYSTEM_FOLDERS = {'_assets', 'venv', 'metadata-generator'}
_BLOCKLISTED_FILES = {'readme.md'}
_MD_LEVEL_SYMBOL = '#'

_PROJECT_NAME = "tech notes"


def format_title(title, level):
    return f'{level * _MD_LEVEL_SYMBOL} {title.capitalize()}'


def format_file(file):
    filename = "".join(file.name.split('.')[:-1]).replace("-", " ").capitalize()

    file_chunks = str(file.absolute()).rsplit('interview-preparation')
    file_relative_path = f'.{file_chunks[-1]}'

    return f'- [{filename}]({file_relative_path})'


def should_ignore_dir(dirname):
    return dirname in _SYSTEM_FOLDERS or dirname[0] == '.'


def should_ignore_file(filename):
    return filename.lower() in _BLOCKLISTED_FILES


def is_md_file(filename):
    filename_parts = filename.split('.')
    return filename_parts and filename_parts[-1] == 'md'


def generate_content(dirpath, level, lines):
    dir_items = list(dirpath.iterdir())
    dirs = list(filter(lambda item: item.is_dir(), dir_items))
    files = list(filter(lambda item: item.is_file(), dir_items))

    lines.append(format_title(dirpath.name, level))

    for file in files:
        lines.append(format_file(file))

    for d in dirs:
        generate_content(d, level + 1, lines)

    return lines


def generate_readme(dirs):
    lines = [format_title(_PROJECT_NAME, 1)]
    for d in dirs:
        for line in generate_content(d, 2, []):
            lines.append(line)

    return lines


def build_table_of_content_lines():
    dirs = files = []

    for item in BASE_PATH.iterdir():
        if item.is_file and is_md_file(item.name) and not should_ignore_file(
                item.name):
            files.append(item)

        if item.is_dir() and not should_ignore_dir(item.name):
            dirs.append(item)

    return generate_readme(dirs)


def generate_table_of_content():
    lines = build_table_of_content_lines()
    try:
        with open(Path(BASE_PATH, "Readme.md"), 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
    except Exception as e:
        print(f'failed to write readme due error: {e}')

    print('Success')


if __name__ == '__main__':
    print(f'Generating metadata from {BASE_PATH}')
    generate_table_of_content()

