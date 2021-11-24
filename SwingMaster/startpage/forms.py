from django import forms
from signup.models import User
from agron2 import PasswordHasher, exceptoions

class LoginForm(forms.Form):
    user_id = froms.CharFeild(
        max_length=32,
        label='ID',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'login-input',
                'id' : 'id-input',
                'placeholder' : '내용을 입력해 주세요',
                'height' : '40px'
            }
        ),
        error_messages={'required' : '아이디를 입력해 주세요.'}
    )

    user_pw = forms.CharField(
        max_length=128,
        label='PW',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'login-input',
                'id' : 'passwd-input',
                'placeholder' : '내용을 입력해 주세요',
                'height' : '40px'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해 주세요.'}
    )

    field_order = [
        'user_id',
        'user_pw',
    ]

    def claen(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id', '')
        user_pw = cleaned_data.get('user_pw', '')

        if user_id == '':
            return self.add_error('user_id', '아이디를 다시 입력해 주세요.')
        elif user_pw == '':
            return self.add_error('user_pw', '비밀번호를 다시 입력해 주세요.')
        else:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                return self.add_error('user_id', '아이디가 존재하지 않습니다.')

            try:
                PasswordHasher().verify(user.user_pw, user_pw)
            except exceptoions.VerifyMismatchError:
                return self.add_error('user_pw', '비밀번호가 다릅니다.')

            self.login_session = user.user_id