class Employee():

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin

class Manager(Employee):

    def __init__(self, name, pin, salary, work_hour):
        self.name = name
        self.pin = pin
        self.salary = salary
        self.work_hour = work_hour

    def payroll_calculation(self):
        return self.salary



class Secretary(Employee):

    def __init__(self, name, pin, salary, work_hour):
        self.name = name
        self.pin = pin
        self.salary = salary
        self.work_hour = work_hour

    def payroll_calculation(self):
        return self.salary


class Seller(Employee):

    def __init__(self, name, pin, salary, work_hour, sell_count):
        self.name = name
        self.pin = pin
        self.salary = salary
        self.work_hour = work_hour
        self.sell_count = sell_count

    def payroll_calculation(self):
        return self.salary + 50 * self.sell_count

class Workshop_worker(Employee):

    def __init__(self, name, pin, work_hour):
        self.name = name
        self.pin = pin
        self.work_hour = work_hour

    def payroll_calculation(self):
        return self.work_hour * 100


class Replacement_secretary(Employee):

    def __init__(self, name, pin, work_hour):
        self.name = name
        self.pin = pin
        self.work_hour = work_hour

    def payroll_calculation(self):
        return self.work_hour * 100

def all_payroll_calculation():
    print(f' {manager.name} c пином номер {manager.pin} начислено {manager.payroll_calculation()} сом.')
    print(f' {secretary.name} c пином номер {secretary.pin} начислено {secretary.payroll_calculation()} сом.')
    print(f' {seller.name} c пином номер {seller.pin} начислено {seller.payroll_calculation()} сом.')
    print(f' {workshop_worker1.name} c пином номер {workshop_worker1.pin} начислено {workshop_worker1.payroll_calculation()} сом.')
    print(f' {workshop_worker2.name} c пином номер {workshop_worker2.pin} начислено {workshop_worker2.payroll_calculation()} сом.')
    print(f' {rep_secretary.name} c пином номер {rep_secretary.pin} начислено {rep_secretary.payroll_calculation()} сом.')
    print(f' Общий фонд заработной платы составил {manager.payroll_calculation()+secretary.payroll_calculation()+seller.payroll_calculation()+workshop_worker1.payroll_calculation()+workshop_worker2.payroll_calculation()+rep_secretary.payroll_calculation()} сом')

def all_performance_evaluation():
    dic = [{'emp': 'Барсбек Канаткулов', 'work': 18*100/40 },
           {'emp': 'Алымкул Тилекбаев', 'work': 38*100/40},
           {'emp': 'Айпери Шалымбекова', 'work': 38*100/40},
           {'emp': 'Бакыт Рустамов', 'work': 25*100/40},
           {'emp': 'Алтынай Ширинбаева', 'work': 40*100/40},
           {'emp': 'Жанар Рыскулов','work': 33*100/40}]

    newlist = sorted(dic, key=lambda k: k['work'])
    for i in newlist:

        if i['work'] < 100:
            print(i['emp']+f' не очень продуктивный сотрудник')
        elif i['work'] == 100:
            print(i['emp'] + f' продуктивный сотрудник')
        else:
            print(i['emp'] + f' очень продуктивный сотрудник')

    print(newlist[0]['emp'] + f' cамый не продуктивный сотрудник')
    print(newlist[-1]['emp'] + f' cамый продуктивный сотрудник')

manager = Manager('Барсбек Канаткулов', 1, 45000, 18)
secretary = Secretary('Алымкул Тилекбаев', 2, 20000, 38)
seller = Seller('Айпери Шалымбекова', 3, 20000, 38, 20)
workshop_worker1 = Workshop_worker('Бакыт Рустамов', 4, 25)
workshop_worker2 = Workshop_worker('Алтынай Ширинбаева', 5, 40)
rep_secretary = Replacement_secretary('Жанар Рыскулов', 6, 33)

all_payroll_calculation()
all_performance_evaluation()



