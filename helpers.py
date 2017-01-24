import os


def mac_notify(title, message):
    os.system('terminal-notifier -title "' + str(title) + '" -message "' + str(
        message) + '"')
    os.system("say Sir, " + str(message))
    return True
