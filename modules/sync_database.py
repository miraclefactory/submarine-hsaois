
import paramiko

def sync_db(self):
    try:
        tran = paramiko.Transport(('124.223.101.237', 22))
        tran.connect(username="root", password='zzh_xyl_123')
        # 获取SFTP实例
        sftp = paramiko.SFTPClient.from_transport(tran)
        # 设置上传的本地/远程文件路径
        localpath = "./hsaois.db"
        remotepath = "/www/wwwroot/hsaois_server/app/hsaois.db"
        sftp.remove(remotepath)
        sftp.put(localpath, remotepath)
        tran.close()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname='124.223.101.237', port=22, username='root', password='zzh_xyl_123')
        stdin, stdout, stderr = client.exec_command('chown www /www/wwwroot/hsaois_server/app/hsaois.db')
        client.close()
        return True
    except Exception as e:
        print(e)
        self.es.message_box.emit("Error", "Error:\n\n" + str(e))
        return False
