from week2.jaeyoung.boundary import FinancialReportPresenter
from week2.jaeyoung.data_structure import FinancialReportRequest, \
    FinancialReportResponse
from week2.jaeyoung.repository import FinancialDataGateway


class FinancialReportRequester:

    def request(self,
                input_dto: FinancialReportRequest) -> FinancialReportResponse:
        pass


class FinancialReportGenerator(FinancialReportRequester):

    def __init__(self, repository: FinancialDataGateway):
        self.repository = repository

    def request(self, input_dto: FinancialReportRequest):
        entity = self.repository.read(input_dto.id)
        report_data = entity.build_report()

        return FinancialReportResponse(
            id=input_dto.id,
            report_data=report_data,
        )


class FinancialReportController:

    def __init__(self,
                 report_id: int,
                 presenter: FinancialReportPresenter,
                 requester: FinancialReportRequester):
        self.input_dto = FinancialReportRequest(id=report_id)
        self.presenter = presenter
        self.requester = requester

    def handle(self):
        output_dto = self.requester.request(self.input_dto)
        return self.presenter.present(output_dto)
