from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shinobi
from .forms import ShinobiForm


@login_required
def home(request):
    context = {
        'shinobi': Shinobi.objects.all()
    }
    return render(request, 'blog/home.html', context)


@login_required
def create(request):
    shinobi_form = ShinobiForm(request.POST, request.FILES)

    if request.method == 'POST':
        if shinobi_form.is_valid():
            shinobi_form.save()

        return redirect('blog-home')

    context = {
        'title': 'Tambah data'
    }

    return render(request, 'blog/create.html', context)


@login_required
def delete(request, pk):
    Shinobi.objects.filter(id=pk).delete()
    return redirect('blog-home')


# class PostDetailView(DetailView):
#     model = Shinobi

@login_required
def update(request, pk):
    post = get_object_or_404(Shinobi, id=pk)
    form = ShinobiForm(instance=post)
    if request.method == "POST":
        form = ShinobiForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-home')

    context = {
        'title': 'update data',
        'post': post,
    }

    return render(request, 'blog/update.html', context)


@login_required
def detail(request, pk):
    post = get_object_or_404(Shinobi, id=pk)
    context = {
        'title': 'detail data',
        'post': post,
    }

    return render(request, 'blog/detail.html', context)
