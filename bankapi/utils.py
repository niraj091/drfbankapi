from bankapi.models import Bank


def get_object_by_bank_name(bank_name,city):
    bank_details=Bank.objects.filter(bank_name=bank_name,city=city)
    if bank_details:
        return bank_details
    return None
            
def get_object_by_ifsc(ifsc):
    try:
        bank_details=Bank.objects.get(ifsc=ifsc)
    except Bank.DoesNotExist:
        bank_details=None
    return bank_details