from pydantic import create_model

fields = ['name', 'id']

DynamicModel = create_model(
    'DynamicModel',
    **{field: (str, ...) for field in fields}   # all fields required str
)


data = DynamicModel(name="Gayathri", id="25")

#print(data.name)
#print(data.id)
