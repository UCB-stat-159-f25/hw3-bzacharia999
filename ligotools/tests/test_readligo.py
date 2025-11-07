from ligotools.readligo import *
import pytest

def test_read_hdf5_asserts_file_not_found_error():
    """
    Asserts that read_hdf5 raises FileNotFoundError when given a non-existent file
    """
    
    non_existent_file = "dummy_filename.hdf5"

    with pytest.raises(FileNotFoundError) as excinfo:
        read_hdf5(non_existent_file)


def test_dq2segs():

    bad_channel_dict = {
        'OTHER_FLAG': [1, 0, 1, 0],
        'DUMMY_FLAG': [0, 1, 0, 1]
    }
    gps_start = 1234567890 

    with pytest.raises(KeyError):
        dq2segs(bad_channel_dict, gps_start)


    

