# Automated Network Device Configuration Backup

Automated Network Device Configuration Backup is a Python script that connects to network devices (e.g., routers, switches, firewalls) using SSH key authentication, retrieves their configurations, and stores them in a Git repository. This script provides a reliable way to schedule regular backups of network device configurations and maintain version control for changes.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using this script, make sure you have the following prerequisites in place:

- Python 3.x installed on your system.
- Required Python libraries installed (you can install them using `pip install paramiko gitpython smtplib`).

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ZEKe125/automated-network-backup.git

2. Navigate to the project directory:

   ```bash
   cd automated-network-backup

3. Install the required Python libraries:

   ```bash
   pip install paramiko gitpython smtplib

## Usage

To use the script, follow these steps:

1. Configure the script:

    - Update the network device details, Git repository details, and email notification settings in the script file (backup_script.py).

2. Run the script:

    - This will connect to the network devices, retrieve their configurations, and store them in the Git repository. If any errors occur, email notifications will be sent.

   ```bash
    python backup_script.py

3. Schedule regular backups:

    - You can schedule the script to run at specified intervals using a task scheduler or cron job, depending on your operating system.

## Customization

1. You can customize the script according to your specific requirements:

- Modify the SSH command (`'show running-config'`) in the `backup_device_config()` function to match the command needed for your network devices.
  - **('ip -s link show')**
  - **('ifconfig')**
  - **('ip addr')**
- Add additional error handling or logging as needed.
- Customize the email notification content and settings in the `send_email_notification()` function.

## Contributing

Contributions to this project are welcome. If you encounter issues, have ideas for improvements, or would like to contribute code, please open an issue or create a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer:** Use this script responsibly and ensure it complies with your network device access policies and security guidelines. Always protect sensitive information and credentials.
