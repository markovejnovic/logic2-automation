from contextlib import contextmanager
import os.path
import threading
import time

from saleae import automation


def test_add_analyzer(manager: automation.Manager, asset_path: str):
    path = os.path.join(asset_path, 'small_spi_capture.sal')

    hla_root_path = os.path.join(asset_path, 'hla/test')
    hla_entry_point = 'test_hla.Hla'

    with manager.load_capture(path) as cap:
        for bitty in [8]:
            analyzer = cap.add_analyzer('SPI', label=f'SPI (bits={bitty})', settings={
                'MISO': 4,
                'Clock': 3,
                'Enable': 5,
                'Bits per Transfer': f'{bitty} Bits per Transfer{" (Standard)" if bitty == 8 else ""}'
            })

            hla = cap.add_high_level_analyzer(hla_root_path, hla_entry_point, input_analyzer=analyzer, label='hi', settings={
                'my_choices_setting': 'A',
                'my_string_setting': 'hi',
                'my_number_setting': 100,
            })

            # time.sleep(3)

            cap.remove_analyzer(hla)

            cap.remove_analyzer(analyzer)

            # time.sleep(10)