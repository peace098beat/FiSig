#! coding:utf-8
"""
    fisig.spectrogram.py
    ~~~~~~~~~~~~~~~~~

    スペクトログラムクラス. 信号データから時間-周波数解析されたスペクトログラムデータ.

    例えば.
        >>> from fisig.signal import Signal
        >>> spectrum = Signal().load_wav("./audio.wav", channel_no=(0,)).stft()
        >>> spectrum.info()


"""


def log10(data):
    from numpy import log10 as nplog10
    return nplog10(data)


class Spectrogram(object):
    """Spectrogramクラスは, 信号データを周波数分析した結果のクラスです.
    ここでSpectrogramとは時間-周波数軸上の2次元データとなります.
    主に信号データを解析した後に生成されるため, Spectrogramクラスを直接生成することはできません.

    :propaty data ndarray<time, frequency>:

    使い方
    ----

        from fisig.spectrum import Signal

        >>> spcgram = Signal().load_wav("./audio.wav", (0)).stft()
        >>> spcgram.info()
        spcgram.amp
        spcgram.pow
        spcgram.logamp
        spcgram.logpow
        spcgram.f_data
        spcgram.fk_data
        spcgram.t_data
        spcgram.tms_data

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
    