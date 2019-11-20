from django.shortcuts import get_object_or_404
from webdes.models import Webdes


def cart_contents(request):
    """
    Display cart content in every page
    when user is log in can add webdes to the cart
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    webdes_count = 0

    for id, quantity in cart.items():
        webdes = get_object_or_404(Webdes, pk=id)
        total += quantity * webdes.price
        webdes_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'webdes': webdes})

    return {'cart_items': cart_items, 'total': total, 'webdes_count': webdes_count}
