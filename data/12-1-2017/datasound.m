function datasound(file)

Fs = 44100;
load(file) %remove this line when copying the entire script to test for sound
%%data = trim_cardboard_vol15;% the data name

a = abs(fft(data));
sound(data,Fs);