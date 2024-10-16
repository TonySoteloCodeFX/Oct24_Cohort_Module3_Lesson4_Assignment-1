import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

print("-" * 50)
for email in emails:
    if not re.search(r"@exclude\.com$", email):
        print(email)
        print("-" * 50)