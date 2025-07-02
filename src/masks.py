import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
def get_mask_card_number(number: str) -> str:

    card_number = ""
    if len(number) != 16:
        logger.error("Недопустимое количество символов")
        return "Error"
    for num in range(len(number)):
        if number[num].isalpha():
            logger.error("Нужны численные значения")
            return "Error"
    else:
        for num in range(len(number)):
            if number[num].isalpha() or number[num] == " ":
                pass
            else:
                card_number += number[num]
        correct_number = card_number[0:7] + card_number[7:14] + card_number[14:19]
        number_mask = (
            correct_number[0:4] + " " + correct_number[4:6] + "**" + " " + "****" + " " + correct_number[12:16]
        )
        logger.info(f"функция закончила выполнение со значениямм {number_mask}")
        return number_mask
def get_mask_account(number: str) -> str:

    if len(number) < 20:
        logger.error("Символов меньше чем 20")
        return "Error"
    for num in range(len(number)):
        if number[num].isalpha():
            logger.error("Нужны численные значения")
            return "Error"
    else:
        number_mask = "**" + number[-4:]
        logger.info(f"функция закончила выполнение со значениями {number_mask}")
        return number_mask
# get_mask_account("14234354436141345")
# get_mask_card_number("112222333344455")