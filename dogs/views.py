from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from dogs.models import Dog



class DogListView(ListView):
    """Контроллер автоматически создает страницу со списком всех собак.
    1. Выполняет запрос к базе данных: Dog.objects.all().
    2. Сохраняет весь список собак в переменную object_list (и дублирует в dog_list).
    3. Передает эту переменную в HTML-шаблон (по умолчанию dogs/dog_list.html) для вывода на экран."""
    model = Dog



class DogDetailView(DetailView):
    """
    DogDetailView открывает профиль одной конкретной собаки (её персональную карточку).
    Он делает следующее:
    1. Берет ID собаки из ссылки (например, /dogs/5/).
    2. Находит эту собаку в базе данных (если её нет — покажет ошибку 404).
    3. Передает все её данные в HTML-шаблон (dog_detail.html) для вывода на экран.
    """
    model = Dog

    def get_object(self, queryset = None):
        """ метод get_object контроллера (класса представления), отвечает за подсчёт просмотров страницы
            (счётчик кликов по карточке объекта)."""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object



class DogCreateView(CreateView):
    """контроллер автоматизирует создание новой записи в базе данных через HTML-форму."""
    model = Dog
    fields = ("name", "breed", "photo", "date_born")
    success_url = reverse_lazy('dogs:dogs_list')



class DogUpdateView(UpdateView):
    """Контроллер автоматизирует изменение (редактирование) данных уже существующей собаки в базе данных."""
    model = Dog
    fields = ("name", "breed", "photo", "date_born")
    success_url = reverse_lazy('dogs:dogs_list')

    def get_success_url(self):
        """метод динамически вычисляет адрес страницы профиля конкретной собаки и
           перенаправляет пользователя туда сразу после успешного редактирования."""
        return reverse('dogs:dogs_detail', args=[self.kwargs.get('pk')])



class DogDeleteView(DeleteView):
    """Контроллер автоматизирует удаление существующей записи о собаке из базы данных."""
    model = Dog
    success_url = reverse_lazy('dogs:dogs_list')