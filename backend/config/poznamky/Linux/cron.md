
## List Current CRON Jobs
crontab -l

## Edit CRON Jobs
crontab -e
## Edit CRON jobs for the root user:
sudo crontab -u root -e
## List CRON jobs for the root user:
sudo crontab -u root -l

## View Completed CRON Jobs
sudo cat /var/log/syslog | grep cron

## Check if CRON is Running
sudo systemctl status cron

1. Minute (0-59)
2. Hour (0-23)
3. Day of Month (1-31)
4. Month (1-12)
5. Day of Week (0-6) (Sunday to Saturday, with Sunday as 0 or 7 )


## General Format
* * * * * command_to_run



## Every Minute
* * * * * echo "hello world"

## On the Fifth Minute of Every Hour
5 * * * * command_to_run

## At 09:05 Every Day
5 9 * * * command_to_run

## At 09:05 on the 15th Day of Every Month
5 9 15 * * command_to_run

## At 09:05 on December 15th Every Year
5 9 15 12 * command_to_run

## At 09:05 on December 15th, but Only if it is Sunday
5 9 15 12 0 command_to_run
5 9 15 12 7 command_to_run

@hourly echo "Running hourly task"
@reboot echo "Running at startup"



## Output Redirection (This captures both standard output and error messages.)
* * * * * command_to_run >> /path/to/logfile.log 2>&1

## Setting Environment Variables: Mention that CRON jobs run in a limited environment. Users may need to set environment variables explicitly
## Declare Variables Directly in the Crontab
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

## Declare Variables Inline with Commands
0 0 * * * APP_ENV=staging /path/to/script.sh     ## Runs daily at midnight

## Inside script.sh
#!/bin/bash
export APP_ENV=production
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin


## Security Best Practices
- Limiting the use of sudo in CRON jobs.
- Ensuring scripts run with the least privilege necessary.


## TODO:
- The difference between using crontab -e and editing /etc/crontab.
- Time zone considerations, especially on servers.

