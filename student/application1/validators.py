from django.forms import ValidationError

def validate_name(name): 
    if len(name)<3:
        raise ValidationError('Name should have atleast 3 characters')
    for i in name:
        if not('A'<=i<='Z' or 'a'<=i<='z' or i==' ',i=='.'):
            raise ValidationError('Name cannot have special char or number')


def validate_phone(phone_no):
    if len(str(phone_no))!=10:
        raise ValidationError('Phone number must have 10 digits')
    if str(phone_no)[0] not in ['6','7','8','9']:
        raise ValidationError('Phone Number not Starts with 0,1,2,3,4,5')
    
def validate_marks(marks):
    if not (0 <= marks <= 100):
        raise ValidationError('Marks must be between 0 and 100')


def validate_username(username):
    if len(username)<=5:
        raise ValidationError('Username must have at least 6 characters')
    
    first_char=username[0]
    if not ('A'<=first_char<='Z' or 'a'<=first_char<='z'):
        raise ValidationError('Must be start a character')
    
    for i in username:
        if not ('A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9'):
            raise ValidationError('No special characters are allowed')

def validate_password(password):
    if len(password)<=5:
        raise ValidationError('Password must have at least 6 characters')

