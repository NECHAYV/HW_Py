def get_mask_card_number(number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску, номер карты замаскирован."""
    card_number = ""
    if len(number) != 16:
        return "Error"
    for num in range(len(number)):
        if number[num].isalpha():
            return "Error"
    else:
        for num in range(len(number)):
            if number[num].isalpha() or number[num] == " ":
                pass
            else:
                card_number += number[num]
        correct_number = card_number[0:7] + card_number[7:14] + card_number[14:19]
        number_mask = (
            correct_number[0:4]
            + " "
            + correct_number[4:6]
            + "**"
            + " "
            + "****"
            + " "
            + correct_number[12:16]
        )
        return number_mask


def get_mask_account(number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску, номер счета замаскирован."""
    if len(number) < 20:
        return "Error"
    for num in range(len(number)):
        if number[num].isalpha():
            return "Error"
    else:
        number_mask = "**" + number[-4:]
        return number_mask
