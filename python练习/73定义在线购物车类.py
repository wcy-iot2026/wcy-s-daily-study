# 购物车：添加商品、删除商品、查看内容、计算总价
class product:
    def __init__(self):
        # 用商品名当键，数量和价格放在里面
        self.cart = {}

    # 添加商品；已有的商品只增加数量
    def add_product(self, product, quantity, price):
        if product in self.cart:
            self.cart[product]["quantity"] += quantity
        else:
            self.cart[product] = {"quantity": quantity, "price": price}

    # 删除整个商品；购物车里没有就提示
    def remove_product(self, product, quantity):
        if product in self.cart:
            del self.cart[product]
        else:
            print(f"商品{product}不存在")

    # 查看购物车里每种商品的数量和价格
    def view_cart(self):
        if not self.cart:
            print("购物车为空")
            return
        for name, info in self.cart.items():
            print(f"{name}的数量为{info['quantity']},价格为{info['price']}")

    # 总价 = 每种商品的数量 × 价格，再相加
    def total_price(self):
        total = 0
        for name, info in self.cart.items():
            total += info["quantity"] * info["price"]
        return total


cart = product()
cart.add_product("苹果", 10, 10)
cart.add_product("香蕉", 20, 20)
cart.add_product("苹果", 5, 10)  # 苹果已存在，数量变成 15
print("添加后：")
cart.view_cart()
print(f"总价格为{cart.total_price()}")

cart.remove_product("香蕉", 20)
print("删除香蕉后：")
cart.view_cart()
print(f"总价格为{cart.total_price()}")

cart.remove_product("橘子", 1)  # 不存在的商品
