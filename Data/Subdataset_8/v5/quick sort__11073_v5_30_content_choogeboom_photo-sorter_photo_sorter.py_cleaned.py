import os
import datetime
import logging
import pathlib as pl
import re
from typing import Union, TypeVar
from exifread import process_file
import click
PathLike = Union[str, bytes, pl.Path]
T = TypeVar('T')
Maybe = Union[T, None]
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    logger.addHandler(logging.StreamHandler())
__all__ = ['sort_directory', 'sort_file']
def _copy(self, target: PathLike):
    import shutil
    assert self.is_file()
    shutil.copy(self, target)
pl.Path.copy = _copy
def sort_directory(source_path: PathLike,
                   target_path: PathLike=None,
                   remove_empty: bool=True,
                   recursive=True,
                   copy=False):
    source_path = pl.Path(str(source_path))
    if not target_path:
        target_path = source_path
    target_path = pl.Path(str(target_path))
    assert source_path.is_dir()
    assert target_path.is_dir()
    log_directory_sorting(source_path, target_path, remove_empty, recursive, copy)
    glob_pattern = '**/*.*' if recursive else '*.*'
    sorted_files = set()
    directories_to_delete = set()
    for file in source_path.glob(glob_pattern):
        if file not in sorted_files:
            new_file = sort_file(file, target_path, copy=copy)
            if new_file:
                sorted_files.add(new_file)
            if remove_empty and is_empty_directory(file.parent):
                directories_to_delete.add(file.parent)
    delete_empty_directories(directories_to_delete)
    log_sorting_completion(source_path)
def sort_file(path: pl.Path, target_path: PathLike, copy=False) -> Maybe[pl.Path]:
    path = pl.Path(str(path))
    logger.debug('Sorting file: %s', path)
    date = extract_file_date(path)
    logger.debug('Inferred date: %s', date)
    if date:
        new_path = generate_new_file_path(path, target_path, date)
    else:
        new_path = target_path / 'Unknown_Date' / path.name
    perform_file_move_or_copy(path, new_path, copy)
    return new_path
def generate_new_file_path(path: pl.Path, target_path: pl.Path, date: datetime.date) -> pl.Path:
    new_path = (target_path / date.strftime('%Y') / date.strftime('%Y-%m')
                / date.strftime('%Y-%m-%d') / path.name)
    if new_path != path:
        handle_existing_file(new_path)
    return new_path
def handle_existing_file(new_path: pl.Path):
    if new_path.exists():
        backup_path = get_backup_path(new_path)
        logger.warning('File "%s" already exists in "%s". Saving as "%s" instead.',
                       new_path.name, new_path.parent, backup_path.name)
        return backup_path
def perform_file_move_or_copy(path: pl.Path, new_path: pl.Path, copy: bool):
    if new_path != path:
        create_directory_if_not_exists(new_path)
        if new_path.exists():
            new_path = handle_existing_file(new_path) or new_path
        perform_move_or_copy_operation(path, new_path, copy)
    else:
        logger.debug('File already sorted.')
def extract_file_date(path: pl.Path) -> Maybe[datetime.date]:
    return (extract_file_date_from_metadata(path) or
            extract_file_date_from_filename(path))
def extract_file_date_from_metadata(path: pl.Path) -> Maybe[datetime.date]:
    if path.suffix.lower() in ('.jpg', '.jpeg'):
        date_tag_names = ('EXIF DateTimeOriginal', 'EXIF DateTimeDigitized',
                          'Image DateTime')
        tags = load_tags(path)
        for tag in date_tag_names:
            if tag in tags:
                return parse_date_string(tags[tag].values)
    return None
def extract_file_date_from_filename(path: pl.Path) -> Maybe[datetime.date]:
    pattern = r'(?P<year>\d{4})(.|\s+)?(?P<month>\d{2})(.|\s+)?(?P<day>\d{2})'
    match = re.search(pattern, path.name)
    if match:
        date_kwargs = {k: int(v) for k, v in match.groupdict().items()}
        try:
            return datetime.date(**date_kwargs)
        except ValueError:
            return None
    else:
        return None
def parse_date_string(date_string: str) -> Maybe[datetime.date]:
    try:
        return datetime.datetime.strptime(date_string, '%Y:%m:%d %H:%M:%S').date()
    except ValueError:
        return None
def load_tags(path: pl.Path) -> dict:
    with open(path, 'rb') as image_file:
        return process_file(image_file)
def create_directory_if_not_exists(directory_path: pl.Path):
    if not directory_path.parent.exists():
        directory_path.parent.mkdir(parents=True)
def delete_empty_directories(directories: set):
    for directory in directories:
        if is_empty_directory(directory):
            logger.debug('Removing empty directory: %s', directory)
            directory.rmdir()
def is_empty_directory(path: pl.Path):
    if path.is_dir():
        return sum(1 for _ in path.iterdir()) == 0
    else:
        return False
@click.command()
@click.option('--copy/--move', '-c/-m', 'copy', default=False)
@click.option('--output', '-o', 'target_path',
              default=None,
              type=click.Path(file_okay=False,
                              dir_okay=True,
                              writable=True,
                              readable=True,
                              resolve_path=True))
@click.option('--remove-empty/--no-remove-empty', '-e/-E', default=True)
@click.option('--logger-level', '-l',
              default='info',
              type=click.Choice(['debug', 'info', 'warning', 'error',
                                 'critical']))
@click.option('--recursive/--no-recursive', '-r/-R', default=True)
@click.argument('source_path', type=click.Path(exists=True,
                                               file_okay=False,
                                               dir_okay=True,
                                               writable=True,
                                               readable=True,
                                               resolve_path=True))
def cli(source_path, target_path, remove_empty, copy, recursive, logger_level):
    logger.setLevel(getattr(logging, logger_level.upper()))
    sort_directory(source_path=source_path,
                   target_path=target_path,
                   remove_empty=remove_empty,
                   recursive=recursive,
                   copy=copy)
if __name__ == '__main__':
    cli()