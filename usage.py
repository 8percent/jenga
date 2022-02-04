from week2.jaeyoung.boundary import PrintPresenter, PDFView, ScreenPresenter, \
    WebView
from week2.jaeyoung.repository import FinancialDataMapper
from week2.jaeyoung.usecase import FinancialReportController, \
    FinancialReportGenerator

if __name__ == '__main__':

    # Print PDF
    pdf_controller = FinancialReportController(
        report_id=1,
        presenter=PrintPresenter(PDFView()),
        requester=FinancialReportGenerator(FinancialDataMapper()),
    )
    pdf_presentation = pdf_controller.handle()

    # Show Web View
    web_controller = FinancialReportController(
        report_id=2,
        presenter=ScreenPresenter(WebView()),
        requester=FinancialReportGenerator(FinancialDataMapper()),
    )
    web_presentation = web_controller.handle()
