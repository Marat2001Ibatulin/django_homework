from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    book_objects = Book.objects.all()
    context = {'books':book_objects}
    return render(request, template, context)

def p_date(request, pub_date):
    book_objects = list(Book.objects.all().order_by('pub_date'))
    print(f'URL: {pub_date}')
    page_number = 1
    for i, book in enumerate(book_objects, start=1):
        if pub_date == str(book.pub_date):
            page_number = i
            break

    prev_date = None
    next_date = None

    if page_number > 1:
        prev_date = book_objects[page_number - 2].pub_date.strftime('%Y-%m-%d')

    if page_number < len(book_objects):
        next_date = book_objects[page_number].pub_date.strftime('%Y-%m-%d')

    paginator = Paginator(book_objects, 1)
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'prev_date': prev_date,
        'next_date': next_date,
}

    return render(request, 'books/page.html', context)

