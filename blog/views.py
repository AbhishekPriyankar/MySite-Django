from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import ArticleForm  # Import ArticleForm


#This view handles the form submission, validating and saving the data to the database if valid, and then redirects to t#he list view.
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'article_create.html', {'form': form})


#The article_detail view and template display the full content of a selected article. get_object_or_404 ensures that an #error is shown if an article with the given ID doesn’t exist.
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})

def article_list(request):
    articles = Article.objects.all()  # Fetch all articles from the database
    return render(request, 'article_list.html', {'articles': articles})

