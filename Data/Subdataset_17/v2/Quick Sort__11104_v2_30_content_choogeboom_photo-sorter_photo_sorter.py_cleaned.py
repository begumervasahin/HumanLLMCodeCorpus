import os
import datetime
import logging
import pathlib as pl
import re
from typing import Union, TypeVar, Optional
from exifread import process_file
import click
PathLike = Union[str, bytes, pl.Path]
T = TypeVar('T')
Maybe = Optional[T]
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    logger.addHandler(logging.StreamHandler())
def _copy(self, target: PathLike):
    import shutil
    assert self.is_file()
    shutil.copy(self, target)
pl.Path.copy = _copy
def sort_directory(source_path: PathLike, target_path: PathLike = None, remove_empty: bool = True, recursive: bool = True, copy: bool = False):
    source_path = pl.Path(source_path)
    target_path = pl.Path(target_path) if target_path else source_path
    assert source_path.is_dir()
    assert target_path.is_dir()
    logger.info('=' * 20 + '\nSorting photos in "%s"', source_path)
    if source_path != target_path:
        logger.info('Outputting to "%s"', target_path)
    logger.debug('remove-empty: %s', remove_empty)
    logger.debug('recursive: %s', recursive)
    logger.debug('copy: %s', copy)
    logger.info('=' * 20)
    glob_pattern = '**/*.*' if recursive else '*.*'
    sorted_files = set()
    directories_to_delete = set()
    for file in source_path.glob(glob_pattern):
        if file not in sorted_files:
            new_file = sort_file(file, target_path, copy=copy)
            if new_file:
                sorted_files.add(new_file)
            if remove_empty and is_empty_dir(file.parent):
                directories_to_delete.add(file.parent)
    for directory in directories_to_delete:
        logger.info('Removing empty directories')
        if is_empty_dir(directory):
            logger.debug('Removing empty directory: %s', directory)
            directory.rmdir()
    logger.info('=' * 20 + '\nSorting photos in "%s" completed successfully!', source_path)
def sort_file(path: pl.Path, target_path: PathLike, copy: bool = False) -> Maybe[pl.Path]:
    logger.debug('Sorting file: %s', path)
    date = get_file_date(path)
    logger.debug('Inferred date: %s', date)
    if date:
        new_path = target_path / date.strftime('%Y') / date.strftime('%Y-%m') / date.strftime('%Y-%m-%d') / path.name
    else:
        new_path = target_path / 'Unknown_Date' / path.name
    if new_path != path:
        if not new_path.parent.exists():
            logger.debug('Creating new directory: %s', new_path.parent)
            new_path.parent.mkdir(parents=True)
        if new_path.exists():
            backup_path = get_backup_path(new_path)
            logger.warning('File "%s" already exists in "%s". Saving as "%s" instead.', new_path.name, new_path.parent, backup_path.name)
            new_path = backup_path
        if copy:
            logger.info('Copying "%s" to "%s"', new_path.name, new_path.parent)
            path.copy(new_path)
        else:
            logger.info('Moving "%s" to "%s"', new_path.name, new_path.parent)
            path.rename(new_path)
    else:
        logger.debug('File already sorted.')
    return new_path
def get_backup_path(path: pl.Path) -> pl.Path:
    def make_path(source_path: pl.Path, number: int) -> pl.Path:
        return source_path.with_name(f'{source_path.stem}_{number}{source_path.suffix}')
    backup_count = 0
    new_path = make_path(path, backup_count)
    while new_path.exists():
        backup_count += 1
        new_path = make_path(path, backup_count)
    return new_path
def is_empty_dir(path: pl.Path) -> bool:
    return path.is_dir() and not any(path.iterdir())
def get_file_date(path: pl.Path) -> Maybe[datetime.date]:
    return get_file_date_from_metadata(path) or get_file_date_from_filename(path) or get_file_date_from_mtime(path)
def get_file_date_from_metadata(path: pl.Path) -> Maybe[datetime.date]:
    if path.suffix.lower() in ('.jpg', '.jpeg'):
        date_tag_names = ('EXIF DateTimeOriginal', 'EXIF DateTimeDigitized', 'Image DateTime')
        tags = load_tags(path)
        for tag in date_tag_names:
            if tag in tags:
                date_str = tags[tag].values
                dt = datetime.datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
                return dt.date()
    return None
def get_file_date_from_filename(path: pl.Path) -> Maybe[datetime.date]:
    pattern = r'(?P<year>\d{4})(.|\s+)?(?P<month>\d{2})(.|\s+)?(?P<day>\d{2})'
    match = re.search(pattern, path.name)
    if match:
        date_kwargs = {k: int(v) for k, v in match.groupdict().items()}
        try:
            return datetime.date(**date_kwargs)
        except ValueError:
            return None
    return None
def get_file_date_from_mtime(path: pl.Path) -> datetime.date:
    return datetime.date.fromtimestamp(os.path.getmtime(path))
def load_tags(path: pl.Path) -> dict:
    with open(path, 'rb') as image_file:
        return process_file(image_file)
@click.command()
@click.option('--copy/--move', '-c/-m', 'copy', default=False, help="Copy files instead of moving them.")
@click.option('--output', '-o', 'target_path', default=None, type=click.Path(file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True), help="Target directory for sorted files.")
@click.option('--remove-empty/--no-remove-empty', '-e/-E', default=True, help="Remove empty directories after sorting.")
@click.option('--logger-level', '-l', default='info', type=click.Choice(['debug', 'info', 'warning', 'error', 'critical']), help="Set the logging level.")
@click.option('--recursive/--no-recursive', '-r/-R', default=True, help="Sort files in subdirectories recursively.")
@click.argument('source_path', type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True))
def cli(source_path, target_path, remove_empty, copy, recursive, logger_level):
    logger.setLevel(getattr(logging, logger_level.upper()))
    sort_directory(source_path=source_path, target_path=target_path, remove_empty=remove_empty, recursive=recursive, copy=copy)
if __name__ == '__main__':
    cli()