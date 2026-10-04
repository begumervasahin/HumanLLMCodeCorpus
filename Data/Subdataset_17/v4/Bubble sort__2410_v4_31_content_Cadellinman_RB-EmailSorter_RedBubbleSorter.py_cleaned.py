import imaplib
def login_to_email(username, password):
    try:
        M = imaplib.IMAP4_SSL('imap.gmail.com')
        M.login(username, password)
        print("Logged in")
        return M
    except imaplib.IMAP4.error:
        print("Login failed")
        return None
def search_emails(M, sender):
    M.select("INBOX")
    typ, dataraw = M.search(None, f'(FROM "{sender}")')
    return dataraw[0].split()
def fetch_subject_and_store_email(M, num, destination_folder):
    M.store(num, '+X-GM-LABELS', destination_folder)
    M.store(num, '+FLAGS', '\\Deleted')
    typ, data = M.fetch(num, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    return data
def extract_amount(data):
    data = str([x[-1] for x in data])
    if "=28=C2=A3" in data:
        amount = data.split('=28=C2=A3')[-1].split('=')[0]
    elif "=28=E2=82=AC" in data:
        amount = float(data.split('=28=E2=82=AC')[-1].split('=')[0]) * 0.88
    else:
        amount = float(data.split('(US$')[-1].split(')')[0]) * 0.77
    return round(float(amount), 2)
def fetch_email_dates(M, num):
    typ, dates = M.fetch(num, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    dates = str([x[-1] for x in dates])
    date_parts = dates.split(' ')
    return date_parts[8] + ' ' + date_parts[9] + ' ' + date_parts[10].replace('\\r\\n', '')
def consolidate_amounts(listy, listdates):
    consolidated_listy = []
    consolidated_listdates = []
    rand = len(listy) - 1
    for i in range(rand):
        if listdates[i] == listdates[i + 1]:
            listy[i] = str(round(float(listy[i]) + float(listy[i + 1]), 2))
            listy[i + 1] = "0"
    for i in range(len(listy)):
        if listy[i] != "0" and listy[i] != "0.0":
            consolidated_listy.append(listy[i])
            consolidated_listdates.append(listdates[i])
    return consolidated_listy, consolidated_listdates
def main():
    username = 'youremailinhere'
    password = 'yourpasswordinhere'
    sender = 'congratulations@redbubble.com'
    destination_folder = 'yourdestinationfolder'
    M = login_to_email(username, password)
    if not M:
        return
    email_nums = search_emails(M, sender)
    amounts = []
    dates = []
    for num in email_nums:
        data = fetch_subject_and_store_email(M, num, destination_folder)
        amount = extract_amount(data)
        amounts.append(amount)
        date = fetch_email_dates(M, num)
        dates.append(date)
    consolidated_amounts, consolidated_dates = consolidate_amounts(amounts, dates)
    for date, amount in zip(consolidated_dates, consolidated_amounts):
        print(f"{date}: £{amount}")
    M.expunge()
    M.close()
    M.logout()
if __name__ == "__main__":
    main()