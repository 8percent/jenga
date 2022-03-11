from week2.jaeyoung.entity import FinancialEntity


class FinancialDataGateway:

    def create(self):
        pass

    def read(self, data_id):
        pass

    def update(self, data_id):
        pass

    def delete(self, data_id):
        pass


class FinancialDataMapper(FinancialDataGateway):

    def create(self):
        # Implementation
        pass

    def read(self, data_id) -> FinancialEntity:
        # Get From Database And Make it Entity
        return FinancialEntity(entity_id=data_id)

    def update(self, data_id):
        # Implementation
        pass

    def delete(self, data_id):
        # Implementation
        pass
