from threading import Event
from globalconsts import NUM_OF_DATASERVERS
OPERATION = None
main_to_name_event = Event()
name_to_main_event = Event()
name_to_data_events = [Event() for _ in range(NUM_OF_DATASERVERS)]
data_to_name_events = [Event() for _ in range(NUM_OF_DATASERVERS)]
global_flag = False
upload_file = None
fetch_file_id = None
fetch_save_file = None
read_file_id = None
read_offset = None
read_count = None
upload_server_block_map = None
fetch_server_block_map = {}
fetch_id_block_map = {}
read_server_block_map = {}
read_block_config = {}
name_node_flag = None
name_node_error_messages = None
data_node_flag = None
data_node_error_messages = None
ls_results = []
read_results = {}
fetch_results = {}