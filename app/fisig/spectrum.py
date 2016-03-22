#! coding:utf-8
"""
    fisig.spectrum.py
    ~~~~~~~~~~~~~~~~~

    スペクトルクラス. 信号データから周波数解析されたスペクトルデータ.

    例えば.

        >>> spectrum = Signal().load_wav("./audio.wav", (0)).fft()
        >>> spectrum.info()


"""


def log10(data):
    from numpy import log10 as nplog10
    return nplog10(data)


class Spectrum(object):
    """Spectrumクラスは, 信号データを周波数分析した結果のクラスです.
    ここでSpectrumとは周波数軸上の1次元データとなります.
    主に信号データを解析した後に生成されるため, Spectrumクラスを直接生成することはできません.

    使い方
    ----

        from fisig.spectrum import Signal

        >>> spec = Signal().load_wav("./audio.wav", (0)).fft()
        >>> spec.info()
        spec.amp
        spec.pow
        spec.logamp
        spec.logpow
        spec.fdata
        spec.fkdata

    """

    def __init__(self):
        self.data = None
        self.fdata = None

    def info(self):
        """スペクトルデータの詳細を表示します."""
        pass

    @property
    def amplitude(self):
        return 10 * log10(self.data)

    @property
    def power(self):
        return 20 * log10(self.data)

    def liftering(self, mode, l):
        pass

    def smothing(self):
        pass

    def plot(self):
        pass

    def show(self):
        pass

    def save(self, figname):
        pass
