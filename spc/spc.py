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
    def __init__(self, data, t, sl, n=6):
        if isinstance(data, list):
            self.data = data
        self.t = t
        self.sl = sl
        self.n = n
        self._usl = t + (float(sl) / 2)
        self._lsl = t - (float(sl) / 2)

    """
    calculates capability
    """
    def calc_capability(self):
        r = self.__calc_mean_range()
        self._sigma = r / constant.DN[self.n]
        return round(self.sl / (6*self._sigma), 2)
    
    '''
    caculates capability index
    '''
    def calc_capability_index(self):
        r = self.__calc_mean_range()
        self._sigma = r / constant.DN[self.n]
        x = self.__calc_mean()
        return round(min((self._usl - x)/(3*self._sigma), (x - self._lsl)/(3*self._sigma)), 2)

    '''
    calculates the mean of max amplitude of samples
    '''
    def __calc_mean_range(self):
        r = []
        i = 0
        empty = False
        while not empty:
            if i*self.n + self.n < len(self.data):
                aux = self.data[i*self.n:i*self.n + self.n]
            else:
                aux = self.data[i*self.n:len(self.data)]
                empty = True
            i = i + 1
            r.append(max(aux) - min(aux))
        return mean(r)
    
    '''
    calculates the mean of the mean of samples
    '''
    def __calc_mean(self):
        _mean = []
        i = 0
        empty = False
        while not empty:
            if i*self.n + self.n < len(self.data):
                _mean.append(mean(self.data[i*self.n:i*self.n + self.n]))
            else:
                _mean.append(mean(self.data[i*self.n:len(self.data)]))
                empty = True
            i = i + 1
        return mean(_mean)