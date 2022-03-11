class FinancialEntity:

    def __init__(self, entity_id):
        self.id = entity_id

    def build_report(self):
        return f'Build Report #{self.id}'
