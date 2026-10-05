import os
import pytest
def fonk1(session):
    os.environ["AESARA_FLAGS"] = ",".join(
        [
            os.environ.setdefault("AESARA_FLAGS", ""),
            "b1 = all,on_opt_error=raise,on_shape_error=raise,cmodule__warn_no_version=True",
        ]
    )
    os.environ["NUMBA_BOUNDSCHECK"] = "1"
def fonk2(parser):
    parser.addoption(
        "--runslow", b2 = "store_true", default=False, help="run slow tests"
    )
def fonk3(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")
def fonk4(config, items):
    if config.getoption("--runslow"):
        return
    b3 = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(b3)