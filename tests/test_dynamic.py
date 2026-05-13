import json
from string import Template

from pydantic import ValidationError, create_model


def read_file(html_file):
    try:
        with open(html_file) as f:
            html_string = f.read()
    except Exception:
        raise ValueError("file is not valid")
    return html_string

def template_dynamic_var(html_string):
    template_obj = Template(html_string)
    dynamic_var_find = [
        match[1] or match[2]
        for match in template_obj.pattern.findall(template_obj.template)
        if match[1] or match[2]
    ]
    return dynamic_var_find

def DynamicModelFunc(fields):
    DynamicModel = create_model(
    'DynamicModel',
    **{field: (str, ...) for field in fields}   # all fields required str
)
    return DynamicModel

html_str=read_file(html_file="/Applications/Work/ezsnapps-projects/ezsn-notify-email/templates/invoice.html")
fields = template_dynamic_var(html_str)
print(fields)
dynamic_model = DynamicModelFunc(fields)
print(dynamic_model)

try:
    user_input={"customer_name":"Gayathri"}
    data=dynamic_model(**user_input)
    print(data.customer_name)
except ValidationError as e:
    errors = [{k: v for k, v in err.items() if k not in ("input", "url")} for err in e.errors()]
    print(json.dumps(errors, indent=2))

#print(data.id)
