import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
from datetime import date

current_date = date.today()
# need to install PIL(pillow)
# pip install pillow

window = tk.Tk()
window.minsize(1100, 775)

stock = {
    '01': {"category": "Perfect Grade", "name": "GUNDAM RAISER", "price": 315.00},
    '02': {"category": "Perfect Grade", "name": "Gundam SEED Astray", "price": 320.00},
    '03': {"category": "Perfect Grade", "name": "Wing Gundam", "price": 350.00},
    '04': {"category": "Perfect Grade", "name": "Freedom Gundam", "price": 410.00},
    '05': {"category": "Real Grade", "name": "RG GoldyMarg", "price": 52.00},
    '06': {"category": "Real Grade", "name": "RG Gao Gai Gar", "price": 78.00},
    '07': {"category": "Real Grade", "name": "God Gundam", "price": 58.00},
    '08': {"category": "Real Grade", "name": "Wing Gundam", "price": 38.00},
    '09': {"category": "Master Grade", "name": "Eclipse Gundam", "price": 195.00},
    '10': {"category": "Master Grade", "name": "Full Saber", "price": 72.00},
    '11': {"category": "Master Grade", "name": "Unicorn Gundam", "price": 64.00},
    '12': {"category": "Master Grade", "name": "Gundam Dynames", "price": 56.00},
    '13': {"category": "Mecha Girl", "name": "Messiah Ranka Lee", "price": 95.00},
    '14': {"category": "Mecha Girl", "name": "Ganesa", "price": 20.00},
    '15': {"category": "Mecha Girl", "name": "Arcanadea Lumitea", "price": 75.00},
    '16': {"category": "Mecha Girl", "name": "Tsubasa Kazanari", "price": 90.00},
    '17': {"category": "Motorized", "name": "Little Ryan", "price": 30.00},
    '18': {"category": "Motorized", "name": "Elephant Racer", "price": 17.00},
    '19': {"category": "Motorized", "name": "Zoids Stylaser", "price": 148.00},
    '20': {"category": "Motorized", "name": "Cannon Bull", "price": 35.00},
}
membership = {
    1: {'name': 'Gold', 'icons': 'Gold_member.png', 'val': 'Gold_3_Rank.png', 'percentage': 0.15},
    2: {'name': 'Silver', 'icons': 'Silver_member.png', 'val': 'Silver_3_Rank.png', 'percentage': 0.10},
    3: {'name': 'Bronze', 'icons': 'Bronze_member.png', 'val': 'Bronze_3_Rank.png', 'percentage': 0.05},
    4: {'name': 'No!', 'icons': 'No_member.png', 'val': '0.png', 'percentage': 0.25}
}
emoji_images = [
    ImageTk.PhotoImage(Image.open("pile_of_gems.png").resize((100, 100))),
    ImageTk.PhotoImage(Image.open("diamond.png").resize((100, 100))),
    ImageTk.PhotoImage(Image.open("money_bag.png").resize((100, 100))),
    ImageTk.PhotoImage(Image.open("cash.png").resize((100, 100))),
    ImageTk.PhotoImage(Image.open("coin.png").resize((100, 100))),
    ImageTk.PhotoImage(Image.open("flying_cash.png").resize((100, 100))),
    ImageTk.PhotoImage(Image.open("flying_cash.png").resize((100, 100))),
]
discount_days = [
    {"name": "Valentine's Day", "start_date": date(current_date.year, 2, 14),
     "end_date": date(current_date.year, 2, 14),
     'image': ImageTk.PhotoImage(Image.open("ValentineDay.png").resize((480, 250)))},
    {"name": "Great Singapore Sale", "start_date": date(current_date.year, 5, 31),
     "end_date": date(current_date.year, 7, 2),
     'image': ImageTk.PhotoImage(Image.open("GSS.png").resize((375, 250)))},
    {"name": "National Day Sales", "start_date": date(current_date.year, 8, 1),
     "end_date": date(current_date.year, 8, 31),
     'image': ImageTk.PhotoImage(Image.open("national_day_sale.png").resize((604, 250)))},
    {"name": "11.11 Sale", "start_date": date(current_date.year, 11, 11),
     "end_date": date(current_date.year, 11, 11),
     'image': ImageTk.PhotoImage(Image.open("sale_11.11.png").resize((417, 250)))},
    {"name": "Black Friday", "start_date": date(current_date.year, 11, 26),
     "end_date": date(current_date.year, 11, 26),
     'image': ImageTk.PhotoImage(Image.open("black_friday.jpg").resize((300, 250)))},
    {"name": "Christmas and Year-End Sales", "start_date": date(current_date.year, 12, 1),
     "end_date": date(current_date.year, 12, 31),
     'image': ImageTk.PhotoImage(Image.open("christmas.jpg").resize((375, 250)))}
]
rates = [
    ("80%", "0.01% (1 in 10,000)"),
    ("20%", "1% (1000 in 10,000)"),
    ("10%", "2% (2000 in 10,000)"),
    ("$5", "5% (500 in 10,000)"),
    ("$2", "10% (2000 in 10,000)"),
    ("$1", "20% (2000 in 10,000)"),
]
frames_dict = {}
GST = 0.08
lucky_spins = 3
cart = {}
zero_list = [False]
discount_day = [False, 0]
val = True
tick_vars = []
total_price_labels = []
frames_to_get_removed = []
lucky_discount = []


def valo():  # Valorent Easter Egg
    global val
    if not val:
        val = True
    else:
        val = False


def check(inputted, item_id, added_to_cart, grey):  # Only allow 1 to 100 integers
    global cart
    if not inputted.strip().isdigit():
        messagebox.showerror("showerror", "Please enter a number between 1 to 100")
        inputted = '0'
    elif int(inputted) <= 0 or int(inputted) > 100:
        messagebox.showerror("showerror", "Please enter a number between 1 to 100")
        inputted = '0'
    if inputted != '0':
        cart[item_id] = str(int(inputted))
        if grey[0]:
            greyed_text(added_to_cart, grey[1], grey[2], grey[3])


def remove(item_id):
    global cart
    if item_id in cart:
        del cart[item_id]


def set_zero(quantity):
    global zero_list
    if not quantity.isdigit():
        return '0'
    else:
        quantity_int = int(quantity)
        quantity_int = str(quantity_int)
        return quantity_int


def add_to_cart(item_id):  # Item add to cart screen
    product_frame = ttk.Frame(window, width=100, height=200)
    product_frame.pack()

    back_frame = ttk.Frame(product_frame)
    back_frame.grid(row=0, column=0, columnspan=2)
    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=restart)
    item_selection_label = ttk.Label(back_frame, text="Item Selection", font=("Calibri", 20))
    item_selection_label.grid(row=0, column=1)

    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0)

    image_frame = ttk.Frame(product_frame, width=100, height=100, padding=50)
    image_frame.grid(row=1, column=0, rowspan=2)
    image = ImageTk.PhotoImage(Image.open(item_id + '.jpg').resize((400, 400)))
    image_label = ttk.Label(image_frame, image=image)
    image_label.image = image
    image_label.grid(row=1, column=0)

    description_frame = ttk.Frame(product_frame, width=100, height=50, padding=50)
    description_frame.grid(row=1, column=1, sticky='nsew')

    # Name
    product_label = ttk.Label(description_frame, text=stock[item_id]["name"], font=("Calibri", 30))
    product_label.grid(row=1, column=0, sticky='wn')

    # Category
    category_label = ttk.Label(description_frame, text=(item_id + ' ' + stock[item_id]["category"]),
                               font=("Calibri", 30))
    category_label.grid(row=0, column=0, sticky='wn')

    # Price
    price_label = ttk.Label(description_frame, text=f"$ {stock[item_id]['price']:.2f}", font=("Calibri", 25))
    price_label.grid(row=2, column=0, sticky='wn', ipady=10)

    add_to_cart_frame = ttk.Frame(product_frame, width=100, height=100, padding=10)
    add_to_cart_frame.grid(row=2, column=1, sticky='n')

    quantity_label = ttk.Label(add_to_cart_frame, text='Quantity', font=("Calibri", 20))
    quantity_label.grid(row=0, column=0, sticky='n')

    added_to_cart = tk.Label(add_to_cart_frame, text="Added to cart", font=("Calibri", 20), fg='grey')
    removed_from_cart = tk.Label(add_to_cart_frame, text="Item Removed", font=("Calibri", 20), fg='grey')
    remove_button = tk.Button(add_to_cart_frame, text='Remove item', font=("Calibri", 20),
                              command=lambda: [remove(item_id),
                                               greyed_text([True, removed_from_cart, True], quantity_int, remove_button,
                                                           enter_button)])
    enter_button = tk.Button(add_to_cart_frame, text='Add to cart', font=("Calibri", 20),
                             command=lambda: [check(quantity_int.get(), item_id, [True, added_to_cart, False],
                                                    [True, quantity_int, remove_button, enter_button]),
                                              quantity_int.set(set_zero(quantity_int.get()))])
    enter_button.grid(row=1, column=0, columnspan=2, ipadx=40, pady=10)

    if item_id in cart:
        enter_button.configure(text="Edit Quantity")
        quantity_int = tk.StringVar(value=str(int(cart[item_id])))
        remove_button.grid(row=2, column=0, columnspan=2, ipadx=30)
        quantity_int = tk.StringVar(value=str(int(cart[item_id])))
    else:
        quantity_int = tk.StringVar(value='0')
    quantity_spinbox = ttk.Spinbox(add_to_cart_frame, from_=0, to=100, width=10, textvariable=quantity_int)
    quantity_spinbox.grid(row=0, column=1)


def greyed_text(grey_label, quantity_int, remove_button, enter_button):
    if grey_label[0]:
        grey_label[1].grid(row=3, column=0, columnspan=2)
        grey_label[1].after(2000, grey_label[1].grid_forget)
        if grey_label[2]:  # Remove
            quantity_int.set('0')
            remove_button.grid_forget()
            enter_button.configure(text="Add to cart")
        else:  # Edit quantity
            enter_button.configure(text="Edit Quantity")
            remove_button.grid(row=2, column=0, columnspan=2, ipadx=30)


def display_items(choice, current_frame):  # Display items in a category
    display_frame = ttk.Frame(current_frame, width=100, height=200)
    display_frame.grid(row=1, column=0, columnspan=2)
    row = 0
    column = 0
    for i, (item_id, item_info) in enumerate(stock.items()):
        if item_info["category"].lower() == choice.lower():
            product_img = Image.open(item_id + '.jpg').resize((200, 200))
            product_image = ImageTk.PhotoImage(product_img)
            button_text = f'{choice.title()}\n{item_id} {item_info.get("name")}\n\n${item_info.get("price"):.2f}'
            button = tk.Button(display_frame, text=button_text, font=("Calibri", 20), justify='left', compound='top',
                               image=product_image,
                               command=lambda item=item_id: [add_to_cart(item), current_frame.pack_forget()])
            button.image = product_image

            button.grid(row=row, column=column, padx=10, pady=10)
            column += 1
            if column == 4:
                row += 1
                column = 0


def categories_frame_(name):
    cat_frame = ttk.Frame(window, width=100, height=200)
    cat_frame.pack()

    back_frame = ttk.Frame(cat_frame)
    back_frame.grid(row=0, column=0, columnspan=4)
    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=restart)

    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0)

    choice_label = tk.Label(back_frame, text=f'Choice Selected | {name.title()}', font=("Calibri", 20))
    choice_label.grid(row=0, column=1, pady=20)

    display_items(name, cat_frame)


def sort_by_price_frame_(categories_frame, mid_frame, htl_or_lth):
    if htl_or_lth:
        name = "High to Low"
    else:
        name = "Low to High"

    categories_frame.pack_forget()
    mid_frame.pack_forget()

    sort_by_price_frame = ttk.Frame(window, width=100, height=200)
    sort_by_price_frame.pack()

    back_frame = ttk.Frame(sort_by_price_frame)
    back_frame.grid(row=0, column=0, columnspan=3)
    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=restart)

    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0)

    sort_by_price_label = tk.Label(back_frame, text=name, font=("Calibri", 20))
    sort_by_price_label.grid(row=0, column=1)

    display_frame = ttk.Frame(sort_by_price_frame, width=100, height=200)
    display_frame.grid(row=1, column=0, columnspan=2)

    canvas = tk.Canvas(display_frame, width=1300, height=700)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(display_frame, orient='vertical', command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    second_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=second_frame, anchor='nw')

    sort_by_price_lst = []
    for item_id, price in stock.items():
        sort_by_price_lst.append([price['price'], item_id])
    sort_by_price_lst.sort(reverse=htl_or_lth)

    row = 0
    column = 0
    for i, (item_price, item_id) in enumerate(sort_by_price_lst):
        product_img = Image.open(item_id + '.jpg').resize((200, 200))
        product_image = ImageTk.PhotoImage(product_img)
        button_text = f'{stock[item_id].get("category")}\n{item_id} {stock[item_id].get("name")}\n\n$' \
                      f'{stock[item_id].get("price"):.2f}'
        button = tk.Button(
            second_frame,
            text=button_text,
            font=("Calibri", 20),
            justify='left',
            compound='top',
            image=product_image,
            command=lambda item=item_id: [add_to_cart(item), sort_by_price_frame.pack_forget()]
        )
        button.config(image=product_image)
        button.image = product_image
        button.grid(row=row, column=column, padx=10, pady=10)
        column += 1
        if column == 4:
            row += 1
            column = 0


def show_all_frame_(categories_frame, mid_frame):
    categories_frame.pack_forget()
    mid_frame.pack_forget()

    show_all_frame = ttk.Frame(window, width=100, height=200)
    show_all_frame.pack()

    back_frame = ttk.Frame(show_all_frame)
    back_frame.grid(row=0, column=0)
    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=restart)

    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0)
    show_all_label = tk.Label(back_frame, text="Show All", font=("Calibri", 20))
    show_all_label.grid(row=0, column=1)

    display_frame = ttk.Frame(show_all_frame, width=100, height=200)
    display_frame.grid(row=1, column=0, padx=(80, 0))

    canvas = tk.Canvas(display_frame, width=1300, height=700)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(display_frame, orient='vertical', command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    second_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=second_frame, anchor='nw')

    row = 0
    column = 0
    for i, (item_id, item_info) in enumerate(stock.items()):
        product_img = Image.open(item_id + '.jpg').resize((200, 200))
        product_image = ImageTk.PhotoImage(product_img)
        button_text = f'{item_info.get("category")}\n{item_id} {item_info.get("name")}\n\n${item_info.get("price"):.2f}'
        button = tk.Button(
            second_frame,
            text=button_text,
            font=("Calibri", 20),
            justify='left',
            compound='top',
            image=product_image,
            command=lambda item=item_id: [add_to_cart(item), show_all_frame.pack_forget()]
        )
        button.config(image=product_image)
        button.image = product_image
        button.grid(row=row, column=column, padx=10, pady=10)
        column += 1
        if column == 4:
            row += 1
            column = 0


def discount_check_frame_(categories_frame, mid_frame):
    global discount_day
    categories_frame.pack_forget()
    mid_frame.pack_forget()

    discount_check_frame = ttk.Frame(window, width=100, height=200)
    discount_check_frame.pack()

    back_frame = ttk.Frame(discount_check_frame)
    back_frame.grid(row=0, column=0)
    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=restart)

    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0)

    discount_check_label = ttk.Label(back_frame, text="Discounts", font=("Calibri", 20))
    discount_check_label.grid(row=0, column=1)

    discount_frame = ttk.Frame(discount_check_frame)
    discount_frame.grid(row=1, column=0)

    lucky_spin_frame = ttk.Frame(discount_frame)
    lucky_spin_frame.grid(row=0, column=0)

    lucky_spin_text_frame = ttk.Frame(lucky_spin_frame)
    lucky_spin_text_frame.grid(row=0, column=0)
    lucky_spin_label = ttk.Label(lucky_spin_text_frame, text="Lucky Spin Discount", font=("Calibri", 20))
    lucky_spin_label.grid(row=0, column=0)
    lucky_spin_discount = ttk.Label(lucky_spin_text_frame, text="No discounts", font=("Calibri", 20))
    lucky_spin_discount.grid(row=1, column=0)

    lucky_spin_image = ImageTk.PhotoImage(Image.open('lucky_discount_banner.png').resize((450, 250)))
    lucky_spin_box = tk.Button(lucky_spin_frame, image=lucky_spin_image,
                               command=lambda: [lucky_spin_frame_(categories_frame, mid_frame),
                                                discount_check_frame.pack_forget()])
    lucky_spin_box.image = lucky_spin_image
    lucky_spin_box.grid(row=0, column=1)

    if len(lucky_discount) > 0:
        if lucky_discount[0]:  # Percentage discounts
            lucky_spin_discount.configure(text=f'{lucky_discount[1] * 100:.0f}% Off')
        else:  # Dollars off
            lucky_spin_discount.configure(text=f'${lucky_discount[1]:.2f} Off')

    sale_box_image = ImageTk.PhotoImage(Image.open("no discounts.png").resize((520, 250)))
    sale_box = tk.Button(lucky_spin_frame,
                         text=f"No discounts today\nClick for more info",
                         font=("Calibri", 20), image=sale_box_image,
                         command=lambda: [date_sale_frame_(categories_frame, mid_frame),
                                          discount_check_frame.pack_forget()])
    sale_box.image = sale_box_image
    sale_box.grid(row=1, column=0)
    sales_check(sale_box)

    discount_day_frame = ttk.Frame(lucky_spin_frame)
    discount_day_frame.grid(row=1, column=1)
    if discount_day[0]:
        discount_day_label_name = ttk.Label(discount_day_frame, text=discount_day[2], font=("Calibri", 20))
        discount_day_label_name.grid(row=0, column=0)
        discount_day_label = ttk.Label(discount_day_frame, text=f'{discount_day[1] * 100}% Off', font=("Calibri", 20))
        discount_day_label.grid(row=1, column=0)


def refresh_label(index, item_id):
    total_price = int(cart[item_id]) * stock[item_id]['price']
    total_price_labels[index].config(text=f"${total_price:.2f}")


def total(checkout_total_label):
    total_monies = 0
    for i, item_id in enumerate(cart):
        total_monies += (int(cart[item_id]) * stock[item_id]['price'])
    checkout_total_label.configure(text=f'${total_monies:.2f}')
    return total_monies


def refresh(categories_frame, mid_frame, top_frame, cart_frame):
    cart_frame.pack_forget()
    categories_frame.pack_forget()
    mid_frame.pack_forget()
    cart_frame_(categories_frame, mid_frame, top_frame)


def select_all_checkboxes(select):
    if select:
        for tick in tick_vars:
            tick.set(1)
    else:
        for tick in tick_vars:
            tick.set(0)


def remove_selected_items(categories_frame, mid_frame, top_frame, cart_frame):
    global tick_vars
    items_to_remove = []
    test = ''
    for g in range(len(tick_vars)):
        test += str(tick_vars[g].get())

    for i, item_id in enumerate(cart):
        if tick_vars[i].get() == 1:
            items_to_remove.append(item_id)
    for item_id in items_to_remove:
        cart.pop(item_id, None)
    tick_vars = []
    refresh(categories_frame, mid_frame, top_frame, cart_frame)


def cart_frame_(categories_frame, mid_frame, top_frame):
    global tick_vars
    categories_frame.pack_forget()
    mid_frame.pack_forget()
    destroy_children()
    top_menu()
    top_ui()

    cart_frame = ttk.Frame(window, width=700, height=200)
    cart_frame.pack()

    back_frame = ttk.Frame(cart_frame)
    back_frame.grid(row=0, column=0, columnspan=2, pady=(10, 30))
    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=restart)

    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0)

    cart_label = tk.Label(back_frame, text="Shopping cart", font=("Calibri", 20))
    cart_label.grid(row=0, column=1)

    if len(cart) == 0:
        space = tk.Label(cart_frame)
        space.grid(row=1, column=0, columnspan=2, pady=70)
        no_items = tk.Label(cart_frame, text="Your shopping cart is empty", font=("Calibri", 20))
        no_items.grid(row=2, column=0, columnspan=2)
        back_button_no = tk.Button(cart_frame, text='Go Shopping Now', font=("Calibri", 20),
                                   command=restart)
        back_button_no.grid(row=3, column=0, columnspan=2)
    else:
        display_frame = ttk.Frame(cart_frame, width=700, height=200)
        display_frame.grid(row=5, column=0, columnspan=2)

        canvas = tk.Canvas(display_frame, width=1300, height=500)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(display_frame, orient='vertical', command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        second_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=second_frame, anchor='nw')

        header = f'{"Product":70s}{"Unit Price":40s}{"Quantity":20s}{"Total Price":20s}{"Actions":15s}'

        header_label = tk.Label(cart_frame, text=header, font=("Calibri", 20))
        header_label.grid(row=4, column=0, columnspan=2)

        checkout_frame = tk.Frame(cart_frame, width=700, height=100)
        checkout_frame.grid(row=6, column=0, columnspan=2)

        checkout_total_label = ttk.Label(checkout_frame, text='$0', font=("Calibri", 15))
        checkout_total_label.grid(row=0, column=3, rowspan=2)
        checkout_button = tk.Button(checkout_frame, text="Check Out", font=('Calibri', 15),
                                    command=lambda: [are_you_member(categories_frame, mid_frame, top_frame),
                                                     cart_frame.pack_forget(), top_frame.pack_forget()])
        checkout_button.grid(row=0, column=4, rowspan=2)

        total_items_label = ttk.Label(checkout_frame, text=f'Subtotal ({len(cart)} items): ')
        total_items_label.grid(row=0, column=2, rowspan=2, padx=(20, 0))

        select_all_items_button = tk.Button(checkout_frame, text='Select All Items', font=('Calibri', 15),
                                            command=lambda: select_all_checkboxes(True))
        select_all_items_button.grid(row=0, column=0, sticky='w')

        unselect_button = tk.Button(checkout_frame, text='Un-select Items', font=('Calibri', 15),
                                    command=lambda: select_all_checkboxes(False))
        unselect_button.grid(row=0, column=1, sticky='w')

        remove_selected_items_button = tk.Button(checkout_frame, text='Remove Selected Items', font=('Calibri', 15),
                                                 command=lambda: remove_selected_items(categories_frame,
                                                                                       mid_frame, top_frame,
                                                                                       cart_frame))
        remove_selected_items_button.grid(row=1, column=0, columnspan=2, sticky='w')

        total(checkout_total_label)

        total_price_labels.clear()

        count = 0
        ticks = []
        for i, item_id in enumerate(cart):
            product_img = Image.open(item_id + '.jpg').resize((100, 100))
            product_image = ImageTk.PhotoImage(product_img)

            tick = tk.IntVar()
            ticks.append(tick)
            tick_vars = ticks

            product_checkbutton = tk.Checkbutton(second_frame, variable=tick, onvalue=1, offvalue=0)
            product_checkbutton.grid(row=count, column=0, rowspan=2)

            image_label = ttk.Label(second_frame, image=product_image)
            image_label.image = product_image
            image_label.grid(row=count, column=1, rowspan=2, padx=(10, 20))

            product_info = stock[item_id]
            name_label = tk.Label(second_frame, text=f"{product_info['category']}\n{item_id} {stock[item_id]['name']}",
                                  font=("Calibri", 15))
            name_label.grid(row=count, column=2, sticky='w', rowspan=2, padx=(0, 200))

            price_label = tk.Label(second_frame, text=f"${product_info['price']:.2f}", font=("Calibri", 15))
            price_label.grid(row=count, column=3, sticky='w', rowspan=2, padx=(0, 200))

            quantity_int = tk.StringVar(value=str(int(cart[item_id])))
            quantity_spinbox = ttk.Spinbox(second_frame, from_=0, to=100, width=10, textvariable=quantity_int)
            quantity_spinbox.grid(row=count, column=4, padx=(0, 50))

            enter_button = tk.Button(second_frame, text='Update quantity', font=("Calibri", 15),
                                     command=lambda quantity_int_=quantity_int, item_id_=item_id, index=i: [
                                         check(quantity_int_.get(), item_id_, [False], [False]),
                                         quantity_int_.set(set_zero(quantity_int_.get())),
                                         refresh_label(index, item_id_), total(checkout_total_label)])
            enter_button.grid(row=count + 1, column=4, padx=(0, 50))

            total_price_label = ttk.Label(second_frame, text=f"${int(cart[item_id]) * stock[item_id]['price']:.2f}",
                                          font=("Calibri", 15))
            total_price_label.grid(row=count, column=5, rowspan=2, padx=(0, 50))
            total_price_labels.append(total_price_label)

            delete_item_button = tk.Button(second_frame, text="Remove item", font=("Calibri", 15),
                                           command=lambda item_id_=item_id: [remove(item_id_),
                                                                             refresh(categories_frame, mid_frame,
                                                                                     top_frame, cart_frame)])
            delete_item_button.grid(row=count, column=6, rowspan=2, padx=(0, 50))

            blank = ttk.Label(second_frame, text=' ')
            blank.grid(row=count + 2, column=1, pady=5)
            count += 3


def are_you_member(categories_frame, mid_frame, top_frame):
    destroy_children()
    top_menu()
    member_frame = ttk.Frame(window)
    member_frame.pack()

    logo_frame = ttk.Frame(member_frame)
    logo_frame.pack()

    logo_image = ImageTk.PhotoImage(Image.open('ACE_logo_high.png').resize((245, 75)))
    logo_label = ttk.Label(logo_frame, image=logo_image)
    logo_label.image = logo_image
    logo_label.grid(row=0, column=0, pady=20)

    back_frame = ttk.Frame(member_frame)
    back_frame.pack()

    payment_label = ttk.Label(back_frame, text="Payment", font=("Calibri", 20))
    payment_label.grid(row=0, column=1, padx=10, pady=10)

    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=lambda: [member_frame.pack_forget(),
                                                                                       cart_frame_(categories_frame,
                                                                                                   mid_frame,
                                                                                                   top_frame)])

    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0)

    payment_frame = ttk.Frame(member_frame)
    payment_frame.pack()
    membership_label = ttk.Label(payment_frame, text="Are you a member with us? ", font=("Calibri", 20))
    membership_label.grid(row=0, columnspan=2, column=0)

    yes_button = tk.Button(payment_frame, text="Yes", font=("Calibri", 20),
                           command=lambda: [be_a_member(categories_frame, mid_frame, top_frame, 'Yes'),
                                            member_frame.pack_forget()])
    yes_button.grid(row=1, column=0)

    no_button = tk.Button(payment_frame, text="No", font=("Calibri", 20),
                          command=lambda: [be_a_member(categories_frame, mid_frame, top_frame, 'No'),
                                           member_frame.pack_forget()])
    no_button.grid(row=1, column=1)


def checkout(membership_var, categories_frame, mid_frame, top_frame):
    checkout_frame = ttk.Frame(window)
    checkout_frame.pack()

    logo_frame = ttk.Frame(checkout_frame)
    logo_frame.pack()

    logo_image = ImageTk.PhotoImage(Image.open('ACE_logo_high.png').resize((245, 75)))
    logo_label = ttk.Label(logo_frame, image=logo_image)
    logo_label.image = logo_image
    logo_label.grid(row=0, column=0, pady=20)

    back_frame = ttk.Frame(checkout_frame)
    back_frame.pack()

    payment_label = ttk.Label(back_frame, text="Checkout", font=("Calibri", 20))
    payment_label.grid(row=0, column=1, padx=10, pady=10)

    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=lambda: [checkout_frame.pack_forget(),
                                                                                       cart_frame_(categories_frame,
                                                                                                   mid_frame,
                                                                                                   top_frame)])

    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0)

    payment_frame = ttk.Frame(checkout_frame, width=700, height=200)
    payment_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(payment_frame, width=1300, height=300)
    my_canvas.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

    my_scrollbar = ttk.Scrollbar(payment_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

    product_label = ttk.Label(second_frame, text='Product', font=("Calibri", 15))
    product_label.grid(row=0, column=0, padx=(350, 20))
    name_label = ttk.Label(second_frame, text='Name', font=("Calibri", 15))
    name_label.grid(row=0, column=1, padx=(0, 20))
    unit_price_label = ttk.Label(second_frame, text="Unit Price", font=("Calibri", 15))
    unit_price_label.grid(row=0, column=2, padx=(0, 20))
    quantity_label_ = ttk.Label(second_frame, text="Quantity", font=("Calibri", 15))
    quantity_label_.grid(row=0, column=3, padx=(0, 20))
    total_label = ttk.Label(second_frame, text="Total", font=("Calibri", 15))
    total_label.grid(row=0, column=4, padx=(0, 20))

    for i, item_id in enumerate(cart):
        product_img = Image.open(item_id + '.jpg').resize((100, 100))
        product_image = ImageTk.PhotoImage(product_img)

        image_label = ttk.Label(second_frame, image=product_image)
        image_label.image = product_image
        image_label.grid(row=i + 1, column=0, padx=(350, 20))

        product_info = stock[item_id]
        name_label = tk.Label(second_frame, text=f"{product_info['category']}\n{item_id} {stock[item_id]['name']}",
                              font=("Calibri", 15))
        name_label.grid(row=i + 1, column=1, padx=(0, 20))

        price_label = tk.Label(second_frame, text=f"${product_info['price']:.2f}", font=("Calibri", 15))
        price_label.grid(row=i + 1, column=2, padx=(0, 20))

        quantity_label = ttk.Label(second_frame, text=str(int(cart[item_id])), font=("Calibri", 15))
        quantity_label.grid(row=i + 1, column=3, padx=(0, 20))
        total_price_label = ttk.Label(second_frame, text=f"${int(cart[item_id]) * stock[item_id]['price']:.2f}",
                                      font=("Calibri", 15))
        total_price_label.grid(row=i + 1, column=4, padx=(0, 20))
        total_price_labels.append(total_price_label)

        blank = ttk.Label(second_frame, text=' ')
        blank.grid(row=i + 2, column=1, pady=50)

    discounts_frame = ttk.Frame(checkout_frame)
    discounts_frame.pack()

    line_img = Image.open('Line.png').resize((650, 1))
    line_img = ImageTk.PhotoImage(line_img)
    line_img_label = ttk.Label(discounts_frame, image=line_img)
    line_img_label.image = line_img
    line_img_label.grid(row=0, column=0, columnspan=3)

    sub_total_label = ttk.Label(discounts_frame, text='$', font=("Calibri", 15))
    sub_total_label.grid(row=1, column=2)
    total_monies = total(sub_total_label)
    subtotal_label = ttk.Label(discounts_frame, text="Sub Total:", font=("Calibri", 15))
    subtotal_label.grid(row=1, column=1)

    if membership_var.get() != 4 or len(lucky_discount) > 0:
        discount_label = ttk.Label(discounts_frame, text="Discounts", font=("Calibri", 15))
        discount_label.grid(row=2, column=0)

    if len(lucky_discount) > 0:
        discount_label = ttk.Label(discounts_frame, text="Lucky Spin Discount", font=("Calibri", 15))
        discount_label.grid(row=3, column=1)
        if lucky_discount[0]:  # Percentage discounts
            lucky_discount_label = ttk.Label(discounts_frame, text=f'{lucky_discount[1] * 100:.0f}% Off',
                                             font=("Calibri", 15))
            lucky_discount_label.grid(row=3, column=2)
        else:  # Dollars off
            lucky_discount_label = ttk.Label(discounts_frame, text=f'${lucky_discount[1]:.2f} Off',
                                             font=("Calibri", 15))
            lucky_discount_label.grid(row=3, column=2)

    if membership_var.get() == 4:
        membership_discounts = 0
    else:
        if val:
            member_images = 'val'
        else:
            member_images = 'icons'

        member_img = Image.open(membership[membership_var.get()][member_images]).resize((50, 50))
        member_img = ImageTk.PhotoImage(member_img)
        member_label = ttk.Label(discounts_frame, image=member_img)
        member_label.image = member_img
        member_label.grid(row=4, column=0)

        member_name_label = ttk.Label(discounts_frame, text=f"{membership[membership_var.get()]['name']} member",
                                      font=("Calibri", 15))
        member_name_label.grid(row=4, column=1)

        percentage_label = ttk.Label(discounts_frame,
                                     text=f"{membership[membership_var.get()]['percentage'] * 100:.0f}% Off",
                                     font=("Calibri", 15))
        percentage_label.grid(row=4, column=2)

        membership_discounts = membership[membership_var.get()]['percentage']

    if discount_day[0] and total_monies >= 300:
        discount_day_label_name = ttk.Label(discounts_frame, text=discount_day[2], font=("Calibri", 15))
        discount_day_label_name.grid(row=5, column=1)
        discount_day_label = ttk.Label(discounts_frame, text=f'{discount_day[1] * 100:.0f}% Off', font=("Calibri", 15))
        discount_day_label.grid(row=5, column=2)

    gst_label = ttk.Label(discounts_frame, text='GST', font=("Calibri", 15))
    gst_label.grid(row=7, column=1)
    gst_percentage_label = ttk.Label(discounts_frame, text=f"{GST * 100}%", font=("Calibri", 15))
    gst_percentage_label.grid(row=7, column=2)

    line_img_label_1 = ttk.Label(discounts_frame, image=line_img)
    line_img_label_1.image = line_img
    line_img_label_1.grid(row=8, columnspan=3, column=0)

    grand_total_label = ttk.Label(discounts_frame, text="Grand Total:", font=("Calibri", 15))
    grand_total_label.grid(row=10, column=1)

    if len(lucky_discount) > 0:
        if lucky_discount[0]:
            grand_total_monies_bf_gst = (total_monies - (total_monies * membership_discounts) -
                                         (total_monies * lucky_discount[1]) - (total_monies * discount_day[1]))
        else:
            grand_total_monies_bf_gst = (total_monies - (total_monies * membership_discounts) -
                                         lucky_discount[1] - (total_monies * discount_day[1]))
    else:
        grand_total_monies_bf_gst = (total_monies - (total_monies * membership_discounts) -
                                     (total_monies * discount_day[1]))
    grand_total_monies = grand_total_monies_bf_gst * (1 + GST)
    grand_total = ttk.Label(discounts_frame, text=f'${grand_total_monies:.2f}', font=("Calibri", 15))
    grand_total.grid(row=10, column=2)

    saved_label = ttk.Label(discounts_frame, text='Saved', font=("Calibri", 15))
    saved_label.grid(row=9, column=1)

    saved = total_monies - grand_total_monies
    if saved <= 0:
        saved = 0
    saved_monies_label = ttk.Label(discounts_frame, text=f'${saved:.2f}', font=("Calibri", 15))
    saved_monies_label.grid(row=9, column=2)

    purchase_button = tk.Button(checkout_frame, text="Payment", font=("Calibri", 20),
                                command=lambda: [purchase_bye(), checkout_frame.pack_forget()])
    purchase_button.pack(pady=(20, 0))


def cart_be_gone(thank_you_frame):
    global cart
    thank_you_frame.place_forget()
    cart = {}
    main_ui()


def purchase_bye():
    thank_you_frame = ttk.Frame(window)
    thank_you_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    thank_you_msg = ttk.Label(thank_you_frame, text='Thank you for buying from ', font=("Calibri", 25))
    thank_you_msg.grid(row=0, column=0)

    logo_image = ImageTk.PhotoImage(Image.open('ACE_logo_high.png').resize((245, 75)))
    logo_label = ttk.Label(thank_you_frame, image=logo_image)
    logo_label.image = logo_image
    logo_label.grid(row=0, column=1)

    go_back_button = tk.Button(thank_you_frame, text='Continue Shopping', font=("Calibri", 20),
                               command=lambda: cart_be_gone(thank_you_frame))
    go_back_button.grid(row=1, column=0, columnspan=2)


def membership_choice(membership_var, categories_frame, mid_frame, top_frame, checkout_frame, proceed_frame):
    if membership_var.get() == 0:
        choose_label = ttk.Label(proceed_frame, text="Please choose an option", font=("Calibri", 20))
        choose_label.grid(row=6, column=0, columnspan=2)

    else:
        checkout_frame.pack_forget()
        checkout(membership_var, categories_frame, mid_frame, top_frame)


def be_a_member(categories_frame, mid_frame, top_frame, choice):
    checkout_frame = ttk.Frame(window)
    checkout_frame.pack()

    logo_frame = ttk.Frame(checkout_frame)
    logo_frame.pack()

    logo_image = ImageTk.PhotoImage(Image.open('ACE_logo_high.png').resize((245, 75)))
    logo_label = ttk.Label(logo_frame, image=logo_image)
    logo_label.image = logo_image
    logo_label.grid(row=0, column=0, pady=20)

    back_frame = ttk.Frame(checkout_frame)
    back_frame.pack()

    payment_label = ttk.Label(back_frame, text="Payment", font=("Calibri", 20))
    payment_label.grid(row=0, column=1, padx=10, pady=10)

    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=lambda: [checkout_frame.pack_forget(),
                                                                                       cart_frame_(categories_frame,
                                                                                                   mid_frame,
                                                                                                   top_frame)])
    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0)

    question_frame = ttk.Frame(checkout_frame)
    question_frame.pack()
    if choice == "Yes":
        question = "What member are you?"
    else:
        question = "Do you want to be a member with us?"

    membership_label = ttk.Label(question_frame, text=question, font=("Calibri", 20))
    membership_label.grid(row=0, column=0)

    payment_frame = ttk.Frame(checkout_frame)
    payment_frame.pack()
    membership_var = tk.IntVar()
    membership_var.set(0)

    radiobutton_text_style = ttk.Style()
    radiobutton_text_style.configure('Custom.TRadiobutton', font=('Calibri', 20),)

    if val:
        member_images = 'val'
    else:
        member_images = 'icons'

    for i in range(1, 4):
        icon_image = ImageTk.PhotoImage(Image.open(membership[i][member_images]).resize((100, 100)))
        icon_radiobutton = ttk.Radiobutton(
            payment_frame,
            variable=membership_var,
            value=i,
            text=membership[i]['name'],
            compound='left',
            image=icon_image,
            style='Custom.TRadiobutton'
        )
        icon_radiobutton.image = icon_image
        icon_radiobutton.grid(row=i, column=0, sticky='w')

    if choice == "No":
        no_icon_image = ImageTk.PhotoImage(Image.open(membership[4][member_images]).resize((100, 100)))
        no_icon_radiobutton = ttk.Radiobutton(
            payment_frame,
            variable=membership_var,
            value=4,
            text=membership[4]['name'],
            compound='left',
            image=no_icon_image,
            style='Custom.TRadiobutton'
        )
        no_icon_radiobutton.image = no_icon_image
        no_icon_radiobutton.grid(row=4, column=0, sticky='w')

    proceed_frame = ttk.Frame(checkout_frame)
    proceed_frame.pack()
    proceed_button = tk.Button(proceed_frame, text="Proceed to payment", font=("Calibri", 20),
                               command=lambda: membership_choice(membership_var, categories_frame, mid_frame,
                                                                 top_frame, checkout_frame, proceed_frame))
    proceed_button.grid(row=5, column=0, columnspan=2)


def spinning_animation(outcome, lucky_spin_frame):
    count = 50
    canvas = tk.Canvas(lucky_spin_frame, width=800)
    canvas.grid(row=7, column=0)
    animation_lst = []
    for i in range(7):
        animation_lst.append(random.choice(emoji_images))
    for i in range(count):
        canvas.create_text(400, 170, anchor=tk.CENTER, text='^', font=("Calibri", 15))
        canvas.create_image(100, 100, anchor=tk.CENTER, image=animation_lst[0])
        canvas.create_image(200, 100, anchor=tk.CENTER, image=animation_lst[1])
        canvas.create_image(300, 100, anchor=tk.CENTER, image=animation_lst[2])
        canvas.create_image(400, 100, anchor=tk.CENTER, image=animation_lst[3])
        canvas.create_image(500, 100, anchor=tk.CENTER, image=animation_lst[4])
        canvas.create_image(600, 100, anchor=tk.CENTER, image=animation_lst[5])
        canvas.create_image(700, 100, anchor=tk.CENTER, image=animation_lst[6])
        window.update()
        canvas.delete("all")
        animation_lst = animation_lst[1:]
        animation_lst.append(random.choice(emoji_images))

        canvas.after(100)
        if i == count - 1:
            animation_lst[3] = outcome
            canvas.create_text(400, 170, anchor=tk.CENTER, text='^', font=("Calibri", 15))
            canvas.create_image(100, 100, anchor=tk.CENTER, image=animation_lst[0])
            canvas.create_image(200, 100, anchor=tk.CENTER, image=animation_lst[1])
            canvas.create_image(300, 100, anchor=tk.CENTER, image=animation_lst[2])
            canvas.create_image(400, 100, anchor=tk.CENTER, image=animation_lst[3])
            canvas.create_image(500, 100, anchor=tk.CENTER, image=animation_lst[4])
            canvas.create_image(600, 100, anchor=tk.CENTER, image=animation_lst[5])
            canvas.create_image(700, 100, anchor=tk.CENTER, image=animation_lst[6])
            window.update()


def lucky_spin(lucky_spin_frame, spins_left, results_label, spin_button):
    global lucky_spins, lucky_discount
    spin_button["state"] = "disabled"

    if lucky_spins != 0:
        lucky_spins -= 1
        if lucky_spins == 0:
            spins_left.configure(foreground="red")
        spins_left.configure(text=f"You have {lucky_spins} lucky spins left.")

        results_label.configure(text="")
        spin_result = random.randint(1, 10000)
        if spin_result == 1:
            lucky_discount = [True, 0.8]
            spinning_animation(emoji_images[0], lucky_spin_frame)
            results_label.configure(text=f"Congratulations! You landed on an 80% discount!")
            spin_button["state"] = "normal"

        elif 2 <= spin_result <= 101:
            lucky_discount = [True, 0.2]
            spinning_animation(emoji_images[1], lucky_spin_frame)
            results_label.configure(text=f"Congratulations! You landed on a 20% discount!")
            spin_button["state"] = "normal"

        elif 102 <= spin_result <= 301:
            lucky_discount = [True, 0.1]
            spinning_animation(emoji_images[2], lucky_spin_frame)
            results_label.configure(text=f"Congratulations! You landed on a 10% discount!")
            spin_button["state"] = "normal"

        elif 302 <= spin_result <= 801:
            lucky_discount = [False, 5]
            spinning_animation(emoji_images[3], lucky_spin_frame)
            results_label.configure(text=f"Congratulations! You landed on a $5 discount!")
            spin_button["state"] = "normal"

        elif 802 <= spin_result <= 1801:
            lucky_discount = [False, 2]
            spinning_animation(emoji_images[3], lucky_spin_frame)
            results_label.configure(text=f"Congratulations! You landed on a $2 discount!")
            spin_button["state"] = "normal"

        elif 1802 <= spin_result <= 3801:
            lucky_discount = [False, 1]
            spinning_animation(emoji_images[4], lucky_spin_frame)
            results_label.configure(text=f"Congratulations! You landed on a $1 discount!")
            spin_button["state"] = "normal"
        else:
            lucky_discount = []
            spinning_animation(emoji_images[5], lucky_spin_frame)
            results_label.configure(text=f"Better luck next time!")
            spin_button["state"] = "normal"
        return


def lucky_spin_frame_(categories_frame, mid_frame):
    global lucky_spins
    categories_frame.pack_forget()
    mid_frame.pack_forget()

    lucky_spin_frame = ttk.Frame(window, width=100, height=200)
    lucky_spin_frame.pack()

    back_frame = ttk.Frame(lucky_spin_frame)
    back_frame.grid(row=0, column=0)
    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=restart)

    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0, pady=(0, 20))

    lucky_spin_label = tk.Label(back_frame, text="Lucky Spin", font=("Calibri", 20))
    lucky_spin_label.grid(row=0, column=1, pady=(0, 20))

    results_label = ttk.Label(lucky_spin_frame, text='', font=("Calibri", 20))
    results_label.grid(row=8, column=0)
    spins_left = ttk.Label(lucky_spin_frame, text=f"You have {lucky_spins} lucky spins left.", font=("Calibri", 15))
    spins_left.grid(row=4, column=0)
    if lucky_spins == 0:
        spins_left.configure(foreground="red")
    spin_button = tk.Button(lucky_spin_frame, text='Spin', font=("Calibri", 20),
                            command=lambda: lucky_spin(lucky_spin_frame, spins_left, results_label, spin_button))
    spin_button.grid(row=9, column=0)
    if lucky_spins == 3:
        welcome_label = ttk.Label(lucky_spin_frame, text="Welcome to ACE's Lucky Spin!", font=("Calibri", 20))
        welcome_label.grid(row=3, column=0)


def date_sale_frame_(categories_frame, mid_frame):
    categories_frame.pack_forget()
    mid_frame.pack_forget()

    date_sale_frame = ttk.Frame(window)
    date_sale_frame.pack()

    back_frame = ttk.Frame(date_sale_frame)
    back_frame.grid(row=0, column=0)
    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(back_frame, image=back_arrow_image, bd=0, command=restart)

    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0)

    date_sale_label = tk.Label(back_frame, text="Sale dates 2023", font=("Calibri", 20))
    date_sale_label.grid(row=0, column=1)

    dates_frame = ttk.Frame(date_sale_frame)
    dates_frame.grid(row=1, column=0, pady=20)

    name = ttk.Label(dates_frame, text="Names", font=("Calibri", 20))
    name.grid(row=0, column=0, padx=10)
    start = ttk.Label(dates_frame, text="Start date", font=("Calibri", 20))
    start.grid(row=0, column=1, padx=10)
    end = ttk.Label(dates_frame, text="End date", font=("Calibri", 20))
    end.grid(row=0, column=2, padx=10)
    for i in range(len(discount_days)):
        dates_name = f'{discount_days[i]["name"]}'
        dates_start = f'{discount_days[i]["start_date"].strftime("%d %b %Y")}'
        dates_end = f'{discount_days[i]["end_date"].strftime("%d %b %Y")}'
        dates_label = ttk.Label(dates_frame, text=dates_name, font=("Calibri", 20))
        dates_label.grid(row=i + 1, column=0, padx=10)
        dates_label = ttk.Label(dates_frame, text=dates_start, font=("Calibri", 20))
        dates_label.grid(row=i + 1, column=1, padx=10)
        dates_label = ttk.Label(dates_frame, text=dates_end, font=("Calibri", 20))
        dates_label.grid(row=i + 1, column=2, padx=10)

    line_img = Image.open('Line.png').resize((650, 1))
    line_img = ImageTk.PhotoImage(line_img)
    line_img_label = ttk.Label(date_sale_frame, image=line_img)
    line_img_label.image = line_img
    line_img_label.grid(row=2, column=0, pady=20)

    info_label = ttk.Label(date_sale_frame, text='Enjoy 10% Off for $300 spent on a Single Receipt',
                           font=("Calibri", 20))
    info_label.grid(row=3, column=0)


def dupe_display_item(name):  # For items like wing gundam
    display_frame = ttk.Frame(window, width=100, height=200)
    display_frame.pack()
    row = 0
    column = 0
    for item_id in name:
        product_img = Image.open(item_id + '.jpg').resize((200, 200))
        product_image = ImageTk.PhotoImage(product_img)
        button_text = f'{stock[item_id]["name"]}\n{item_id} {stock[item_id]["category"]}\n\n' \
                      f'${stock[item_id]["price"]:.2f}'
        button = tk.Button(display_frame, text=button_text, font=("Calibri", 20), justify='left', compound='top',
                           image=product_image,
                           command=lambda item=item_id: [add_to_cart(item), display_frame.pack_forget()])
        button.image = product_image
        button.grid(row=row, column=column, pady=5, padx=5)
        column += 1
        if column == 4:
            row += 1
            column = 0


def search_item(keyword, current_frames):
    destroy_children()
    top_menu()
    top_ui()
    name_lst = []
    count = []
    category_lst = []
    for item in stock.values():
        name = item['name']
        name_lst.append(name.lower())
        category = item['category']
        category_lst.append(category.lower())

    try:
        if 1 <= int(keyword) <= 9:
            keyword = '0' + keyword
    except ValueError:
        pass
    if keyword.lower() == 'motorised':
        keyword = 'motorised'
    if keyword in stock.keys():  # Item ID
        for frames in current_frames:
            frames.pack_forget()
        add_to_cart(keyword)
    elif keyword.lower() in name_lst:  # Name
        for id_item, item in enumerate(name_lst):
            if keyword == item:
                if id_item + 1 <= 9:
                    count.append('0' + str(id_item + 1))
                else:
                    count.append(str(id_item + 1))
        if len(count) > 1:
            for frames in current_frames:
                frames.pack_forget()
            dupe_display_item(count)
            return

        for item_id, name in enumerate(name_lst):
            if keyword == name:
                item_id += 1
                if 1 <= item_id <= 9:
                    item_id = '0' + str(item_id)
                item_id = str(item_id)
                for frames in current_frames:
                    frames.pack_forget()
                add_to_cart(item_id)
    elif keyword.lower() in category_lst:
        categories_frame_(keyword.lower())
    else:
        for frames in current_frames:
            frames.pack_forget()
        not_found_frame = ttk.Frame(window, width=100, height=200)
        not_found_frame.pack()

        if keyword == "search by name or item id" or keyword == '':
            not_found_text = 'Enter Name or Item ID'
        else:
            not_found_text = f"Item '{keyword}' is not found"

        item_not_found_label = ttk.Label(not_found_frame, text=not_found_text, font=('Calibri', 30))
        item_not_found_label.grid(row=0, column=0, sticky='nsew', pady=(30, 10))

        back_button = tk.Button(not_found_frame, text='Go Shopping Now', font=("Calibri", 20),
                                command=restart)
        back_button.grid(row=3, column=0, sticky='nsew')


def on_entry_click(entry):
    if entry.get() == "Search by Name or Item ID":
        entry.delete(0, tk.END)
        entry.configure(foreground='black')


def on_focusout(entry):
    if entry.get() == "":
        entry.insert(0, "Search by Name or Item ID")
        entry.configure(foreground='gray')


def destroy_children():
    for i in window.winfo_children():
        i.destroy()


def restart():
    destroy_children()
    main_ui()


def sales_check(sale_box):
    global discount_day
    for event in discount_days:
        if event["start_date"] <= current_date <= event["end_date"]:
            sale_box['text'] = f"{event['name']},\nEnjoy up to 10% off⁎ (with a min of $300 spent on a single receipt.)"
            sale_discount = 0.1
            discount_day = [True, sale_discount, event['name']]
            sale_box['image'] = event['image']


def toggle_fullscreen(event):
    is_fullscreen = window.attributes("-fullscreen")
    window.attributes("-fullscreen", not is_fullscreen)


def help_lucky_spin():
    destroy_children()
    top_menu()
    help_lucky_spin_frame = ttk.Frame(window)
    help_lucky_spin_frame.pack()
    logo_frame = ttk.Frame(help_lucky_spin_frame)
    logo_frame.pack()

    logo_image = ImageTk.PhotoImage(Image.open('ACE_logo_high.png').resize((245, 75)))
    logo_label = ttk.Label(logo_frame, image=logo_image)
    logo_label.image = logo_image
    logo_label.grid(row=0, column=0, pady=20)

    title_frame = ttk.Frame(logo_frame)
    title_frame.grid(row=1, column=0)
    title_label1 = ttk.Label(title_frame, text="HOW TO USE", font=("Calibri", 30, 'bold'))
    title_label1.grid(row=0, column=1)
    title_label2 = ttk.Label(title_frame, text="Lucky Spin", font=("Calibri", 25, 'bold'))
    title_label2.grid(row=1, column=1, pady=(0, 20))

    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(title_frame, image=back_arrow_image, bd=0, command=restart)
    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0, rowspan=2, padx=(0, 20))

    frame = ttk.Frame(help_lucky_spin_frame)
    frame.pack()

    information_frame = ttk.Frame(frame)
    information_frame.grid(row=0, column=0)

    sentence_label = ttk.Label(information_frame, text="• You have 3 chances per day to use\n\n"
                                                       "• If you're unsatisfied with the result, you can re-roll\n"
                                                       "for a better discount.\n\n"
                                                       "• DISCOUNTS WON ARE NOT ACCUMULATIVE, \n"
                                                       "PLEASE DO NOT BE MISTAKEN.", font=("Calibri", 20))
    sentence_label.grid(row=0, column=0)

    rate_frame = ttk.Frame(frame)
    rate_frame.grid(row=0, column=1)
    discount_label = ttk.Label(rate_frame, text="Discounts", font=("Calibri", 20, 'bold'))
    discount_label.grid(row=0, column=0, padx=5, pady=5)
    rates_label = ttk.Label(rate_frame, text="Rates", font=("Calibri", 20, 'bold'))
    rates_label.grid(row=0, column=1, padx=5, pady=5)

    for i, (discount, rate) in enumerate(rates, start=1):
        discount_label2 = ttk.Label(rate_frame, text=discount, font=("Calibri", 15))
        discount_label2.grid(row=i, column=0, padx=5, pady=5)
        rates_label2 = ttk.Label(rate_frame, text=rate, font=("Calibri", 15))
        rates_label2.grid(row=i, column=1, padx=5, pady=5)


def author():
    destroy_children()
    top_menu()
    author_frame = ttk.Frame(window)
    author_frame.pack()
    logo_frame = ttk.Frame(author_frame)
    logo_frame.pack()

    logo_image = ImageTk.PhotoImage(Image.open('ACE_logo_high.png').resize((245, 75)))
    logo_label = ttk.Label(logo_frame, image=logo_image)
    logo_label.image = logo_image
    logo_label.grid(row=0, column=0, pady=20)

    title_frame = ttk.Frame(logo_frame)
    title_frame.grid(row=1, column=0)
    title_label = ttk.Label(title_frame, text="About us", font=("Calibri", 30, 'bold'))
    title_label.grid(row=0, column=1)

    back_arrow_image = ImageTk.PhotoImage(Image.open('back_arrow.png').resize((40, 40)))
    back_button = tk.Button(title_frame, image=back_arrow_image, bd=0, command=restart)
    back_button.image = back_arrow_image
    back_button.grid(row=0, column=0, rowspan=2, padx=(0, 20))

    about_us_label = ttk.Label(author_frame, text="Author:", font=("Calibri", 25, 'bold'))
    about_us_label.pack(pady=(30, 0))

    names = f'{"Cayden Miguel Theseira (230833F)":^70}\n{"Chang Hao Wen (233431A)":^70}'
    author_label = ttk.Label(author_frame, text=names, font=("Calibri", 20))
    author_label.pack()


def top_menu():
    tab_frame = ttk.Frame(window)

    menu = tk.Menu(tab_frame)
    help_menu = tk.Menu(menu, tearoff=False)
    help_menu.add_command(label='Lucky Spin', command=help_lucky_spin)
    help_menu.add_separator()
    help_menu.add_command(label="Refresh page", command=restart)
    menu.add_cascade(label='Help', menu=help_menu)

    about_us_menu = tk.Menu(menu, tearoff=False)
    about_us_menu.add_command(label='Author', command=author)
    about_us_menu.add_separator()
    about_us_menu.add_command(label='Valorent', command=valo)

    menu.add_cascade(label='About us', menu=about_us_menu)
    window.configure(menu=menu)


def perform_search(search):
    if search.get().strip().isdigit():
        keyword = str(int(search.get().strip()))
    else:
        keyword = (search.get().strip()).lower()
    search_item(keyword, [frames_dict['mid_frame'], frames_dict['categories_frame']])


def top_ui():
    top_frame = ttk.Frame(window)
    top_frame.configure()
    top_frame.pack()

    logo_image = ImageTk.PhotoImage(Image.open('ACE_logo_high.png').resize((245, 75)))

    logo = tk.Button(top_frame, image=logo_image, bd=0, command=restart)  # Go home button
    logo.image = logo_image
    logo.grid(row=0, column=0, pady=20)

    search_style = ttk.Style()
    search_style.configure("Placeholder.TEntry", foreground='gray')
    search = ttk.Entry(top_frame, width=40, style="Placeholder.TEntry")
    search.configure(font=('Calibri', 25))
    search.insert(0, "Search by Name or Item ID")
    search.bind('<FocusIn>', lambda event: on_entry_click(search))
    search.bind('<FocusOut>', lambda event: on_focusout(search))
    search.grid(row=0, column=1, pady=20, padx=20)

    shopping_cart_image = ImageTk.PhotoImage(Image.open('SHOPPING CART ICON.png').resize((50, 50)))
    shopping_cart = tk.Button(top_frame, image=shopping_cart_image, font=('Calibri', 50),
                              command=lambda: [cart_frame_(frames_dict['categories_frame'], frames_dict['mid_frame'],
                                                           top_frame),
                                               frames_dict['categories_frame'].pack_forget()], bd=0)
    shopping_cart.image = shopping_cart_image
    shopping_cart.grid(row=0, column=3, pady=20, padx=5)

    search.bind('<Return>', lambda event: perform_search(search))
    search_image = ImageTk.PhotoImage(Image.open('MAGNIFYING GLASS ICON.png').resize((40, 40)))
    search_button = tk.Button(top_frame, image=search_image, font=('Calibri', 20),
                              command=lambda: perform_search(search), bd=0)
    search_button.image = search_image
    search_button.grid(row=0, column=2)

    if len(cart) > 0:
        red_ball = ImageTk.PhotoImage(Image.open('Red_Circle.png').resize((15, 15)))
        red_ball_button = tk.Button(top_frame, text=len(cart), image=red_ball, compound='center',
                                    font=('Calibri', 10, 'bold'), fg='white', bd=0,
                                    command=lambda: [cart_frame_(frames_dict['categories_frame'],
                                                                 frames_dict['mid_frame'], top_frame),
                                                     frames_dict['categories_frame'].pack_forget()])
        red_ball_button.image = red_ball
        red_ball_button.place(x=1055, y=30)
    return top_frame


def main_ui():
    top_menu()

    # TOP UI
    top_ui()

    # Middle UI
    mid_frame = ttk.Frame(window, width=100, height=100)
    mid_frame.pack()
    frames_dict['mid_frame'] = mid_frame

    sale_box_image = ImageTk.PhotoImage(Image.open("no discounts.png").resize((520, 250)))
    sale_box = tk.Button(mid_frame,
                         text=f"No discounts today\nClick for more info",
                         font=("Calibri", 20), image=sale_box_image,
                         command=lambda: date_sale_frame_(categories_frame, mid_frame))
    sale_box.grid(row=0, column=0)
    sales_check(sale_box)

    lucky_spin_image = ImageTk.PhotoImage(Image.open('lucky_discount_banner.png').resize((450, 250)))
    lucky_spin_box = tk.Button(mid_frame, image=lucky_spin_image,
                               command=lambda: lucky_spin_frame_(categories_frame, mid_frame))
    lucky_spin_box.grid(row=0, column=1, padx=20)

    # Bottom UI
    categories_frame = ttk.Frame(window, width=100, height=200)
    categories_frame.pack()
    frames_dict['categories_frame'] = categories_frame

    categories = tk.Label(categories_frame, text="Categories:", font=("Calibri", 20))
    categories.grid(row=0, column=0, pady=20)

    perfect_grade_image = ImageTk.PhotoImage(Image.open('PERFECT GRADE.png').resize((160, 100)))
    perfect_grade_button = tk.Button(categories_frame, image=perfect_grade_image,
                                     command=lambda: [categories_frame.pack_forget(), mid_frame.pack_forget(), categories_frame_("Perfect Grade")])
    perfect_grade_button.grid(row=1, column=0, padx=20)

    real_grade_image = ImageTk.PhotoImage(Image.open('real grade.png').resize((160, 100)))
    real_grade_button = tk.Button(categories_frame, image=real_grade_image,
                                  command=lambda: [categories_frame.pack_forget(), mid_frame.pack_forget(), categories_frame_("Real Grade")])
    real_grade_button.grid(row=1, column=1, padx=20)

    master_grade_image = ImageTk.PhotoImage(Image.open('MASTER GRADE.jpg').resize((160, 100)))
    master_grade_button = tk.Button(categories_frame, image=master_grade_image,
                                    command=lambda: [categories_frame.pack_forget(), mid_frame.pack_forget(), categories_frame_("Master Grade")])
    master_grade_button.grid(row=1, column=2, padx=20)

    mecha_gir_image = ImageTk.PhotoImage(Image.open('Mecha Girl.png').resize((160, 100)))
    mecha_girl_button = tk.Button(categories_frame, image=mecha_gir_image,
                                  command=lambda: [categories_frame.pack_forget(), mid_frame.pack_forget(), categories_frame_("Mecha Girl")])
    mecha_girl_button.grid(row=1, column=3, padx=20)

    motorized_image = ImageTk.PhotoImage(Image.open('motorised1.png').resize((160, 100)))
    motorized_button = tk.Button(categories_frame, image=motorized_image,
                                 command=lambda: [categories_frame.pack_forget(), mid_frame.pack_forget(), categories_frame_("Motorized")])
    motorized_button.grid(row=1, column=4, padx=20)

    sort_by_label = tk.Label(categories_frame, text="Sort by:", font=("Calibri", 20))
    sort_by_label.grid(row=3, column=0, pady=20)

    high_to_low_image = ImageTk.PhotoImage(Image.open('Sort_high_to_low.png').resize((50, 50)))
    high_to_low_button = tk.Button(categories_frame, image=high_to_low_image,
                                   command=lambda: sort_by_price_frame_(categories_frame, mid_frame,
                                                                        True), bd=0)
    high_to_low_button.grid(row=4, column=0, padx=20)
    high_to_low_label = tk.Label(categories_frame, text='High to low', font=("Calibri", 15))
    high_to_low_label.grid(row=5, column=0)

    low_to_high_image = ImageTk.PhotoImage(Image.open('Sort_low_to_high.png').resize((50, 50)))

    low_to_high_button = tk.Button(categories_frame, image=low_to_high_image,
                                   command=lambda: sort_by_price_frame_(categories_frame, mid_frame,
                                                                        False), bd=0)
    low_to_high_button.grid(row=4, column=1, padx=20)
    low_to_high_label = tk.Label(categories_frame, text='low to High', font=("Calibri", 15))
    low_to_high_label.grid(row=5, column=1)

    show_all_image = ImageTk.PhotoImage(Image.open('select_all.png').resize((50, 50)))
    show_all_button = tk.Button(categories_frame, image=show_all_image,
                                command=lambda: show_all_frame_(categories_frame, mid_frame), bd=0)
    show_all_button.grid(row=4, column=2, padx=20)
    show_all_label = tk.Label(categories_frame, text='Show All', font=("Calibri", 15))
    show_all_label.grid(row=5, column=2)

    line_img = Image.open('rotated_line_grey.png').resize((1, 75))
    line_img = ImageTk.PhotoImage(line_img)
    line_img_label = ttk.Label(categories_frame, image=line_img)
    line_img_label.image = line_img
    line_img_label.place(relx=0.6, rely=0.76)

    discount_check_image = ImageTk.PhotoImage(Image.open('discount.png').resize((50, 50)))
    discount_check_button = tk.Button(categories_frame, image=discount_check_image,
                                      command=lambda: discount_check_frame_(categories_frame, mid_frame), bd=0)
    discount_check_button.grid(row=4, column=3, padx=20)
    discount_check_button = tk.Label(categories_frame, text='Discounts', font=("Calibri", 15))
    discount_check_button.grid(row=5, column=3)

    quit_image = ImageTk.PhotoImage(Image.open('exit.png').resize((50, 50)))
    quit_button = tk.Button(categories_frame, image=quit_image,
                            command=lambda: window.destroy(), bd=0)
    quit_button.grid(row=4, column=4, padx=20)
    quit_button_label = tk.Label(categories_frame, text='Quit', font=("Calibri", 15))
    quit_button_label.grid(row=5, column=4)

    window.mainloop()


def main():
    window.bind("<F11>", toggle_fullscreen)
    window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}")
    window.title('ACE Shopping')
    window.iconbitmap("ACE_logo_black.ico")
    main_ui()


main()
