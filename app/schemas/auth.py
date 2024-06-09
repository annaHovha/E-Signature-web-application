from marshmallow import Schema, fields


class RegisterSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)

class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class AccessTokenSchema(Schema):
    access_token = fields.Str()
    refresh_token = fields.Str()
