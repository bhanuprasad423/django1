from django.forms import ValidationError

def validate_name(name):
    if len(name) < 3:
            raise ValidationError('Name Should have Atlease 3 characters')
    for i in name:
            if not('A'<=i<='Z' or 'a'<=i<='z' or i==' ' or i=='.'):
                raise ValidationError('Name cannot have special char or number')
    return name

def validate_phone_no(phone_no):

        if len(str(phone_no)) != 10:
            raise ValidationError('Phone Number must have 10 digits')
            
        if str(phone_no)[0] not in ['6','7','8','9']:
            raise ValidationError('Phone Number not Starts with 0,1,2,3,4,5')
        

def validate_marks(marks):
    if not (0 <= marks <= 100):
        raise ValidationError('Marks must be between 0 and 100')
