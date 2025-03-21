from ml_tto.automatic_emittance.scan_cropping import crop_scan
import numpy as np


class TestScanCropping:
    def test_cropping_without_cutoff_max(self):
        x = np.array(
            [
                1.6,
                -5.0,
                -2.5,
                0.0,
                1.0,
                2.5,
                5.0,
                1.32652795,
                0.91836554,
                0.7142843,
                0.51020312,
                0.30612189,
                0.10204065,
                0.91836554,
                0.91836554,
                0.91836554,
                6.0,
            ]
        )
        y = np.array(
            [
                0.00025466,
                0.00064587,
                0.0003674,
                0.00025124,
                np.nan,
                0.00030424,
                0.00064788,
                0.00024831,
                0.000256,
                0.00024105,
                0.00025109,
                0.00025661,
                0.00025207,
                0.00024721,
                0.00024402,
                0.00024574,
                np.nan,
            ]
        )

        x_cropped, y_cropped = crop_scan(x, y)

        assert np.allclose(
            x_cropped,
            np.array(
                [
                    1.6,
                    -2.5,
                    2.5,
                    1.32652795,
                    0.91836554,
                    0.7142843,
                    0.91836554,
                    0.91836554,
                    0.91836554,
                ]
            ),
            rtol=1.0e-1,
        )
        assert np.allclose(
            y_cropped,
            np.array(
                [
                    0.00025466,
                    0.0003674,
                    0.00030424,
                    0.00024831,
                    0.000256,
                    0.00024105,
                    0.00024721,
                    0.00024402,
                    0.00024574,
                ]
            ),
            rtol=1.0e-1,
        )

    def test_cropping_with_cutoff_max(self):
        x = np.array(
            [
                -75.0,
                -67.10526,
                -51.31579,
                -43.42105,
                -35.526318,
                -27.63158,
                -19.736843,
                -11.842106,
                -3.9473724,
                3.9473724,
                11.842106,
                19.736843,
                27.63158,
                35.526318,
                43.42105,
                51.31579,
                59.210526,
                67.10526,
                75.0,
                -59.210526,
                500.0,
            ]
        )

        y = np.array(
            [
                np.nan,
                0.00150532,
                0.00088447,
                0.00070892,
                0.00047886,
                0.00020754,
                0.000376,
                0.00069786,
                0.00100929,
                0.00136199,
                0.00173777,
                0.00218552,
                0.00268864,
                0.0033956,
                0.00401786,
                0.00390501,
                0.00382698,
                0.00363087,
                np.nan,
                0.0008867,
                np.nan,
            ]
        )

        x_cropped, y_cropped = crop_scan(x, y, cutoff_max=10)

        assert np.allclose(
            x_cropped,
            np.array(
                [
                    -67.10526,
                    -51.31579,
                    -27.63158,
                    -19.736843,
                    -11.842106,
                    3.9473724,
                    11.842106,
                    19.736843,
                    27.63158,
                    67.10526,
                    -59.210526,
                ]
            ),
            rtol=1.0e-1,
        )
        assert np.allclose(
            y_cropped,
            np.array(
                [
                    0.00150532,
                    0.00088447,
                    0.00020754,
                    0.000376,
                    0.00069786,
                    0.00136199,
                    0.00173777,
                    0.00218552,
                    0.00268864,
                    0.00363087,
                    0.0008867,
                ]
            ),
            rtol=1.0e-1,
        )
