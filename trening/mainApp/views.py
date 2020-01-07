from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homepage.html')


def contacts(request):
    return render(request, 'mainApp/contacts.html',
    {'contact':[
        'Контактный email:  mikhin.n@sch2009.net',
        'Контактный номер:  8-(999)-840-31-02'
    ]}
    )


def docs(request):
    return render(request, 'mainApp/docs.html')

