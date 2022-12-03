def my_message(code):
    """
        Message to user email
    """
    email_body = "Ваш код активации: " + code
    email_subject = "Активация аккаунта"
    message = {"email_body": email_body, "email_subject": email_subject}
    return message


def get_message_for_test(point: int, required_score: int) -> str:
    message = ''
    if point >= required_score and point == 100:
        message = 'Поздравляем! Вы набрали максимальное количество баллов в данном тестировании.'
    elif point >= required_score and point < 100:
        message = f'Поздравляем! Вы успешно прошли тестирование. Количество баллов которое вы набрали - {point}.'
    elif point < required_score:
        message = 'К сожалению, вы не достигли порогового балла. Не расстраивайтесь, попробуйте пройти тест снова через некоторое время.'
    return message



