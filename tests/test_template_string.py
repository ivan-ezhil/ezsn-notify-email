import re
from string import Template

# assume these are imported from your code
# from your_module import clean_username_bs4, find_missing_inputs

html_string = None
with open("templates/invoice.html") as f:
    html_string = f.read()


t = Template(html_string)


user_input = {
    "customer_name": "$Nila,/n<b><script>alert('hi')</script>",
    "invoice_reference": "Amazon",
}


def clean_username_bs4(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # remove script/style blocks with content
    text = re.sub(r"<script.*?>.*?</script>", "", text, flags=re.DOTALL | re.IGNORECASE)

    # remove all remaining HTML tags
    text = re.sub(r"<.*?>", "", text)

    return text


print(clean_username_bs4(""))


def find_missing_inputs(template_obj, user_input):
    variables = [
        match[1] or match[2]
        for match in template_obj.pattern.findall(template_obj.template)
        if match[1] or match[2]
    ]

    missing_input = []

    for key in variables:
        if key not in user_input:
            missing_input.append(key)

    return missing_input


class TestInvoiceTemplate:
    # Sample template

    # 1. Valid input test
    def test_valid_input_rendering():
        TEMPLATE = Template("Hello $customer_name, Invoice: $invoice_reference")

        user_input = {"customer_name": "Gayathri", "invoice_reference": "Amazon"}

        result = TEMPLATE.substitute(user_input)

        assert "Gayathri" in result
        assert "Amazon" in result

    # 2. HTML tags should be removed
    def test_remove_html_tags():
        dirty_input = "<b>Gayathri</b>"

        cleaned = clean_username_bs4(dirty_input)

        assert "<b>" not in cleaned
        assert "</b>" not in cleaned

    # 3. Script tags should be removed (security)
    def test_remove_script_tags():
        dirty_input = "<script>alert('hi')</script>"

        cleaned = clean_username_bs4(dirty_input)

        assert "script" not in cleaned.lower()

    # 4. Special characters removed
    def test_remove_special_characters():
        dirty_input = "!@#$%^&*()Gayathri"

        cleaned = clean_username_bs4(dirty_input)

        assert "!" not in cleaned
        assert "@" not in cleaned
        assert "Gayathri" in cleaned

    # 5. Trim whitespaces
    def test_trim_whitespace():
        dirty_input = "   Gayathri   "

        cleaned = clean_username_bs4(dirty_input)

        assert cleaned == "Gayathri"

    # 6. Handle newline and tabs
    def test_newline_and_tabs():
        dirty_input = "Gayathri\nMA\tTest"

        cleaned = clean_username_bs4(dirty_input)

        assert "\n" not in cleaned
        assert "\t" not in cleaned
        assert cleaned == "GayathriMATest"

    # 7. Empty input handling
    def test_empty_input():
        cleaned = clean_username_bs4("")

        assert cleaned == ""

    # 8. Only spaces input
    def test_only_spaces():
        cleaned = clean_username_bs4("     ")

        assert cleaned == ""

    # 9. Missing template variables
    def test_missing_variables():
        html = "Hello $customer_name, Date: $date"
        t = Template(html)

        user_input = {"customer_name": "Gayathri"}

        missing_input = find_missing_inputs(t, user_input)

        assert "date" in missing_input

    # 10. All variables present
    def test_all_variables_present():
        html = "Hello $customer_name, Invoice: $invoice_reference"
        t = Template(html)

        user_input = {"customer_name": "Gayathri", "invoice_reference": "Amazon"}

        missing_input = find_missing_inputs(t, user_input)

        assert missing_input == []

    # 11. Safe substitution (no crash)
    def test_safe_substitute():
        html = "Hello $customer_name, Date: $date"
        t = Template(html)

        user_input = {"customer_name": "Gayathri"}

        result = t.safe_substitute(user_input)

        assert "$date" in result  # not replaced but no crash

    # 12. Malicious combined input
    def test_malicious_input_cleaning():
        dirty_input = "$Nila,/n<b><script>alert('hi')</script>"

        cleaned = clean_username_bs4(dirty_input)

        assert "<" not in cleaned
        assert ">" not in cleaned
        assert "script" not in cleaned.lower()


# def clean_username_bs4(html_text):
#     soup = BeautifulSoup(html_text, "html.parser")
#     # Decompose removes the tag AND its content
#     for tag in soup.find_all(True):  # Finds all tags
#         tag.decompose()
#     clean_text = soup.get_text().replace("\n", "").replace("\t", "")
#     clean_text = soup.get_text(strip=True).translate(
#         str.maketrans("", "", "!@#$%^&*()_+-=[]{}|;:,.<>?/ ")
#     )
#     return clean_text.strip()


# remove the special char
# for clean_input in user_input.values():
#     print(clean_username_bs4(clean_input))

# find the missing user input

# missing_input = []
# def find_missing_inputs():
#     for key in variables:
#         if key in user_input:
#             print("avaliable--->", key)
#         else:
#             print("not avaliable---->", key)
#             missing_input.append(key)
#     return missing_input

# s=t.safe_substitute(user_input)
# s = t.substitute(user_input)
# print(s)

# with open("templates/substitute.html", "w") as f:
#    f.write(s)


# def test_special_char():
#     user_input = {
#     "customer_name": "!@#$%^&*()",
#     "invoice_reference": "Amazon"}
#     s = t.substitute(user_input)
#     print(s)
