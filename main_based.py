import interface_based as ui
import logger_based as lg
import crud_based

lg.logging.info('Start')
crud_based.init_data_base('base_info.csv')
ui.ls_menu()