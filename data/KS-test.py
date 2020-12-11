import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import seaborn as sns
import tqdm
import os
from scipy import stats


def index(start_h0, end_h0, step_h0): # scale height index , default= (0.01, 0.5, 0.01)
    index_num = int((end_h0 - start_h0)/step_h0)
    index_h0  = [ round(start_h0 + step_h0*i, 4) for i in range(index_num + 1)]
    return index_h0

def columns(start_r, end_r, step_r): # radius of the toy galaxy, default = (9, 18.5, 0.5)
    index_num = int(( end_r - start_r)/step_r)
    index_r   = [ round(start_r +  step_r*i, 3) for i in range(index_num + 1)]
    return index_r



class Statistics():
    def __init__(self, R, std, std_lu, l_mu, number):
        self.R      = R
        self.l_mu  = l_mu
        self.std    = std
        self.std_lu = std_lu
        self.number = number
        self.std    = std
    def gaussian(self):
        const = 1/(np.sqrt(2*np.pi)*self.std)
        expo  = np.exp(-((t-mu)**2/(self.std**2)))
        return const * expo

    def model(self): # TOY MODEL
        np.random.seed(777)
        theta  = np.random.uniform(0, 2*np.pi, self.number)
        np.random.seed(778)
        r       = np.random.exponential(self.R, self.number)
        mx, my = r*np.cos(theta), r*np.sin(theta)
        np.random.seed(779)
        mz     = np.random.normal(loc=0, scale=self.std, size=self.number)
        np.random.seed(780)
        lu_log10   = np.random.normal(loc=self.l_mu, scale=self.std_lu, size=self.number)
        model = np.vstack([mx,my,mz,lu_log10])
        return model

class KStest(): # Kolmogorov-Smirnov test
    def __init__(self, model, real, gc, sun, bins):
        self.model = model
        self.real  = real
        self.gc    = gc
        self.sun   = sun # -8.2 kpc
        self.bins  = bins
    def ks_test(self):
        kpc_pc = 1000
        pc_m   = 3.0 * 10 ** 16
        W_Jy   = 10 ** 26
        mx, my, mz = [ self.model[i] - self.sun[i] for i in range(len(self.sun)) ]
        lu_log10 = self.model[3]
        rl = np.array([float(x)-360 if float(x)>180 else float(x) for x in self.real[1]])
        rb = np.array([float(x) for x in self.real[2]]) 
        rf = np.array([float(x) for x in self.real[6]])
        r_xyz = np.sqrt(mx**2+my**2+mz**2)
        D2 = r_xyz**2 * kpc_pc**2 * pc_m**2
        mf = (10**lu_log10*W_Jy)/(4*np.pi*D2)
        i_obs = np.where(mf>rf.min())[0]
        # LATITUDE AND LONGITUDE
        r_xyz = np.sqrt(mx**2+my**2+mz**2)
        r_xy  = np.sqrt(mx**2+my**2)
        ml = np.array([np.arccos(my[i]/r_xy[i])*360/(2*np.pi) if mx[i]<0 else -np.arccos(my[i]/r_xy[i])*360/(2*np.pi) for i in range(len(my)) ])
        mb = np.arcsin(mz/r_xyz)*360/(2*np.pi)
        i_obs_sta = []
        for i in i_obs:
            if -28<=ml[i]<=-self.gc or self.gc<=ml[i]<=10 or 14.35 <=ml[i] <= 67.25:
                if -1.25 <=mb[i]<=1.25:
                    i_obs_sta.append(i)
        i_notgc = []
        for i, l in enumerate(rl):
            if not -self.gc<l<self.gc:
                i_notgc.append(i)
        real_hist = plt.hist(rb[i_notgc],density=True, bins=self.bins)
        model_hist = plt.hist(mb[i_obs_sta], density=True,bins=self.bins)
        p_value = round(stats.ks_2samp(real_hist[0], model_hist[0]).pvalue,3)
        print(p_value)
        print('number of stars','real',len(i_notgc), 'model',len(i_obs_sta))
        print('p_value is ',p_value)
        return p_value

class Drawing():
    def __init__(self, color,linewidth, alpha):
        self.color = color
        self.linewidth = linewidth
        self.alpha = alpha

def main():
    CURRENT_DIRECTORY = os.getcwd()
    BASE_DIRECTORY = 'PATH2DATA'
    EXPERIMENT_CODE      = 'sh_res_nea' # TODO
    SL = index(1,21,1)# start, end, step [kpc]
    SH = columns(0.05, 0.4, 0.01) # start, end, step [kpc] #TODO
    SOURCES = 100000 # number of modeled maser sources 
    GC = 4 # [degree] degree of ignoring longitude TODO
    L_MU = 15.3 # Mean value of luminosity distribution. default = 15.3 (NEAR DISTANCE), 15.5 (FAR DISTANCE)(Engels and Bunzel, 2015) # TODO
    FWHM_L = 1.25 # FWHM value of luminosity distribution. default = 1.25 (Engels and Bunzel, 2015)
    std_lu = round(FWHM_L/ (2*np.sqrt(2*np.log(2))),3)
    SUN = np.array([0, -8.2,-0.017]) # same parameter setting as Engels and Bunzel, 2015. *Initial position AT X-axis. # TODO
    REAL = np.load('../data/stat.npy') # np.array([name, gl, gb, radial-velocity, expansion-velocity... etc])
    BINS = 21 # Number of bins of histgram to K-S test.
    results = np.zeros((len(SH),len(SL))) # R, scale height, p-value
    t = time.time()
    #for i, r in enumerate(R):
    for i, r in enumerate(SL):
        for j, h in enumerate(SH):
            print('')
            print('##################################')
            print('Model:','radi', r,'[kpc]','height',int(h*1000),'[pc]')
            print('')
            std = round(h/np.sqrt(2),4) # [kpc]
            statistics = Statistics(r, std, std_lu, L_MU, SOURCES)
            model = statistics.model()
            kstest = KStest(model, REAL, GC, SUN, BINS)
            pvalue = kstest.ks_test()
            results[j][i] = pvalue
            print('')
        print('##################################')
    t_ = time.time()
    practice_time = (t_ - t) /60
    df = pd.DataFrame(data=results, index=SH, columns=SL)
    df.to_pickle(BASE_DIRECTORY+EXPERIMENT_CODE + 'R.pkl')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    sns.heatmap(df, annot=False, square=True, cmap='viridis')
    plt.savefig(BASE_DIRECTORY+ EXPERIMENT_CODE, transparent =True, dpi = 300)
    print('RESULTS SAVED AT: ', BASE_DIRECTORY)
    print ('RUN TIME IS: ' , round(practice_time,3), '[min]')
    return
if __name__=='__main__':
    main()
