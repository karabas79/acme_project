from django.shortcuts import render

from .forms import BirthdayForm
from .utils import calculate_birthday_countdown


def birthday(request):
    form = BirthdayForm(request.GET or None)
    birthday_countdown = None
    context = {'form': form}
    if form.is_valid():
        # ...вызовем функцию подсчёта дней:
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )

    context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context=context)
