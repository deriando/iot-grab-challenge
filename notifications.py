import apprise

notif = apprise.Apprise()

#notif.add("mailto://deriando21:mdzbhaaqgzldxcfz@gmail.com")
#notif.add("twilio://AC7dc8922d0fcba2a987b37b830d337e88:ecff7d681e29f98abe47473f90fc032a@1 678 515 9700/65 81002510") #not working?

def telegramNotif(title, body):
    notif.add("tgram://1166066903:AAEfKq6lq5RkOmffXsSpkOzEyJ-KKzKYAGE")
    notif.notify(
        title = title,
        body = body
    )