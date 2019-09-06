import  datetime
import  re

def parse_apt_log():
    """Parse local apt log and check for today's updates
    
    Returns:
        str: Log output
    """
    #La fichier de log APT à parser
    APT_LOG_FILE = "/var/log/apt/history.log"
    
    #les paquets mis à jour sont  situés dans un bloc de 4 lignes
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    #Début du bloc
    start_date = "Start-Date: "+today
    end_date = "End-Date: "+today
    log_output=[]
    with open(APT_LOG_FILE, 'r') as f:
        line = f.readline()
        while line:
            if start_date in line:
                log_output.append(line)
                line = f.readline()
                while line: 
                    log_output.append(line)
                    if end_date in line:
                        line = f.readline()
                        break
                    else: 
                        line = f.readline()
            else:
                line = f.readline()
    return log_output

if __name__ == "__main__":
    print(parse_apt_log())
    