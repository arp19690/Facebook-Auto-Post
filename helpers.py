import os


def mac_notify(title, message):
    os.system('terminal-notifier -title "' + str(title) + '" -message "' + str(message) + '"')
    return True
