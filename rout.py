import click
from utils.docker_helper import sandbox_file_in_container


@click.group()
@click.pass_context
def sandbox(ctx):
    pass


@sandbox.command()
@click.argument('file_path', type=click.Path(exists=True, resolve_path=True))
def java(file_path):
    """>_ sandbox java HelloWorld.java"""
    sandbox_file_in_container('szilagyiabo/alpine-java8', 'runJavaCode ' + str(file_path), file_path)


@sandbox.command()
@click.argument('file_path', type=click.Path(exists=True, resolve_path=True))
def python(file_path):
    """>_ sandbox python HelloSahara.py"""
    sandbox_file_in_container('szilagyiabo/alpine-python', 'python ' + str(file_path), file_path)


@sandbox.command()
@click.argument('file_path', type=click.Path(exists=True, resolve_path=True))
def gcc(file_path):
    """>_ sandbox gcc HelloWord.c"""
    sandbox_file_in_container('szilagyiabo/alpine-gcc', 'runGccCode ' + str(file_path), file_path)
