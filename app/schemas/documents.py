from marshmallow import Schema,fields


class SomeTemplateSchema(Schema):
    email = fields.Email(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    callback_url = fields.Str(required=True)
    description = fields.Str(required=True)
