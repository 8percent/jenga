from week2.jaeyoung.boundary import PrintPresenter, PDFView, ScreenPresenter, \
    WebView
from week2.jaeyoung.repository import FinancialDataMapper
from week2.jaeyoung.usecase import FinancialReportController, \
    FinancialReportGenerator

if __name__ == '__main__':

    # Print PDF
    pdf_presentation = FinancialReportController(
        report_id=1,
        presenter=PrintPresenter(PDFView()),
        requester=FinancialReportGenerator(FinancialDataMapper()),
    )

    # Show Web View
    web_presentation = FinancialReportController(
        report_id=1,
        presenter=ScreenPresenter(WebView()),
        requester=FinancialReportGenerator(FinancialDataMapper()),
    )
