import paramiko
import git
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define network device details
device_ip = '172.31.41.198'
device_port = 22
device_username = 'ec2'
device_password = 'hello'

# Define Git repository details
repo_path = '/home/ec2-user/backup-result'
repo_url = 'https://github.com/ZEKe125/backup-result.git'

# Define email notification settings
email_from = 'ezelcuevas@gmail.com'
email_to = 'ezelcuevas@gmail.com'
email_subject = 'Network Device Configuration Backup'

# Function to connect to the network device and retrieve configuration
def backup_device_config():
    try:
        # Connect to the network device using SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device_ip, port=device_port, username=device_username, password=device_password)

        # Send a command to retrieve the configuration (replace with your specific command)
        stdin, stdout, stderr = ssh.exec_command('ip a')

        # Read the configuration data
        config_data = stdout.read().decode()

        # Close the SSH connection
        ssh.close()

        return config_data
    except Exception as e:
        print(f'Error: {str(e)}')
        return None

# Function to commit configuration to Git repository
def commit_to_git(config_data):
    try:
        # Initialize the Git repository
        repo = git.Repo(repo_path)

        # Create a Git commit with the configuration data
        repo.index.add(['config.txt'])
        repo.index.commit('Backup configuration')
        
        # Push the changes to the remote repository
        origin = repo.remote('origin')
        origin.push()
    except Exception as e:
        print(f'Git Error: {str(e)}')

# Function to send email notifications
def send_email_notification(message):
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = email_subject
    msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_from, 'your_email_password')
    #server.sendmail(email_from, email_to, msg.as_string())
    server.quit()

if __name__ == '__main__':
    config_data = backup_device_config()
    if config_data:
        # Save configuration to a file (adjust the filename as needed)
        with open(os.path.join(repo_path, 'config.txt'), 'w') as config_file:
            config_file.write(config_data)
        
        # Commit and push to Git
        commit_to_git(config_data)
