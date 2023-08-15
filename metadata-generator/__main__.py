import logging
import os
import sys
from os.path import relpath
from pathlib import Path

BASE_PATH = Path(os.getcwd())
DOCS_PATH = Path('./docs')
TOC_OUTPUT_FILENAME = './README.md'
TABLE_OF_CONTENT_OUTPUT_FILE_PATH = Path(BASE_PATH, TOC_OUTPUT_FILENAME)

SYSTEM_FOLDERS = {'_assets', 'venv', 'metadata-generator'}
BLOCKLISTED_FILES = {'readme.md', '.ds_store'}
_MD_LEVEL_SYMBOL = '#'
_EMPTY_LINE = ""
_PROJECT_NAME = "tech notes"


def format_title(title, level):
    return f'\n{level * _MD_LEVEL_SYMBOL} {title.capitalize()}\n'


def format_file(file):
    filename = "".join(
        file.name.split('.')[:-1]
    ).replace("-", " ").capitalize()

    filepath = relpath(file.absolute())
    return f'- [{filename}](./{filepath})'


def should_ignore_dir(dirname):
    return dirname in SYSTEM_FOLDERS or dirname[0] == '.'


def should_ignore_file(filename):
    return filename.lower() in BLOCKLISTED_FILES


def is_md_file(filename):
    filename_parts = filename.split('.')
    return filename_parts and filename_parts[-1] == 'md'


def generate_lines_for_dir(dir_path, level, lines):
    if level > 1:
        lines.append(format_title(dir_path.name, level))
    logging.debug(f'{level*" "} exploring dir={dir_path.name}')
    dir_items = list(dir_path.iterdir())
    dirs = list(filter(
        lambda item: item.is_dir() and not should_ignore_dir(item.name),
        dir_items
    ))
    files = list(filter(
        lambda item: item.is_file() and not should_ignore_file(item.name),
        dir_items
    ))
    if files:
        logging.debug(f'{(level+1)*" "} found files:')
    for file in files:
        logging.debug(f'{(level+1)*" "} {relpath(file.absolute())}')
        lines.append(format_file(file))
    if dirs:
        logging.debug(f'{(level + 1) * " "} found dirs:')
    for d in dirs:
        logging.debug(f'{(level + 1)*" "} {d}')
        generate_lines_for_dir(d, level + 1, lines)

    return lines


def build_table_of_content_lines():
    logging.debug(
        f'Building table of content from base folder_name={DOCS_PATH}'
    )

    if not DOCS_PATH.exists() or not DOCS_PATH.is_dir():
        raise IOError(f'Folder at path={DOCS_PATH.absolute()} must exist')

    # initialize table of content lines with title
    lines = [format_title(_PROJECT_NAME, 1)]
    for line in generate_lines_for_dir(DOCS_PATH, 1, []):
        lines.append(line)

    return lines


def flush_table_of_content(lines, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def generate_table_of_content(output_path):
    lines = build_table_of_content_lines()
    logging.info(f"table_of_content_length={len(lines)}")
    try:
        flush_table_of_content(lines, output_path)
    except Exception as err:
        logging.info(f'failed to write readme due error: {err}')


def write_table_of_content():
    logging.info(f'Generating metadata from {BASE_PATH}')

    try:
        generate_table_of_content(TABLE_OF_CONTENT_OUTPUT_FILE_PATH)
    except Exception as e:
        logging.error('Failed to generate table of content due to error')
        raise e

    logging.info(
        f'Wrote table of content to file path'
        f' {TABLE_OF_CONTENT_OUTPUT_FILE_PATH.absolute()} 🎉'
    )


if __name__ == '__main__':
    if (len(sys.argv) == 2 and (
            sys.argv[1] == '-v' or sys.argv[0] == '--verbose')):
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.root.setLevel(level)
    logging.basicConfig(format='%(levelname)s:%(message)s', level=level)

    write_table_of_content()
