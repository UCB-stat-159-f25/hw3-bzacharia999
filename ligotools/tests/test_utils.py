from ligotools.utils import *
import numpy as np
import pytest

def test_reqshift():
    """Asserts that the output length is unchanged and the output is an np.array"""
    
   
    data_in = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    fshift_in = 1.0
    sample_rate_in = 8.0
    
    shifted_data = reqshift(data_in, fshift=fshift_in, sample_rate=sample_rate_in)

    assert len(shifted_data) == 8

    assert isinstance(shifted_data, np.ndarray)



def test_whiten_output_shape_simple():
    """
    Asserts that the output array length equals the input array length
    by using a simple locally-defined function for the PSD.
    """
    
    def psd_func(freqs):
        """returns 1.0 for the PSD value."""
        # Use a numpy array of ones to match the shape of the input freqs
        return np.ones_like(freqs)

    strain_in = np.array([1, 0, 0, 0, 0, 0, 0, 0])
    dt_in = 1.0
    
    white_ht = whiten(strain_in, psd_func, dt_in)

    assert len(white_ht) == 8

    assert isinstance(white_ht, np.ndarray)
