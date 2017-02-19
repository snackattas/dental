from django.contrib import admin
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.utils.crypto import get_random_string

from authtools.admin import NamedUserAdmin
from authtools.forms import UserCreationForm

from agents.models import Facility, Agent

User = get_user_model()


class AgentCreationForm(UserCreationForm):
    """
    An AgentCreationForm with optional password inputs.
    """
    facility = forms.ModelChoiceField(
        queryset=Facility.objects.all(),
        required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = super(AgentCreationForm, self).clean_password2()
        if bool(password1) ^ bool(password2):
            raise forms.ValidationError("Fill out both fields")
        return password2


class UserAdmin(NamedUserAdmin):
    """
    A UserAdmin that sends a password-reset email when creating a new user,
    unless a password was entered.
    """
    add_form = AgentCreationForm
    add_fieldsets = (
        (None, {
            'description': (
                "Enter the new user's name and email address and click save."
                " The user will be emailed a link allowing them to login to"
                " the site and set their password."
            ),
            'fields': ('email', 'name', 'facility'),
        }),
        ('Password', {
            'description': "Optionally, you may set the user's password here.",
            'fields': ('password1', 'password2'),
            'classes': ('collapse', 'collapse-closed'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            # Django's PasswordResetForm won't let us reset an unusable
            # password. We set it above super() so we don't have to save twice.
            obj.set_password(get_random_string())
            reset_password = True
            import pdb;pdb.set_trace()
        else:
            reset_password = False

        user = super(UserAdmin, self).save_model(request, obj, form, change)
        import pdb;pdb.set_trace()
        # Create the Agent now
        facility = form.cleaned_data.get("facility")
        user = User.objects.get(email=form.cleaned_data.get("email"))
        Agent(user=user, facility=facility).save()
        import pdb;pdb.set_trace()
        if reset_password:
            import pdb;pdb.set_trace()
            reset_form = PasswordResetForm({'email': obj.email})
            assert reset_form.is_valid()
            if reset_password:
                reset_form = PasswordResetForm({'email': obj.email})
                assert reset_form.is_valid()
                reset_form.save(
                    request=request,
                    use_https=request.is_secure(),
                    subject_template_name='account_creation_subject.txt',
                    email_template_name='account_creation_email.html',)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
