import xlrd


def load_greetings(file_name):
    wb = xlrd.open_workbook(file_name)
    sh = wb.sheet_by_index(0)
    greets = sh.get_rows()
    contacts = {}
    greet_idx = 0
    for each_greet in greets:
        greet_idx += 1
        contact_name = each_greet[0].value
        if contact_name not in contacts:
            contacts[contact_name] = []
        contacts[contact_name].append((greet_idx, each_greet[1].value))
    for each_contact in contacts:
        contacts[each_contact].sort()
    return contacts
