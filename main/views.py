from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama': 'Mirfak Naufal Pratama Putra',
        'npm': '2306244961',
        'kelas': 'PBP A',
    }

    return render(request, "main.html", context)