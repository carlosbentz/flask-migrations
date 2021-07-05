from flask import Flask
from flask.cli import AppGroup
from click import echo, argument
from app.models import UserModel, CreditCardModel
from faker import Faker


def cli_users(app: Flask):
    cli_users_group = AppGroup("user")
    session = app.db.session

    
    @cli_users_group.command("create")
    @argument("quantity")
    def cli_users_create(quantity):
        fake = Faker()
        quantity = int(quantity)

        if quantity < 1:
            echo(f"The minimum quantity must be at least 1, but was {quantity}")
            exit()

        for _ in range(quantity):
            login = fake.name()
            password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

            password_to_hash = password
            user= UserModel(login=login)
            user.password = password_to_hash

            session.add(user)
            session.commit()


    app.cli.add_command(cli_users_group)


def cli_admins(app: Flask):
    cli_admins_group = AppGroup("admin")
    session = app.db.session\


    @cli_admins_group.command("create")
    def cli_admins_create():
        fake = Faker()

        login = fake.name()
        password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

        password_to_hash = password
        admin= UserModel(login=login, is_admin=True)
        admin.password = password_to_hash

        session.add(admin)
        session.commit()
        echo(f"Admin criado!! \n login: {admin.login} \n password: {admin.password_hash}")



    app.cli.add_command(cli_admins_group)


def cli_credit_cards(app: Flask):
    cli_credit_cards_group = AppGroup("users_credit_cards")
    session = app.db.session\


    @cli_credit_cards_group.command("create")
    @argument("quantity")
    def cli_credit_cards_create(quantity):
        fake = Faker()
        quantity = int(quantity)

        if quantity < 1:
            echo(f"The minimum quantity must be at least 1, but was {quantity}")
            exit()

        for _ in range(quantity):
            login = fake.name()
            password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

            password_to_hash = password
            user= UserModel(login=login)
            user.password = password_to_hash
            session.add(user)
            session.commit()

            credit_cards_quantity = fake.random_int(min=0, max=2)

            for _ in range(credit_cards_quantity):
                credit_card = CreditCardModel(
                    expire_date=fake.credit_card_expire(),
                    number=fake.credit_card_number(),
                    provider=fake.credit_card_provider(),
                    security_code=fake.credit_card_security_code(card_type="mastercard"),
                    user_id=user.id
                )

                session.add(credit_card)


    app.cli.add_command(cli_credit_cards_group)

def init_app(app: Flask):
    cli_users(app)
    cli_admins(app)
    cli_credit_cards(app)
