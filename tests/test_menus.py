import src.menus as menus


# ==================================================
# choose_currency
# ==================================================

def test_choose_currency_valid(mocker):

    mocker.patch(
        "src.menus.get_available_currencies",
        return_value=["USD", "EUR", "GBP"]
    )

    mocker.patch(
        "builtins.input",
        return_value="2"
    )

    assert menus.choose_currency() == "EUR"


def test_choose_currency_return(mocker):

    mocker.patch(
        "src.menus.get_available_currencies",
        return_value=["USD", "EUR"]
    )

    mocker.patch(
        "builtins.input",
        return_value="3"
    )

    assert menus.choose_currency() is None


# ==================================================
# choose_period
# ==================================================

def test_choose_period_week(mocker):

    mocker.patch(
        "builtins.input",
        return_value="1"
    )

    assert menus.choose_period() == 7


def test_choose_period_two_weeks(mocker):

    mocker.patch(
        "builtins.input",
        return_value="2"
    )

    assert menus.choose_period() == 14


def test_choose_period_month(mocker):

    mocker.patch(
        "builtins.input",
        return_value="3"
    )

    assert menus.choose_period() == 30


def test_choose_period_return(mocker):

    mocker.patch(
        "builtins.input",
        return_value="7"
    )

    assert menus.choose_period() is None


# ==================================================
# choose_start_date
# ==================================================

def test_choose_start_date_valid(mocker):

    mocker.patch(
        "builtins.input",
        return_value="2024-01-01"
    )

    mocker.patch(
        "src.menus.validate_date",
        return_value=True
    )

    assert menus.choose_start_date() == "2024-01-01"


def test_choose_start_date_return(mocker):

    mocker.patch(
        "builtins.input",
        return_value="R"
    )

    assert menus.choose_start_date() is None


# ==================================================
# display_menu
# ==================================================

def test_display_menu_yes(mocker):

    mocker.patch(
        "builtins.input",
        return_value="YES"
    )

    assert menus.display_menu() == "YES"


def test_display_menu_no(mocker):

    mocker.patch(
        "builtins.input",
        return_value="NO"
    )

    assert menus.display_menu() == "NO"


# ==================================================
# export_menu
# ==================================================

def test_export_menu_yes(mocker):

    mocker.patch(
        "builtins.input",
        return_value="YES"
    )

    assert menus.export_menu() == "YES"


def test_export_menu_no(mocker):

    mocker.patch(
        "builtins.input",
        return_value="NO"
    )

    assert menus.export_menu() == "NO"


# ==================================================
# continue_menu
# ==================================================

def test_continue_menu_yes(mocker):

    mocker.patch(
        "builtins.input",
        return_value="YES"
    )

    assert menus.continue_menu() == "YES"


def test_continue_menu_no(mocker):

    mocker.patch(
        "builtins.input",
        return_value="NO"
    )

    assert menus.continue_menu() == "NO"


# ==================================================
# session_analysis_flow
# ==================================================

def test_session_analysis_flow_export(mocker):

    mocker.patch(
        "src.menus.choose_currency",
        return_value="USD"
    )

    mocker.patch(
        "src.menus.choose_period",
        return_value=30
    )

    mocker.patch(
        "src.menus.get_currency_data",
        return_value=[1, 2, 3]
    )

    mocker.patch(
        "src.menus.analyze_sessions",
        return_value=(10, 5, 2)
    )

    mocker.patch(
        "src.menus.display_menu",
        return_value="NO"
    )

    mocker.patch(
        "src.menus.export_menu",
        return_value="YES"
    )

    mocker.patch(
        "builtins.input",
        return_value="session.csv"
    )

    export_mock = mocker.patch(
        "src.menus.export_session_analysis"
    )

    menus.session_analysis_flow()

    export_mock.assert_called_once_with(
        "session.csv",
        "USD",
        "30",
        10,
        5,
        2
    )


def test_session_analysis_flow_no_data(mocker):

    mocker.patch(
        "src.menus.choose_currency",
        return_value="USD"
    )

    mocker.patch(
        "src.menus.choose_period",
        return_value=30
    )

    mocker.patch(
        "src.menus.get_currency_data",
        return_value=[]
    )

    menus.session_analysis_flow()


# ==================================================
# statistics_flow
# ==================================================

def test_statistics_flow_export(mocker):

    mocker.patch(
        "src.menus.choose_currency",
        return_value="USD"
    )

    mocker.patch(
        "src.menus.choose_period",
        return_value=30
    )

    mocker.patch(
        "src.menus.get_currency_data",
        return_value=[1, 2, 3]
    )

    mocker.patch(
        "src.menus.calculate_statistics",
        return_value={
            "median": 1.0,
            "mode": 1.0,
            "std_dev": 0.5,
            "variation": 5.0
        }
    )

    mocker.patch(
        "src.menus.display_menu",
        return_value="NO"
    )

    mocker.patch(
        "src.menus.export_menu",
        return_value="YES"
    )

    mocker.patch(
        "builtins.input",
        return_value="stats.csv"
    )

    export_mock = mocker.patch(
        "src.menus.export_statistics"
    )

    menus.statistics_flow()

    export_mock.assert_called_once_with(
        "stats.csv",
        "USD",
        "30",
        {
            "median": 1.0,
            "mode": 1.0,
            "std_dev": 0.5,
            "variation": 5.0
        }
    )


# ==================================================
# histogram_flow
# ==================================================

def test_histogram_flow_export(mocker):

    mocker.patch(
        "src.menus.choose_currency_for_histogram",
        side_effect=["USD", "EUR"]
    )

    mocker.patch(
        "src.menus.choose_start_date",
        return_value="2024-01-01"
    )

    mocker.patch(
        "src.menus.get_currency_data",
        return_value=[{"effectiveDate": "2024-01-01", "mid": 1}]
    )

    mocker.patch(
        "src.menus.create_currency_pair",
        return_value=[1, 2]
    )

    histogram = [{"interval": "0-10", "count": 5}]

    mocker.patch(
        "src.menus.build_histogram",
        return_value=histogram
    )

    mocker.patch(
        "src.menus.display_histogram"
    )

    mocker.patch(
        "src.menus.display_menu",
        return_value="NO"
    )

    mocker.patch(
        "src.menus.export_menu",
        return_value="YES"
    )

    mocker.patch(
        "builtins.input",
        side_effect=[
            "MONTHLY",        # analysis_type
            "histogram.csv"   # filename
        ]
    )

    export_mock = mocker.patch(
        "src.menus.export_histogram"
    )

    import src.menus as menus
    menus.histogram_flow()

    export_mock.assert_called_once_with(
        "histogram.csv",
        histogram
    )


# ==================================================
# start_application
# ==================================================

def test_start_application_exit(mocker):

    mocker.patch(
        "src.menus.main_menu",
        return_value="4"
    )

    menus.start_application()


def test_start_application_option_1(mocker):

    mocker.patch(
        "src.menus.main_menu",
        return_value="1"
    )

    flow_mock = mocker.patch(
        "src.menus.session_analysis_flow"
    )

    mocker.patch(
        "src.menus.continue_menu",
        return_value="NO"
    )

    menus.start_application()

    flow_mock.assert_called_once()


def test_start_application_option_2(mocker):

    mocker.patch(
        "src.menus.main_menu",
        return_value="2"
    )

    flow_mock = mocker.patch(
        "src.menus.statistics_flow"
    )

    mocker.patch(
        "src.menus.continue_menu",
        return_value="NO"
    )

    menus.start_application()

    flow_mock.assert_called_once()


def test_start_application_option_3(mocker):

    mocker.patch(
        "src.menus.main_menu",
        return_value="3"
    )

    flow_mock = mocker.patch(
        "src.menus.histogram_flow"
    )

    mocker.patch(
        "src.menus.continue_menu",
        return_value="NO"
    )

    menus.start_application()

    flow_mock.assert_called_once()