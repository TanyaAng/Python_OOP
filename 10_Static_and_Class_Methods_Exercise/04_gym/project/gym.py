class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result=''
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        result+=repr(subscription)+'\n'

        customer_id = subscription.customer_id
        customer = [c for c in self.customers if c.id == customer_id][0]
        result += repr(customer) + '\n'

        trainer_id = subscription.trainer_id
        trainer = [t for t in self.trainers if t.id == trainer_id][0]
        result += repr(trainer) + '\n'

        exercise_id = subscription.exercise_id
        exercise_plan = [e for e in self.plans if e.id == exercise_id ][0]

        equipment_id=exercise_plan.equipment_id
        equipment=[e for e in self.equipment if e.id==equipment_id][0]

        result += repr(equipment) + '\n'
        result += repr(exercise_plan) + '\n'

        return result.strip()







