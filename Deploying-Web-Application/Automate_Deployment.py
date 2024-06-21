import paramiko #  For SSH connection
key = paramiko.RSAKey.from_private_key_file("/devops-automation/dev.pem")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for instance_id in instance_ids:
    instance = ec2.describe_instances(InstancesIds=[instance_id])['Reservations'][0]['Instances'][0]
    ssh.connect(instance['PublicIpAddress'], username='ec-user',pkey= 'dev.ppk')
    
    
    commands = [
        "sudo yum update -y"
        "sudo yum install -y httpd"
        "s=aws s3 cp s3://springapp-bucket/application.zip /var/www/html/application.zip",
        "unzip /var/www/html/application.zip -d /var/www/html"
        ]
    for command in commands:
        stdin,stdout,stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        print(stderr.read().decode())
        ssh.closse()