#TryHackMe

What is the default command line interpreter in the Windows environment?

Answer: `cmd.exe`

What is the OS version of the Windows VM?

Answer: `10.0.20348.2655`

What is the hostname of the Windows VM?

Answer: `WINSRV2022-CORE`

What are the file’s contents in C:\Treasure\Hunt?

Answer: `THM{CLI_POWER}`

What command would you use to find the running processes related to notepad.exe?

Answer: `tasklist /FI "imagename eq notepad.exe"`

What command can you use to kill the process with PID 1516?

Advantages using a CLI:
Lower resource usage.
Automation.
Remote management.

SSH syntax: `ssh <username>@<MACHINE_IP>`
The credentials for this room:
Username: user
Password: Tryhackme123!

Other useful commands:
help
cls - Clears command prompt screen.

You can find this by entering the ver command.

cd command to navigate between directories.
cd .. to go up one level.
dir view child directories.
dir /a - Displays hidden and system files.
dir /s - Displays files in current directory and all subdirectories.
mkdir directory_name - creates a directory.

With known process ID (PID), terminate task using taskkill /PID target_pid
