function datasound(file)
close all
clear sound
Fs = 44100;
load(file) %remove this line when copying the entire script to test for sound
%%data = trim_cardboard_vol15;% the data name

a = abs(fft(data));
sound(data*50,Fs);
figure
plot(data)
xlabel('Time')
ylabel('Amplitude')
title('Raw data from LDV')