def send_email (message, recipient, sender = "university.help@gmail.com"):
    if "@" not in recipient or not (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")):
       print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправлять письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправленно с адреса {sender} на адрес {recipient} с сообщением: {message}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email("привет", "gevorgyan@gmail.coms")
send_email("как дела?", "gevorhyan@gmail.ru")
send_email("Чисто проверка!", "mikhail@mail.ru", sender= "mikhail@mail.ru")
send_email("Совершенно секретно!", "mikhail@gmail.net", sender="university.vip@gmail.com")
