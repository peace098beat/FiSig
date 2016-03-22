#! coding:utf-8
"""
    fisig.signal.py
    ~~~~~~~~~~~~~~~

    シグナルクラス. 信号データクラス. wavファイルやcsv等から読み込んだ1次元データ
    に対して, 信号処理を行うことができる.

"""


class Signal(object):
    """Signalクラスは信号処理における最初の重要なクラスです.
    信号を.wavファイルやcsvファイルからロードすることから始まり,
    読み込んだ信号データに対し, 準備されている信号処理を行うことができます.

    使い方
    ----

        from fisig.signal import Signal

        >>> sig = Signal()
        >>> sig.load_wav('./audio.wav', channel_no=0)
        print sig.fs
        print sig.data.shape
        print sig.get_times

        spectrum = sig.fft("hanning")
        spectrogram = sig.stft(256, "hanning", 125, 0.5)


    """

    def __init__(self):
        self.filepath = None
        self.fs = None
        self.channel_no = None

        self._data_org = np.array_empty([])
        self.data = np.array_empty([])
        self.xdata = np.array_empty([])

        self.tdata = None

    def info(self):
        """ロードされた信号データの詳細を表示します."""
        pass

    def load_wav(self, wavfilepath, channel_no):
        """wavファイルからオーディオデータを読み込みます. Signalクラスに保持さるのは1チャンネル分のデータになります.
        もし, wavファイルに複数のチャンネルが含まれている場合は:param:channel_no<tuple>にて指定可能です.
        例えば:param:channel_noに(0,1)と指定すると, (ch1+ch2)/2と平均化されます.これは複数チャンネルでも同じです.
        """
        self.filepath = wavfilepath
        self.channel_no = channel_no
        # self.data, self.fs = _load_wav(self.filepath, self.channel_no)
        return self

    def fft(self):
        return Spectrum
        pass

    def slice_smp(self, start, end):
        """信号処理の対象となるサンプルの範囲を指定します.

            >>> sig = Signal().load_wav("./audio.wav", channel_no=(0,1))
            >>> sig.info()
            samples : 0-249999 [n]
            fs : 44100 [Hz]
            tdata: 0-0.5 [ms]
            >>> sig.slice_ms(0.1,0.2)
            >>> sig.info()
            fs : 44100[Hz]
            samples : 2500-12000 [n]
            times: 0.1-0.2 [ms]
        """
        self.data = self._data_org(start, end)
        pass

    def slice_ms(self, start, end):
        """信号処理の対象となるサンプルの範囲を指定します.

            >>> sig = Signal().load_wav("./audio.wav", channel_no=(0,1))
            >>> sig.info()
            samples : 0-249999 [n]
            fs : 44100 [Hz]
            tdata: 0-0.5 [ms]
            >>> sig.slice_ms(0.1,0.2)
            >>> sig.info()
            fs : 44100[Hz]
            samples : 2500-12000 [n]
            times: 0.1-0.2 [ms]
        """
        pass

    # helper
    def _ms2smp(self, ms, smp):
        pass

    def _smp2ms(self, smp, ms):
        pass
