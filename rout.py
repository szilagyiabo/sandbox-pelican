import click
from docker import Client
import dockerpty

docker_client = Client(base_url='unix://var/run/docker.sock')


@click.group()
@click.pass_context
def sandbox(ctx):
    pass


@sandbox.command()
@click.argument('file_path', type=click.Path(exists=True, resolve_path=True))
def java(file_path):
    directory = find_dir(str(file_path))
    container = docker_client.create_container(image='szilagyiabo/alpine-java8', working_dir=directory,
                                               volumes=[directory],
                                               host_config=docker_client.create_host_config(binds=[
                                                   directory + ':' + directory,
                                               ]),
                                               stdin_open=True, tty=True,
                                               command='runJavaCode ' + str(file_path))
    dockerpty.start(docker_client, container)
    docker_client.remove_container(container)


@sandbox.command()
@click.argument('file_path', type=click.Path(exists=True, resolve_path=True))
def python(file_path):
    directory = find_dir(str(file_path))
    container = docker_client.create_container(image='szilagyiabo/alpine-python', working_dir=directory,
                                               volumes=[directory],
                                               host_config=docker_client.create_host_config(binds=[
                                                   directory + ':' + directory,
                                               ]),
                                               stdin_open=True, tty=True,
                                               command='python ' + str(file_path))
    dockerpty.start(docker_client, container)
    docker_client.remove_container(container)


@sandbox.command()
@click.argument('file_path', type=click.Path(exists=True, resolve_path=True))
def gcc(file_path):
    pass


def find_dir(path_to_file):
    last_slash = path_to_file.rfind('/')
    return path_to_file[0:last_slash+1]
