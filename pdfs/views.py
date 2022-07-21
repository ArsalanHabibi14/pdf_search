from asyncore import read
from django.views.generic import ListView, DetailView
from .models import Books
import PyPDF2
import uuid
from django.http import FileResponse
import os


def show_pdf(request, filepath):
    filepath = os.path.join('media', filepath)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

class BookListView(ListView):
    queryset = Books.objects.all()
    template_name = 'files_list.html'
    
class BookDetailView(DetailView):
    queryset = Books.objects.all()
    template_name = 'file_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['data']  = []
        get_book = Books.objects.get(id=self.kwargs.get('pk'))
        key = self.request.GET.get('key')
        file_name = os.path.basename(get_book.file.url)
        my_file = open(f"{get_book.file.path}", "rb")
        reader = PyPDF2.PdfFileReader(my_file)
        full_pages = reader.numPages
        if key:
            for s in range(0, full_pages):
                pdf_page = reader.getPage(s)
                text_pdf = pdf_page.extract_text()
                get_words = text_pdf.split(" ")
                for c in get_words:
                    if str(key).lower() in c.lower():
                        context['data'].append(c)
        
        return context
