import os


def mac_notify(title, message):
    os.system('terminal-notifier -title "' + str(title) + '" -message "' + str(
        message) + '"')
    os.system("say Sir, " + str(message))
    return True


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
