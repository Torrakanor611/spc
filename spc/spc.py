from statistics import mean
from . import constant

class spc():
    '''
    calculates capability and capability index
    for a given data, target,
    specifications limit and sample size

    :param data: source data
    :type data: list
    :param t: Target
    :param sl: Specification limit
    :param n: Sample size
    '''
    def __init__(self, data, t, sl):
        if isinstance(data, list):
            self.data = data
        self.t = t
        self.sl = sl
        self._usl = t + (float(sl) / 2)
        self._lsl = t - (float(sl) / 2)

    '''
    calculates capability
    '''
    def calc_capability(self, n=None):
        _n = n if n is not None else constant.N
        r = self.__calc_mean_range(_n)
        self._sigma = r / constant.DN[_n]
        return round(self.sl / (6*self._sigma), 2)
    
    '''
    caculates capability index
    '''
    def calc_capability_index(self, n=None):
        _n = n if n is not None else constant.N
        r = self.__calc_mean_range(_n)
        self._sigma = r / constant.DN[_n]
        x = self.__calc_mean(_n)
        return round(min((self._usl - x)/(3*self._sigma), (x - self._lsl)/(3*self._sigma)), 2)

    '''
    calculates the mean of max amplitude of samples
    '''
    def __calc_mean_range(self, n):
        r = []
        i = 0
        empty = False
        while not empty:
            if i* n + n < len(self.data):
                aux = self.data[i*n:i*n + n]
            else:
                aux = self.data[i*n:len(self.data)]
                empty = True
            i = i + 1
            r.append(max(aux) - min(aux))
        return mean(r)
    
    '''
    calculates the mean of the mean of samples
    '''
    def __calc_mean(self, n):
        _mean = []
        i = 0
        empty = False
        while not empty:
            if i*n + n < len(self.data):
                _mean.append(mean(self.data[i*n:i*n + n]))
            else:
                _mean.append(mean(self.data[i*n:len(self.data)]))
                empty = True
            i = i + 1
        return mean(_mean)