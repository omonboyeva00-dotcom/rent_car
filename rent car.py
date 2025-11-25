class Car:
    def __init__(self,car_id,model,price):
        self.car_id=car_id
        self.model=model
        self.price=price
        self.is_rented=False
        self.rented_by=None


class User:
    def __init__(self,user_id,name,salary):
        self.user_id=user_id
        self.name=name
        self.salary=salary
        self.rented_cars=[]


class JM_company:
    def __init__(self):
        self.balance=0

    def add_income(self,amount):
        self.balance+=amount



class rent_manager:
    def __init__(self):
        self.cars={}
        self.users={}
        self.company=JM_company()

    def add_car(self,car_id,model,price):
        self.cars[car_id]=Car(car_id,model,price)
        print("mashina qoshildi")

    def edit_car(self,car_id,new_model=None,new_price=None):
        if car_id not in self.cars:
            print("mashina yoq")
            return
        car=self.cars[car_id]

        if new_model:
            car.model=new_model
        if new_price:
            car.price=new_price
        print("mashina tahrirlandi")


    def add_user(self,user_id,name,salary):
        self.users[user_id]=User(user_id,name,salary)
        print("user qoshildi")

    def show_cars(self):
        for item in self.cars.values():
            holati="ijarada" if item.is_rented else "bosh"
            print(f"{item.car_id}{item.model}{item.price}{holati}")


    def rented_cars(self):
        for item in self.cars.values():
            if item.is_rented:
                print(f"{item.car_id}{item.model}{item.price}{item.rented_by}")

    def free_cars(self):
        for item in self.cars.values():
            if not item.is_rented:
                print(f"{item.car_id}{item.model}{item.price} bosh")

    def rent_car(self,car_id,user_id):
        if car_id not in self.cars:
            print("mashina yoq")
            return
        if user_id not in self.users:
            print("user yoq")
            return
        car=self.cars[car_id]
        user=self.users[user_id]

        if car.is_rented:
            print("mashina ijarada")
            return
        if user.salary<car.price:
            print("oylik yeterli emas")
            return

        car.is_rented=True
        car.rented_by=user.name
        user.rented_cars.append(car)
        self.company.balance+=car.price
        print(f"{user.name}{car.model}shu turdagi mashinani oldi")
        print(f"{self.company.balance}")


    def return_car(self,car_id,user_id):
        if car_id not in self.cars or user_id not in self.users:
            print("id raqam xato kiritdingiz")
            return
        car=self.cars[car_id]
        user=self.users[user_id]

        if car not in user.rented_cars:
            print("bu odam mashinani olmagan")
            return
        car.is_rented=False
        car.rented_by=None
        user.rented_cars.remove(car)
        print("mashina qaytarildi")

rental=rent_manager()
rental.add_car(1,"gentra",150)
rental.add_car(2,"cobalt",120)
rental.add_user(10,"nargiz",300)
rental.add_user(11,"ali",100)
rental.show_cars()

rental.rent_car(1,10)
rental.rent_car(2,11)
rental.rented_cars()
rental.free_cars()