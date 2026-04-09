from string import Template

from bs4 import BeautifulSoup

html_string = None
with open("templates/invoice.html") as f:
    html_string = f.read()


t = Template(html_string)

variables = [
    match[1] or match[2]
    for match in t.pattern.findall(t.template)
    if match[1] or match[2]
]


user_input = {
    "customer_name": "$Nila,/n<b><script>alert('hi')</script>",
    "invoice_reference": "Amazon",
}

print(user_input['customer_name'])





def clean_username_bs4(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    # Decompose removes the tag AND its content
    for tag in soup.find_all(True):  # Finds all tags
        tag.decompose()
    clean_text =soup.get_text(strip=True).translate(str.maketrans('', '', '!@#$%^&*()_+-=[]{}|;:,.<>?/ '))
    return clean_text

# remove the special char
for clean_input in user_input.values():
    print(clean_username_bs4(clean_input))

# find the missing user input

missing_input=[]

for key in variables:
        if key in user_input:
            print("avaliable--->",key)
        else:
            print("not avaliable---->",key)
            missing_input.append(key)


print(missing_input)


# s=t.safe_substitute(user_input)
#s = t.substitute(user_input)
#print(s)

#with open("templates/substitute.html", "w") as f:
#    f.write(s)
