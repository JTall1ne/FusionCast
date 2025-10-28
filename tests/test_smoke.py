def test_import():
    import importlib
    module = importlib.import_module("fusioncast")
    assert module is not None
