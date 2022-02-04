from dataclasses import dataclass


@dataclass
class FinancialReportRequest:
    id: int


@dataclass
class FinancialReportResponse:
    id: int
    report_data: dict


@dataclass
class PrintViewModel:
    print_data: dict


@dataclass
class ScreenViewModel:
    screen_data: dict
