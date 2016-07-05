from docker import Client
import dockerpty

docker_client = Client(base_url='unix://var/run/docker.sock')


def sandbox_file_in_container(container, command, file_path):
    directory = _find_dir(str(file_path))
    container = docker_client.create_container(image=container, working_dir=directory,
                                               volumes=[directory],
                                               host_config=docker_client.create_host_config(binds=[
                                                   directory + ':' + directory,
                                               ]),
                                               stdin_open=True, tty=True,
                                               command=command)
    dockerpty.start(docker_client, container)
    docker_client.remove_container(container)


def _find_dir(path_to_file):
    last_slash = path_to_file.rfind('/')
    return path_to_file[0:last_slash + 1]
