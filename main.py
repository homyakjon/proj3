from datetime import datetime, timedelta


class MedicalRepresentation:

    days = timedelta(days=2500)

    def __init__(self, name, birthday, employment_date, unit, profile, salary):
        self.name = name
        self.birthday = self.transform_date(birthday)
        self.employment_date = self.transform_date(employment_date)
        self.unit = unit
        self.profile = profile
        self.salary = salary
        self.increases = {}

    def transform_date(self, date_as_string: str) -> datetime:
        date_as_object = datetime.strptime(date_as_string, "%d.%m.%Y")
        return date_as_object

    def check_work_experience(self):
        today = datetime.today()
        experience = today - self.employment_date
        return experience

    def increase_salary(self, amount, restrictions=True, increase_type=None):
        if self.increases.get(increase_type):
            print(f"Err: this MedRep already had {increase_type} increase")
            return False

        if amount > self.salary * 0.1 and restrictions:
            print("Err:You can not increase salary more than 10 % for one time ")
            return False

        self.salary += amount
        if increase_type:
            self.increases[increase_type] = True
        print(f"msg:new salary is {self.salary} UA")

    def data_processing(self):
        if self.check_work_experience() >= self.days:
            self.increase_salary(
                self.salary * 0.3,
                restrictions=False,
                increase_type="maximum",
            )


class Ivanich(MedicalRepresentation):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class YuraKorol(MedicalRepresentation):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Tatyana(MedicalRepresentation):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ArturBatya(MedicalRepresentation):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


ivanich = Ivanich(
    name="Roman",
    birthday="14.07.1981",
    employment_date="20.03.2017",
    unit="Rx",
    profile="Doctors",
    salary=2500.00,
)


korol = YuraKorol(
    name="Yurii",
    birthday="08.11.1989",
    employment_date="12.04.2014",
    unit="Rx",
    profile="Doctors",
    salary=2500.00,
)


tanya = Tatyana(
    name="Tanya",
    birthday="12.11.1978",
    employment_date="06.06.2017",
    unit="OTC",
    profile="Farmacy",
    salary=3000.00,
)


batya = ArturBatya(
    name="Artur",
    birthday="21.07.1980",
    employment_date="01.02.2014",
    unit="Rx",
    profile="Doctors",
    salary=3000.00,
)















