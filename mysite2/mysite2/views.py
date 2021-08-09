from django.shortcuts import render


def test_img(request):

    return render(request, 'test_img.html')