import logging.handlers
file_handler = logging.FileHandler('/var/log/docker-cmd.log')
cmd_logger = logging.getLogger("hamravesh-cmd")
cmd_logger.addHandler(file_handler)
cmd_logger.error('Monitoring:%s', str_command.cout)
cmd_logger.removeHandler(file_handler)