import pytest

def test_analysis():
    from rzuefi.uefi_analyzer import UefiAnalyzer
    summary = UefiAnalyzer.get_summary("tests/bins/haiku_loader_amd64.efi")
    assert summary['p_guids'][2]['value'] == "BB25CF6F-F1D4-11D2-9A0C0090273FC1FD"
    assert summary['p_guids'][2]['name'] ==  "EFI_SERIAL_IO_PROTOCOL_GUID"
    summary = UefiAnalyzer.get_summary("tests/bins/bootia32.efi")
    assert summary['p_guids'][2]['name'] ==  "EFI_LOADED_IMAGE_PROTOCOL_GUID"
    assert summary['p_guids'][4]['name'] ==  "EFI_DEVICE_PATH_PROTOCOL_GUID"
    