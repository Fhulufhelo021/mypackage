from mypackage import myModule

def test_top_n():
    """
    make sure top_n works correctly
    """
    assert myModule.top_n([8,3,2,7,4],3) == [8,7,4], 'incorrect'
    assert myModule.top_n([8,3,2,7,4],3) == [8,7,2], 'incorrect'
    assert myModule.top_n([8,3,2,7,4],3) == [3,7,4], 'incorrect'