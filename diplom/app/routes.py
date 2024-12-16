from flask import render_template, request, redirect, url_for, session
from app import app
from app.classes.Cart import Cart
from app.classes.models.Admin import Admin
from app.classes.models.Product import Product
from app.classes.models.Order import Order
from app.classes.models.OrderStatus import OrderStatus
from app.decorators import decorator_login
from os import getenv


@app.route('/')
@app.route('/index/')
@app.route('/catalog/')
def show_catalog_page():
    catalog_list = Product.get_list(
        ['is_active = True'],
        ['id DESC'],

        100
    )
    return render_template("public/catalog.html", list=catalog_list)


@app.route('/catalog/<alias>/')
def show_category_page():
    return "Это Категория"


@app.route('/product/<alias>/')
def show_product_page(alias):
    product = Product.get_by_key('alias', alias)
    return render_template("public/product.html", product=product)


@app.route('/cart/')
def show_cart_page():
    content = Cart.get_instance().get_cart_info()
    return render_template("public/cart.html", content=content)


@app.route('/cart/add/', methods=['GET', 'POST'])
def show_cart_add_page():
    if request.method == 'POST':
        print(Cart.get_instance().add(request.form['product_id']))
    return "Корзина обновлена"


@app.route('/cart/delete/', methods=['POST'])
def show_cart_delete_page():
    if request.method == 'POST':
        Cart.get_instance().delete(request.form['product_id'])
    return redirect("/cart/")


@app.route('/checkout/', methods=["GET", "POST"])
def show_checkout_page():
    order = Order()

    if request.method == 'POST':
        order.set_attributes(dict(request.form))
        if order.validate():
            order.save_to_db()
            return redirect("/thanks/")

    cart = Cart.get_instance().get_cart_info()

    if len(cart['list']) == 0:
        return redirect("/cart/")

    return render_template("public/checkout.html", order=order, cart=cart)


@app.route('/thanks/')
def show_thanks_page():
    return render_template("public/thanks.html")


@app.route('/admin/login/', methods=['GET', 'POST'])
def show_admin_login_page():
    if request.method == 'POST':
        admin = Admin.get_admin_by_credentials(
            request.form['login'],
            request.form['password'],
        )

        if admin is not None and admin.authorize():
            return redirect('/admin/')

    return render_template("admin/login.html")


@app.route('/admin/logout/')
def show_logout():
    Admin.logout()
    return redirect("/admin/login")


@app.route('/admin/')
@app.route('/admin/<item_type>/list/')
@decorator_login
def show_admin_list_page(item_type='product'):
    match item_type:
        case 'product':
            products = Product.get_list([], ['id DESC'])
            return render_template('admin/list_product.html', list=products)
        case 'order':
            orders = Order.get_list([], ['id DESC'])
            return render_template('admin/list_order.html', list=orders)
        case _:
            return render_template('404.html'), 404


@decorator_login
@app.route('/admin/<item_type>/edit/<item_id>/', methods=['GET', 'POST'])
@app.route('/admin/<item_type>/add/', methods=['GET', 'POST'])
@decorator_login
def show_admin_edit_page(item_type, item_id=None):
    data = None

    if request.method == 'POST':
        data = dict(request.form)
    match item_type:
        case 'product':
            if item_id is not None:
                product = Product.get_by_key('id', item_id)
            else:
                product = Product()

            if data is not None:
                if "is_active" not in data:
                    data.update({"is_active": "0"})

                product.set_attributes(data)

                if product.validate():
                    product.save_to_db()
                    return redirect(f'/admin/{item_type}/edit/{product.id}/')
            return render_template('admin/edit_product.html', product=product)
        case 'order':
            if item_id is None:
                return redirect("/admin/order/list/")

            order = Order.get_by_key('id', item_id)
            status_list = OrderStatus.get_list([], ['id ASC'], 100)

            if data is not None:
                order.set_attributes(data)

                if order.validate():
                    order.save_to_db()
                    return redirect(f'/admin/{item_type}/edit/{order.id}/')

            return render_template('admin/edit_order.html', order=order, status_list=status_list)
        case _:
            return render_template('404.html'), 404


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
