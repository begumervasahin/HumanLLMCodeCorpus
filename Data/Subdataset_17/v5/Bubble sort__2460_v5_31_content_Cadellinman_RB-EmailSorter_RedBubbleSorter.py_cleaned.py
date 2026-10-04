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
    typ, data = M.search(None, f'(FROM "{sender}")')
    return data[0].split()
def fetch_subject_and_store_email(M, num, destination_folder):
    M.store(num, '+X-GM-LABELS', destination_folder)
    M.store(num, '+FLAGS', '\\Deleted')
    typ, data = M.fetch(num, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
    return data
def extract_amount(data):
    data_str = str([x[-1] for x in data])
    if "=28=C2=A3" in data_str:
        amount = data_str.split('=28=C2=A3')[-1].split('=')[0]
    elif "=28=E2=82=AC" in data_str:
        amount = float(data_str.split('=28=E2=82=AC')[-1].split('=')[0]) * 0.88
    else:
        amount = float(data_str.split('(US$')[-1].split(')')[0]) * 0.77
    return round(float(amount), 2)
def fetch_email_dates(M, num):
    typ, dates = M.fetch(num, '(BODY[HEADER.FIELDS (RECEIVED DATE)])')
    dates_str = str([x[-1] for x in dates])
    date_parts = dates_str.split(' ')
    return f"{date_parts[8]} {date_parts[9]} {date_parts[10].replace('\\r\\n', '')}"
def consolidate_amounts(amounts, dates):
    consolidated_amounts = []
    consolidated_dates = []
    for i in range(len(amounts) - 1):
        if dates[i] == dates[i + 1]:
            amounts[i] = str(round(float(amounts[i]) + float(amounts[i + 1]), 2))
            amounts[i + 1] = "0"
    for i in range(len(amounts)):
        if amounts[i] != "0" and amounts[i] != "0.0":
            consolidated_amounts.append(amounts[i])
            consolidated_dates.append(dates[i])
    return consolidated_amounts, consolidated_dates
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