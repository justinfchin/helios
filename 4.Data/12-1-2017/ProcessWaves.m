function ProcessWaves(file)
close all
Fs = 44100;
load(file) %remove this line when copying the entire script to test for sound
%%data = trim_cardboard_vol15;% the data name

a = abs(fft(data));
figure(1)
num_bins = length(a);
plot([0:1/(num_bins/2 -1):1], a(1:num_bins/2))
%plot(a(1:1000))
title('FFT of Raw Data')
xlabel('Normalised frequency')
ylabel('Magnitude')
%create Butter filter co
[B, A] = butter(20, 0.4, 'low');
%apply Butter filter
filtered = filter(B,A,data);

%lets see how this compares with the fft of input
b = abs(fft(filtered));
figure(2)
num_bins = length(b);
plot([0:1/(num_bins/2 -1):1], b(1:num_bins/2))
title('FFT of Butter filtered data')
xlabel('Normalised frequency')
ylabel('Magnitude')
%testing the sound difference
%1st sound is original
%2nd sound is filtered
%sound(data,Fs);
%sound(filtered,Fs);
figure(3)
plot(data)
xlabel('Time')
ylabel('Amplitude')
title('Raw data from LDV')
figure(4)
plot(filtered)
xlabel('Time')
ylabel('Amplitude')
title('Filtered Data with Butter')
%testing the sound difference
%1st sound is original
%2nd sound is filtered
%sound(data,Fs);
%sound(filtered,Fs);





