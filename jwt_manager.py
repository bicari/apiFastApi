from jwt import encode, decode

def create_token(data: dict):
    token: str = (encode(payload=data, key="bibi3103", algorithm="HS256"))
    return token

def validate_token(token : str)-> dict:
    TOKEN: dict =decode(token, key="bibi3103", algorithms=['HS256'])
    return TOKEN

