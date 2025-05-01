"""
Check for valid url.

This program accept user input.
validate the input for a specific url.

"""
domainNames = (".com", ".org", ".net", ".gov", ".edu", ".co.uk")
website_url = input("Enter website url: ")

if website_url.lower().startswith("https://"):
    if website_url.lower().endswith(domainNames):
        print(f"✔ {website_url.lower()} is secured!")
        print("You are safe to browser.🔒")
    else:
        print(f"Sorry😢 I could find your website domain!")
elif website_url.lower().startswith("http://"):
    if website_url.lower().endswith(domainNames):
        print(f"👹 {website_url.lower()} is Dangerous")
        print("You are vulnerable to attackers 🔓!!")
    else:
        print(f"invalid {website_url.lower()} url")