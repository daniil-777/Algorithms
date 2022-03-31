def get_nearest_happy_ticket(current_ticket: str) -> str:

    """
    :type current_ticket: object
    :param current_ticket: ticket number with 6 digits
    :return: nearest happy ticket number with 6 digits
    """
    ticket = current_ticket
    final = current_ticket
    ticket1 = ticket
    ticket2 = ticket
    if check(current_ticket) == 1:
        return final
    else:
        if int(ticket[0]) == 0:
            j = 1
            while int(ticket[j]) == 0:
                j = j + 1
            if j >= 3:
                return '000000'
            ticket1 = ticket[j:]
            print(ticket1)
            ticket2 = ticket[j:]
        while True:
            ticket1 = str(int(ticket1) + 1)
            if check(add(ticket1)) == 1:
                final = add(ticket1)
                break
            ticket2 = str(int(ticket2) - 1)
            if check(add(ticket2)) == 1:
                final = add(ticket2)
                break
        return final


def check(ticket: str) -> int:
    if len(ticket) == 6:
        if ((int(ticket[0]) + int(ticket[1]) + int(ticket[2]))
                == (int(ticket[3]) + int(ticket[4]) + int(ticket[5]))):
            return 1
        else:
            return 0
    else:
        return 0


def add(ticket: str) ->str:
    if len(ticket) < 6:
        list = []
        for i in range(0, 6 - len(ticket)):
            list.append('0')
        string = ''.join(list)
        return string + ticket
    return ticket
