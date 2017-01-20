from django.shortcuts import render
from django.views import View


def index(request):
    return render (request, 'index.html')

class Orders(View):
    data = {
        'orders': [
            {'title': 'Ученик 1', 'id': 1},
            {'title': 'Ученик 2', 'id': 2},
            {'title': 'Ученик 3', 'id': 3},
            {'title': 'Ученик 4', 'id': 4},
            {'title': 'Ученик 5', 'id': 5}
        ]
    }

    def get(self,request):
        return render(request, 'orders.html', Orders.data)

class OrderOb(Orders):
    id = 0
    title = ''
    data = {
        'orders': {
            'id': id,
            'title': title
        }
    }

    def get(self, request, id):
        self.id = id
        self.title = Orders.data['orders'][int(id)-1]['title']
        self.data['orders']['id'] = self.id
        self.data['orders']['title'] = self.title
        return render(request, 'order.html', self.data)