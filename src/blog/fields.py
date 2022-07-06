from django.db.models import CharField

class NonStrippingCharField(CharField):
    """
    A CharField that does not strip whitespace at the beginning/end of
    it's value.

    I added this for ease of searching with split in tags,
    because Django would strip it automatically but it shouldn't be.
    """

    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingCharField, self).formfield(**kwargs)