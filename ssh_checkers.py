import paramiko
import yaml

with open('settings.yaml') as f:
    data = yaml.safe_load(f)

def ssh_checkout(host, user, password, cmd, text, port=data['port']):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode('utf-8')
    client.close()
    if text in out and exit_code == 0:
        return True
    return False


def ssh_checkout_negative(host, user, password, cmd, text, port=data['port']):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode('utf-8')
    client.close()
    if text in out and exit_code != 0:
        return True
    return False


def ssh_checkout_get(host, user, password, cmd, port=data['port']):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    out = (stdout.read() + stderr.read()).decode('utf-8')
    client.close()
    return out