#TESTING FOR python_speech_features
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav

####TESTING FOR DIFFERENT MFCC'S
from mel_coefficients import mfcc as mfcc2

(rate,sig) = wav.read("english.wav")
mfcc_feat = mfcc(sig,rate)
mfcc_feat2 = mfcc2(sig,rate,13)

d_mfcc_feat = delta(mfcc_feat, 2)
fbank_feat = logfbank(sig,rate)



print mfcc_feat.shape
print mfcc_feat2.shape
print mfcc_feat2.transpose().shape

