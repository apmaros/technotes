import logging
import os
import sys
from pathlib import Path

_BASE_PATH = Path(os.getcwd())
_DOCS_PATH = Path('./docs')
_TOC_OUTPUT_FILENAME = './Readme.md'
TABLE_OF_CONTENT_OUTPUT_FILE_PATH = Path(_BASE_PATH, _TOC_OUTPUT_FILENAME)

_SYSTEM_FOLDERS = {'_assets', 'venv', 'metadata-generator'}
_BLOCKLISTED_FILES = {'readme.md'}
_MD_LEVEL_SYMBOL = '#'
_EMPTY_LINE = ""
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


def generate_lines_for_dir(dir_path, level, lines):
    dir_items = list(dir_path.iterdir())
    dirs = list(filter(lambda item: item.is_dir(), dir_items))
    files = list(filter(lambda item: item.is_file(), dir_items))

    lines.append(format_title(dir_path.name, level))
    lines.append(_EMPTY_LINE)

    for file in files:
        lines.append(format_file(file))

    for d in dirs:
        generate_lines_for_dir(d, level + 1, lines)

    return lines


def build_table_of_content_lines():
    logging.debug(
        f'Building table of content from base folder_name={_DOCS_PATH}'
    )

    if not _DOCS_PATH.exists() or not _DOCS_PATH.is_dir():
        raise IOError(f'Folder at path={_DOCS_PATH.absolute()} must exist')

    lines = [format_title(_PROJECT_NAME, 1), _EMPTY_LINE]
    for line in generate_lines_for_dir(_DOCS_PATH, 2, []):
        lines.append(line)

    return lines


def write_table_of_content(lines, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def generate_table_of_content(output_path):
    lines = build_table_of_content_lines()
    logging.info(f"table_of_content_length={len(lines)}")
    try:
        write_table_of_content(lines, output_path)
    except Exception as e:
        logging.info(f'failed to write readme due error: {e}')


def _set_logger(log_level):
    logging.root.setLevel(log_level)
    logging.basicConfig(format='%(levelname)s:%(message)s', level=log_level)


if __name__ == '__main__':
    if (len(sys.argv) == 2
            and (sys.argv[1] == '-v' or sys.argv[0] == '--verbose')):
        level = logging.DEBUG
    else:
        level = logging.INFO
    _set_logger(level)

    logging.info(f'Generating metadata from {_BASE_PATH}')

    try:
        generate_table_of_content(TABLE_OF_CONTENT_OUTPUT_FILE_PATH)
    except Exception as e:
        logging.error('Failed to generate table of content due to error', e)
    logging.info(
        f'Wrote table of content to file = {TABLE_OF_CONTENT_OUTPUT_FILE_PATH.absolute()} 🎉'
    )
