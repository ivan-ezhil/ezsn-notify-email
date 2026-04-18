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
