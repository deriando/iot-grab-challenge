import apprise

notif = apprise.Apprise()

# notif.add("mailto://email:password@gmail.com")


def telegramNotif(title, body):
    notif.add("tgram://[bottokentoken]")
    notif.notify(
        title=title,
        body=body
    )
