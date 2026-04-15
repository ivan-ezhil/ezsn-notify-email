import re
from string import Template


class EmailTemplate:
    def __init__(self, html_file, user_input):
        self.html_string = None
        self.html_file = html_file
        self.user_input = user_input
        self.dynamic_var_find = []
        self.missing_input = []
        self.template_obj = []

    def read_file(self):
        try:
            with open(self.html_file) as f:
                self.html_string = f.read()
        except Exception:
            raise ValueError("file is not valid")
        return self.html_string

    def template_dynamic_var(self):
        template_obj = Template(self.html_string)
        self.dynamic_var_find = [
            match[1] or match[2]
            for match in template_obj.pattern.findall(template_obj.template)
            if match[1] or match[2]
        ]
        return self.dynamic_var_find

    def find_missing_input(self):
        for key in self.dynamic_var_find:
            if key not in user_input:
                self.missing_input.append(key)
        return self.missing_input


html_file = "templates/invoice.html"
user_input = {
    "customer_name": "$Nila,/n<b><script>alert('hi')</script>",
    "invoice_reference": "Amazon",
}

et = EmailTemplate(html_file, user_input)
et.read_file()
print(et.template_dynamic_var())
print(et.find_missing_input())


def clean_username_bs4(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # remove script/style blocks with content
    text = re.sub(r"<script.*?>.*?</script>", "", text, flags=re.DOTALL | re.IGNORECASE)

    # remove all remaining HTML tags
    text = re.sub(r"<.*?>", "", text)

    return text


# class TestInvoiceTemplate:
#     # Sample template

#     # 1. Valid input test
#     def test_valid_input_rendering():
#         TEMPLATE = Template("Hello $customer_name, Invoice: $invoice_reference")

#         user_input = {"customer_name": "Gayathri", "invoice_reference": "Amazon"}

#         result = TEMPLATE.substitute(user_input)

#         assert "Gayathri" in result
#         assert "Amazon" in result

#     # 2. HTML tags should be removed
#     def test_remove_html_tags():
#         dirty_input = "<b>Gayathri</b>"

#         cleaned = clean_username_bs4(dirty_input)

#         assert "<b>" not in cleaned
#         assert "</b>" not in cleaned

#     # 3. Script tags should be removed (security)
#     def test_remove_script_tags():
#         dirty_input = "<script>alert('hi')</script>"

#         cleaned = clean_username_bs4(dirty_input)

#         assert "script" not in cleaned.lower()

#     # 4. Special characters removed
#     def test_remove_special_characters():
#         dirty_input = "!@#$%^&*()Gayathri"

#         cleaned = clean_username_bs4(dirty_input)

#         assert "!" not in cleaned
#         assert "@" not in cleaned
#         assert "Gayathri" in cleaned

#     # 5. Trim whitespaces
#     def test_trim_whitespace():
#         dirty_input = "   Gayathri   "

#         cleaned = clean_username_bs4(dirty_input)

#         assert cleaned == "Gayathri"

#     # 6. Handle newline and tabs
#     def test_newline_and_tabs():
#         dirty_input = "Gayathri\nMA\tTest"

#         cleaned = clean_username_bs4(dirty_input)

#         assert "\n" not in cleaned
#         assert "\t" not in cleaned
#         assert cleaned == "GayathriMATest"

#     # 7. Empty input handling
#     def test_empty_input():
#         cleaned = clean_username_bs4("")

#         assert cleaned == ""

#     # 8. Only spaces input
#     def test_only_spaces():
#         cleaned = clean_username_bs4("     ")

#         assert cleaned == ""

#     # 9. Missing template variables
#     def test_missing_variables():
#         html = "Hello $customer_name, Date: $date"
#         t = Template(html)

#         user_input = {"customer_name": "Gayathri"}

#         missing_input = find_missing_inputs(t, user_input)

#         assert "date" in missing_input

#     # 10. All variables present
#     def test_all_variables_present():
#         html = "Hello $customer_name, Invoice: $invoice_reference"
#         t = Template(html)

#         user_input = {"customer_name": "Gayathri", "invoice_reference": "Amazon"}

#         missing_input = find_missing_inputs(t, user_input)

#         assert missing_input == []

#     # 11. Safe substitution (no crash)
#     def test_safe_substitute():
#         html = "Hello $customer_name, Date: $date"
#         t = Template(html)

#         user_input = {"customer_name": "Gayathri"}

#         result = t.safe_substitute(user_input)

#         assert "$date" in result  # not replaced but no crash

#     # 12. Malicious combined input
#     def test_malicious_input_cleaning():
#         dirty_input = "$Nila,/n<b><script>alert('hi')</script>"

#         cleaned = clean_username_bs4(dirty_input)

#         assert "<" not in cleaned
#         assert ">" not in cleaned
#         assert "script" not in cleaned.lower()
