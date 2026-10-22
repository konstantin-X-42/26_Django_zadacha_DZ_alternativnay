from django.forms import ModelForm

from dogs.models import Dog, Parent


class DogForm(ModelForm):
    class Meta:
        model = Dog
        exclude = ("views_counter",)          # exclude - скрывает поле счётчик просмотров

class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"         # значение "__all__" - все поля форм