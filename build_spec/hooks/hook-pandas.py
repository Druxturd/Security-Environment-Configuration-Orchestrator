from PyInstaller.utils.hooks import collect_data_files, collect_submodules

datas = collect_data_files("pandas", include_py_files=True)
hiddenimports = collect_submodules("pandas")
