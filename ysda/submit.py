#!/usr/bin/env python3
import subprocess
from pathlib import Path
import sys
import os
from os import path
import shutil


SHADOW_REPO_DIR = '../.submit-repo'
IGNORE_FILE_PATTERNS = ['test_public.py', '__pycache__']
VERBOSE = False


def print_command(*args):
    print('>', *args, file=sys.stderr)
    sys.stderr.flush()


def git(*args):
    command_args = ['git'] + list(args)
    stdout = subprocess.DEVNULL

    if VERBOSE:
        print_command(' '.join(command_args))
        stdout = None

    subprocess.run(
        command_args, cwd=SHADOW_REPO_DIR,
        stderr=subprocess.STDOUT, stdout=stdout, check=True
    )


def git_output(*args):
    command_args = ['git'] + list(args)

    if VERBOSE:
        print_command(' '.join(command_args))

    return subprocess.check_output(
        command_args
    ).strip().decode('utf-8')


def clean_up():
    try:
        shutil.rmtree(SHADOW_REPO_DIR)
    except PermissionError:
        if sys.platform.startswith('win'):
            # Windows related staff for correct deletion
            os.system('rmdir /s /q "{}"'.format(SHADOW_REPO_DIR))
        else:
            raise
    except FileNotFoundError:
        pass


def set_up_shadow_repo(task_name):
    print('Setting up repo...')
    clean_up()
    os.makedirs(SHADOW_REPO_DIR)

    git('init')
    git('remote', 'add', 'local', '..')
    try:
        git('fetch', 'local',
            '+refs/heads/submits/{0}:refs/heads/submits/{0}'.format(task_name))
    except subprocess.CalledProcessError:
        pass

    user_name = git_output('config', 'user.name')
    user_email = git_output('config', 'user.email')
    student_url = git_output('config', '--get', 'remote.student.url')
    git('remote', 'add', 'student', student_url)

    with open(path.join(SHADOW_REPO_DIR, '.git', 'config'),
              mode='a', encoding='utf-8') as config:
        config.write(
            '[user]\n\tname = {}\n\temail = {}\n'.format(user_name, user_email)
        )


def add_grader_ci():
    shutil.copyfile(
        '../.grader-ci.yml',
        path.join(SHADOW_REPO_DIR, '.gitlab-ci.yml')
    )
    git('add', '.gitlab-ci.yml')


def copy_files(source: Path, target: Path, ignore_patterns):
    ignore_files = sum([
        list(source.glob(ignore_pattern))
        for ignore_pattern in ignore_patterns
    ], [])
    target.mkdir(parents=True, exist_ok=True)
    for file in source.iterdir():
        if file in ignore_files:
            continue
        source_path = source / file.name
        target_path = target / file.name
        if file.is_dir():
            copy_files(source_path, target_path, ignore_patterns)
            continue
        shutil.copyfile(str(source_path), str(target_path))


def create_commits(task_name):
    git('checkout', '-b', 'initial')
    add_grader_ci()
    git('commit', '-m', 'initial')

    print('Creating submit commit...')
    try:
        git('checkout', 'submits/' + task_name)
    except subprocess.CalledProcessError:
        git('checkout', '-b', 'submits/' + task_name)
    git('rm', '-r', '.')
    add_grader_ci()

    copy_files(Path('.'), Path(SHADOW_REPO_DIR) / task_name, IGNORE_FILE_PATTERNS)
    git('add', '--all')
    git('commit', '-m', task_name, '--allow-empty')


def push_branches(task_name):
    print('Pushing changes to remote repo...')
    git('push', 'local', 'submits/' + task_name)
    try:
        git('push', '-f', 'student', 'initial')
    except subprocess.CalledProcessError:
        pass
    git('push', '-f', 'student', 'submits/' + task_name)


def main():
    if '-v' in sys.argv:
        global VERBOSE
        VERBOSE = True

    task_name = path.basename(path.realpath('.'))

    set_up_shadow_repo(task_name)
    create_commits(task_name)
    push_branches(task_name)
    print('Done.')

    student_url = git_output('config', '--get', 'remote.student.url')
    student_url = student_url.replace(':', '/') \
        .replace('.git', '/pipelines').replace('git@', 'https://')
    print('\nYou can track your submission at:\n{}'.format(
        student_url
    ))


if __name__ == '__main__':
    main()
