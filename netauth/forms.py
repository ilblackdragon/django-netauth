from django import forms
from django.utils.translation import ugettext as _

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

from netauth import settings
from netauth.models import NetID

class ExtraForm(forms.Form):

    username = forms.CharField(min_length=3, max_length=25, label="Display Name")

    def clean_username(self):
        try:
            User.objects.get( username = self.cleaned_data[ 'username' ] )
            raise forms.ValidationError(_(u'This username name is already taken'))
        except User.DoesNotExist:
            return self.cleaned_data['username']

    def save(self, request, identity, provider):
        user = User.objects.create(username=self.cleaned_data['username'], password=settings.UNUSABLE_PASSWORD)
        if settings.ACTIVATION_REQUIRED:
            user.is_active = False
        user.save()
        NetID.objects.get_or_create(identity=identity, provider=provider, defaults={'user': user})
        return user

