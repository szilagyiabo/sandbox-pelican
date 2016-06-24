import click
import subprocess


@click.group()
@click.pass_context
def sandbox(ctx):
    pass


@sandbox.command()
@click.argument('file')
def java(file):
    pass

