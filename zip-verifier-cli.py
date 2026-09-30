import click
from zipfile import ZipFile
from pathlib import Path

def verify_zip(zip_path: Path, manifest_path: Path) -> bool:
    with ZipFile(zip_path, 'r') as zip_file:
        zip_contents = set(zip_file.namelist())
    with manifest_path.open('r') as manifest_file:
        manifest_contents = set(line.strip() for line in manifest_file)
    return zip_contents == manifest_contents

def main(zip_path: Path, manifest_path: Path):
    if verify_zip(zip_path, manifest_path):
        click.secho('Verification successful!', fg='green')
    else:
        click.secho('Verification failed!', fg='red')

click.command()(main)
