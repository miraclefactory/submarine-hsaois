import paramiko


def remove_db_x():
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname='124.223.101.237', port=22, username='root', password='806710_zzh')

    stdin, stdout, stderr = client.exec_command('cd /')
    stdin, stdout, stderr = client.exec_command('cd www/wwwroot/hsaois_server/app')
    stdin, stdout, stderr = client.exec_command('rm -rf hsaois.db')

    localpath = './hsaois.db'

    print(stdout.read().decode('utf-8'))

    client.close()


def sync_db():
    tran = paramiko.Transport(('124.223.101.237', 22))
    tran.connect(username="root", password='806710_zzh')
    # 获取SFTP实例
    sftp = paramiko.SFTPClient.from_transport(tran)
    # 设置上传的本地/远程文件路径
    localpath = "../hsaois.db"
    remotepath = "/www/wwwroot/hsaois_server/app/hsaois.db"
    sftp.remove(remotepath)
    sftp.put(localpath, remotepath)
    tran.close()
