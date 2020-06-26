import apprise

notif = apprise.Apprise()

#notif.add("mailto://email:password@gmail.com")

def telegramNotif(title, body):
    notif.add("tgram://1166066903:AAEfKq6lq5RkOmffXsSpkOzEyJ-KKzKYAGE")
    notif.notify(
        title = title,
        body = body
    )