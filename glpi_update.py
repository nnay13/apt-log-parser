import datetime
import re


def parse_apt_log():
    """Parse local apt log and check for today's updates

    Returns:
        str: Log output
    """
    # La fichier de log APT à parser
    APT_LOG_FILE = "/var/log/apt/history.log

    # les paquets mis à jour sont  situés dans un bloc de 4 lignes
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    # Début du bloc
    start_date = "Start-Date: "+today
    log_file = []
    log_index = []
    log_output = []
    with open(APT_LOG_FILE, 'r') as f:
        for index, line in enumerate(f):
            log_file.append(line)
            if start_date in line:
                log_index.append(index)
    for index in log_index:
        log_output.append(log_file[index:index+5])

    return log_output


if __name__ == "__main__":
    log = parse_apt_log()
    print(log[0])


class AptLogEvent(object):
    def __init__(self, log):
        self.start_date = log[0].strip("Start-Date: ")
        self.action = log[1].strip("Commandline: ")
        self.paquets = log[2].strip("")
        return
