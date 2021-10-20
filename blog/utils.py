from .models import DFrame
def get_field_columns(field):
    return list(DFrame.objects.distinct().values_list(field, flat = True))