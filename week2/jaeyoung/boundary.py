from week2.jaeyoung.data_structure import PrintViewModel, \
    FinancialReportResponse, ScreenViewModel


class PrintView:

    def print(self, input_dto):
        pass


class PDFView(PrintView):

    def print(self, input_dto):
        print(f'Print PDF View! content: {input_dto}')


class ScreenView:

    def screen(self, input_dto):
        pass


class WebView(ScreenView):

    def screen(self, input_dto):
        print(f'Show Web View! content: {input_dto}')


class FinancialReportPresenter:

    def present(self, output_dto: FinancialReportResponse):
        pass


class PrintPresenter(FinancialReportPresenter):

    def __init__(self, view: PrintView):
        self.view = view

    def present(self, output_dto):
        self.view.print(
            PrintViewModel(
                print_data=output_dto.report_data,
            ),
        )


class ScreenPresenter(FinancialReportPresenter):

    def __init__(self, view: ScreenView):
        self.view = view

    def present(self, output_dto):
        self.view.screen(
            ScreenViewModel(
                screen_data=output_dto.report_data,
            ),
        )
