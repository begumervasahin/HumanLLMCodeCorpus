from threading import Event
from globalconsts import NUM_OF_DATASERVERS
OPERATION = None
main2name_event = Event()
name2main_event = Event()
name2data_events = [Event() for _ in range(NUM_OF_DATASERVERS)]
data2name_events = [Event() for _ in range(NUM_OF_DATASERVERS)]
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
NameNode_Flag = None
NameNode_error_messages = None
DataNode_Flag = None
DataNode_error_messages = None
ls_results = []
read_results = {}
fetch_results = {}